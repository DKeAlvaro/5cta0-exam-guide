// Ask-the-guide: a small chat panel that answers questions about the current
// page using the reader's own LLM API key (stored only in localStorage).
// Highlighting text on the page pops up a button to ask about that passage.
(function () {
  const LS = {
    provider: "ssp-ask-provider",
    key: "ssp-ask-key",
    model: "ssp-ask-model",
    bases: "ssp-ask-bases",
  };

  const MAX_CONTEXT = 14000; // chars of page text sent as context
  const MAX_TURNS = 12; // messages kept in the conversation
  const MAX_SELECTION = 4000; // chars of highlighted text

  const ICONS = {
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    settings: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h9M19 7h1M4 17h3M13 17h7"/><circle cx="16" cy="7" r="2.3"/><circle cx="10" cy="17" r="2.3"/></svg>',
    send: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V6M6 12l6-6 6 6"/></svg>',
    chat: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12a7.5 7.5 0 0 1-7.5 7.5H8l-4 2.5V12A7.5 7.5 0 0 1 11.5 4.5h1A7.5 7.5 0 0 1 20 12z"/></svg>',
    quote: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 7h4v4a5.5 5.5 0 0 1-4 5v-2.2c1.2-.5 1.9-1.3 2-2.3H7V7zm8 0h4v4a5.5 5.5 0 0 1-4 5v-2.2c1.2-.5 1.9-1.3 2-2.3h-2V7z"/></svg>',
  };

  // Older defaults kept in localStorage get upgraded silently.
  const LEGACY_MODELS = {
    "gpt-4o-mini": "gpt-5.6-terra",
    "gpt-4o": "gpt-5.6-terra",
    "gemini-2.5-flash": "gemini-3.8-flash",
    "gemini-2.0-flash": "gemini-3.8-flash",
    "openai/gpt-4o-mini": "google/gemini-3.8-flash",
  };

  const PROVIDERS = {
    openai: {
      name: "OpenAI",
      keyHint: "sk-...",
      keyUrl: "https://platform.openai.com/api-keys",
      defaultModel: "gpt-5.6-terra",
      defaultBase: "https://api.openai.com/v1",
      baseHint: "https://api.openai.com/v1",
      build: (base, key, model, system, messages) => ({
        url: base.replace(/\/+$/, "") + "/chat/completions",
        headers: chatHeaders(key),
        body: { model: model, messages: [{ role: "system", content: system }].concat(messages.map((m) => ({ role: m.role, content: m.text }))) },
        read: (d) => d.choices[0].message.content,
      }),
    },
    gemini: {
      name: "Google Gemini",
      keyHint: "AIza...",
      keyUrl: "https://aistudio.google.com/apikey",
      defaultModel: "gemini-3.8-flash",
      defaultBase: "https://generativelanguage.googleapis.com/v1beta",
      baseHint: "https://generativelanguage.googleapis.com/v1beta",
      build: (base, key, model, system, messages) => {
        const headers = { "Content-Type": "application/json" };
        if (key) headers["x-goog-api-key"] = key;
        return {
          url: base.replace(/\/+$/, "") + "/models/" + encodeURIComponent(model) + ":generateContent",
          headers: headers,
          body: {
            system_instruction: { parts: [{ text: system }] },
            contents: messages.map((m) => ({
              role: m.role === "assistant" ? "model" : "user",
              parts: [{ text: m.text }],
            })),
          },
          read: (d) => {
            const c = d.candidates && d.candidates[0];
            return c && c.content ? c.content.parts.map((p) => p.text || "").join("") : "";
          },
        };
      },
    },
    openrouter: {
      name: "OpenRouter",
      keyHint: "sk-or-...",
      keyUrl: "https://openrouter.ai/keys",
      defaultModel: "google/gemini-3.8-flash",
      defaultBase: "https://openrouter.ai/api/v1",
      baseHint: "https://openrouter.ai/api/v1",
      build: (base, key, model, system, messages) => ({
        url: base.replace(/\/+$/, "") + "/chat/completions",
        headers: chatHeaders(key),
        body: { model: model, messages: [{ role: "system", content: system }].concat(messages.map((m) => ({ role: m.role, content: m.text }))) },
        read: (d) => d.choices[0].message.content,
      }),
    },
  };

  function chatHeaders(key) {
    const h = { "Content-Type": "application/json" };
    if (key) h.Authorization = "Bearer " + key;
    return h;
  }

  function loadBases() {
    try {
      return JSON.parse(localStorage.getItem(LS.bases)) || {};
    } catch (e) {
      return {};
    }
  }

  const state = {
    provider: localStorage.getItem(LS.provider) || "gemini",
    key: localStorage.getItem(LS.key) || "",
    model: localStorage.getItem(LS.model) || "",
    bases: loadBases(),
    selection: "", // highlighted passage to ask about
    history: [], // {role: "user"|"assistant", text}
    busy: false,
    open: false,
  };
  if (LEGACY_MODELS[state.model]) {
    state.model = LEGACY_MODELS[state.model];
    localStorage.setItem(LS.model, state.model);
  }

  /* ---------- page context ---------- */

  function pageContext() {
    const main = document.querySelector(".md-content__inner");
    if (!main) return "";
    const clone = main.cloneNode(true);
    clone.querySelectorAll("script, style, .noprint, #ask-panel, .md-content__button").forEach((n) => n.remove());
    // Give the model the LaTeX source instead of KaTeX's duplicated render.
    clone.querySelectorAll(".katex").forEach((katex) => {
      const ann = katex.querySelector('annotation[encoding="application/x-tex"]');
      const tex = ann ? ann.textContent.trim() : katex.textContent;
      katex.replaceWith(document.createTextNode(" $" + tex + "$ "));
    });
    const title = (document.querySelector("h1") || {}).textContent || document.title;
    const text = clone.textContent.replace(/[ \t\u00a0]+/g, " ").replace(/\n{3,}/g, "\n\n").trim();
    return ("Page: " + title + "\n\n" + text).slice(0, MAX_CONTEXT);
  }

  function systemPrompt() {
    return (
      "You are a tutor for 5CTA0 Statistical Signal Processing (TU/e). " +
      "The student is revising for the exam and asks about the material in this guide. " +
      "Answer only from the PAGE CONTENT below when the question is about the guide; " +
      "if it goes beyond it, say so and answer from general knowledge. " +
      "When a message starts with 'Selected passage', that is the exact text the student highlighted: " +
      "focus your answer on it and treat it as the immediate context. " +
      "Be concise and exam-focused: short derivation steps, state the formula before using it, " +
      "and point out the common mistakes the exams punish. " +
      "Write maths in LaTeX between $...$ (inline) or $$...$$ (display); never use MathML. " +
      "Reply in the same language the student writes in.\n\n--- PAGE CONTENT ---\n" +
      pageContext()
    );
  }

  /* ---------- tiny markdown renderer ---------- */

  function escapeHtml(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function inline(s) {
    return s
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[\s(])\*([^*\n]+)\*(?=[\s).,;:!?]|$)/g, "$1<em>$2</em>");
  }

  function renderMarkdown(src) {
    const parts = String(src).split(/```/);
    let html = "";
    parts.forEach((chunk, i) => {
      if (i % 2) {
        const body = chunk.replace(/^[a-zA-Z0-9+#-]*\n/, "");
        html += "<pre><code>" + escapeHtml(body) + "</code></pre>";
        return;
      }
      chunk.split(/\n{2,}/).forEach((block) => {
        const b = block.trim();
        if (!b) return;
        const lines = b.split("\n");
        const isList = lines.every((l) => /^\s*([-*]|\d+\.)\s+/.test(l));
        if (/^#{1,6}\s/.test(b)) {
          const level = Math.min(6, b.match(/^#+/)[0].length);
          html += "<h" + level + ">" + inline(escapeHtml(b.replace(/^#+\s*/, ""))) + "</h" + level + ">";
        } else if (isList) {
          const ordered = /^\s*\d+\./.test(lines[0]);
          html += "<" + (ordered ? "ol" : "ul") + ">" +
            lines.map((l) => "<li>" + inline(escapeHtml(l.replace(/^\s*([-*]|\d+\.)\s+/, ""))) + "</li>").join("") +
            "</" + (ordered ? "ol" : "ul") + ">";
        } else {
          html += "<p>" + inline(escapeHtml(b)).replace(/\n/g, "<br>") + "</p>";
        }
      });
    });
    return html;
  }

  function renderMath(el) {
    if (typeof renderMathInElement !== "function") return;
    try {
      renderMathInElement(el, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\[", right: "\\]", display: true },
          { left: "\\(", right: "\\)", display: false },
        ],
        throwOnError: false,
      });
    } catch (e) { /* math is optional */ }
  }

  /* ---------- selection button ---------- */

  let selBtn = null;

  function hideSelectionBtn() {
    if (selBtn) selBtn.style.display = "none";
  }

  function showSelectionBtn() {
    const sel = window.getSelection();
    const text = sel ? String(sel).replace(/\s+/g, " ").trim() : "";
    const content = document.querySelector(".md-content__inner");
    const inContent = (n) => n && content && content.contains(n.nodeType === 1 ? n : n.parentNode);
    if (!sel || sel.isCollapsed || text.length < 3 || text.length > MAX_SELECTION ||
        !inContent(sel.anchorNode) || !inContent(sel.focusNode) || state.open) {
      hideSelectionBtn();
      return;
    }
    const range = sel.getRangeAt(0);
    const rects = range.getClientRects();
    const r = rects.length ? rects[rects.length - 1] : range.getBoundingClientRect();
    if (!r || (!r.top && !r.left)) { hideSelectionBtn(); return; }

    if (!selBtn) {
      selBtn = document.createElement("button");
      selBtn.id = "ask-select-btn";
      selBtn.type = "button";
      selBtn.title = "Ask about the selected text";
      selBtn.innerHTML = ICONS.quote + '<span>Ask about this</span>';
      selBtn.addEventListener("mousedown", (e) => e.preventDefault()); // keep the selection
      selBtn.addEventListener("click", () => {
        const t = selBtn.dataset.text || "";
        hideSelectionBtn();
        toggle(true);
        setSelection(t);
        if (el.input) el.input.focus();
      });
      document.body.appendChild(selBtn);
    }
    selBtn.dataset.text = text;
    selBtn.style.display = "flex";
    const w = selBtn.offsetWidth || 110;
    const x = Math.min(Math.max(8, r.left + r.width / 2 - w / 2), window.innerWidth - w - 8);
    const above = r.top > 52;
    selBtn.style.left = x + "px";
    selBtn.style.top = (above ? r.top - 40 : Math.min(r.bottom + 8, window.innerHeight - 52)) + "px";
    selBtn.classList.toggle("below", !above);
  }

  function setSelection(text) {
    state.selection = (text || "").slice(0, MAX_SELECTION);
    if (el.quote) {
      el.quote.classList.toggle("open", !!state.selection);
      el.quoteText.textContent = state.selection.length > 240
        ? state.selection.slice(0, 240) + "…"
        : state.selection;
      if (el.input) {
        el.input.placeholder = state.selection
          ? "Ask about the selected passage…"
          : "Ask about the topics on this page…";
      }
    }
  }

  /* ---------- UI ---------- */

  let el = {};

  function build() {
    if (document.getElementById("ask-panel")) return;
    const wrap = document.createElement("div");
    wrap.id = "ask-panel";
    wrap.innerHTML =
      '<div class="ask-head">' +
        '<div class="ask-head-text">' +
          '<span class="ask-title">Ask the guide</span>' +
          '<span class="ask-sub">5CTA0 tutor &middot; your own API key</span>' +
        '</div>' +
        '<button type="button" class="ask-icon" data-act="settings" title="API key settings">' + ICONS.settings + '</button>' +
        '<button type="button" class="ask-close" data-act="close" title="Close (Esc)">' + ICONS.close + '</button>' +
      '</div>' +
      '<div class="ask-settings">' +
        '<p class="ask-note">The key is kept only in this browser (localStorage) and goes straight to the provider. Nothing passes through this site.</p>' +
        '<label>Provider <select class="ask-provider"></select></label>' +
        '<label>API key <input type="password" class="ask-key" placeholder="paste your key" autocomplete="off" spellcheck="false"></label>' +
        '<label>Base URL <input type="url" class="ask-base" spellcheck="false" placeholder="https://…"></label>' +
        '<label>Model <input type="text" class="ask-model" spellcheck="false"></label>' +
        '<div class="ask-actions">' +
          '<button type="button" class="ask-save">Save</button>' +
          '<a class="ask-keylink" target="_blank" rel="noopener">Get a key</a>' +
        '</div>' +
      '</div>' +
      '<div class="ask-quote"><span class="ask-quote-text"></span>' +
        '<button type="button" class="ask-icon" data-act="unquote" title="Remove the selection">&times;</button></div>' +
      '<div class="ask-msgs">' +
        '<div class="ask-empty">' +
          '<div class="ask-empty-title">Ask anything on this page</div>' +
          'Type below, or select a passage and hit <i>Ask about this</i>. Maths welcome.' +
          '<div class="ask-chips">' +
            '<button type="button" class="ask-chip">Explain this page in 5 bullets</button>' +
            '<button type="button" class="ask-chip">Quiz me on this topic</button>' +
            '<button type="button" class="ask-chip">Where do people lose points?</button>' +
          '</div>' +
        '</div>' +
      '</div>' +
      '<form class="ask-form">' +
        '<textarea class="ask-input" rows="1" placeholder="Ask about the topics on this page…"></textarea>' +
        '<button type="submit" class="ask-send" title="Send">' + ICONS.send + '</button>' +
      '</form>';

    document.body.appendChild(wrap);
    el = {
      panel: wrap,
      settings: wrap.querySelector(".ask-settings"),
      provider: wrap.querySelector(".ask-provider"),
      key: wrap.querySelector(".ask-key"),
      base: wrap.querySelector(".ask-base"),
      model: wrap.querySelector(".ask-model"),
      keylink: wrap.querySelector(".ask-keylink"),
      quote: wrap.querySelector(".ask-quote"),
      quoteText: wrap.querySelector(".ask-quote-text"),
      msgs: wrap.querySelector(".ask-msgs"),
      form: wrap.querySelector(".ask-form"),
      input: wrap.querySelector(".ask-input"),
      send: wrap.querySelector(".ask-send"),
    };

    Object.keys(PROVIDERS).forEach((id) => {
      const o = document.createElement("option");
      o.value = id;
      o.textContent = PROVIDERS[id].name;
      el.provider.appendChild(o);
    });

    wrap.addEventListener("click", (e) => {
      const actEl = e.target.closest && e.target.closest("[data-act]");
      const act = actEl && actEl.getAttribute("data-act");
      if (act === "close") toggle(false);
      if (act === "settings") el.settings.classList.toggle("open");
      if (act === "unquote") setSelection("");
      const chip = e.target.closest && e.target.closest(".ask-chip");
      if (chip) askNow(chip.textContent);
    });
    el.provider.addEventListener("change", () => {
      loadProviderFields(el.provider.value); // show that provider's saved values
    });
    wrap.querySelector(".ask-save").addEventListener("click", saveSettings);

    el.form.addEventListener("submit", (e) => { e.preventDefault(); send(); });
    el.input.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
    });
    el.input.addEventListener("input", () => {
      el.input.style.height = "auto";
      el.input.style.height = Math.min(el.input.scrollHeight, 140) + "px";
    });

    loadProviderFields(state.provider);
  }

  function loadProviderFields(id) {
    const p = PROVIDERS[id] || PROVIDERS.gemini;
    el.provider.value = id;
    el.key.value = id === state.provider ? state.key : "";
    el.model.value = id === state.provider ? state.model : "";
    el.base.value = state.bases[id] || "";
    el.model.placeholder = p.defaultModel;
    el.key.placeholder = p.keyHint;
    el.base.placeholder = p.baseHint;
    el.keylink.href = p.keyUrl;
  }

  function saveSettings() {
    state.provider = el.provider.value;
    state.key = el.key.value.trim();
    state.model = el.model.value.trim();
    const base = el.base.value.trim();
    if (base) state.bases[state.provider] = base;
    else delete state.bases[state.provider];
    localStorage.setItem(LS.provider, state.provider);
    localStorage.setItem(LS.key, state.key);
    localStorage.setItem(LS.model, state.model);
    localStorage.setItem(LS.bases, JSON.stringify(state.bases));
    el.settings.classList.remove("open");
    if (state.key) {
      addMessage("assistant", "Saved. Ask me anything about the material on this page — or select a passage and hit *Ask about this*.");
    }
    updateButton();
  }

  function addMessage(role, text, quote) {
    const isThinking = role.indexOf("thinking") > -1;
    const empty = el.msgs.querySelector(".ask-empty");
    if (empty && !isThinking) empty.remove();
    const div = document.createElement("div");
    div.className = "ask-msg " + role.replace(" thinking", "") + (isThinking ? " thinking" : "");
    if (role.indexOf("user") === 0) {
      if (quote) {
        const q = document.createElement("div");
        q.className = "ask-msg-quote";
        q.textContent = quote.length > 180 ? quote.slice(0, 180) + "…" : quote;
        div.appendChild(q);
      }
      div.appendChild(document.createTextNode(text));
    } else {
      div.innerHTML = renderMarkdown(text);
      renderMath(div);
    }
    el.msgs.appendChild(div);
    el.msgs.scrollTop = el.msgs.scrollHeight;
    return div;
  }

  function toggle(force) {
    build();
    state.open = typeof force === "boolean" ? force : !state.open;
    el.panel.classList.toggle("open", state.open);
    const launcher = document.getElementById("ask-toggle");
    if (launcher) launcher.classList.toggle("hidden", state.open); // never overlap the panel
    if (state.open) {
      hideSelectionBtn();
      if (!state.key) el.settings.classList.add("open");
      el.input.focus();
      el.msgs.scrollTop = el.msgs.scrollHeight;
    }
  }

  function updateButton() {
    const b = document.getElementById("ask-toggle");
    if (b) b.classList.toggle("has-key", !!state.key);
  }

  function ensureButton() {
    if (document.getElementById("ask-toggle")) return;
    const b = document.createElement("button");
    b.id = "ask-toggle";
    b.type = "button";
    b.title = "Ask about the material on this page (bring your own API key)";
    b.innerHTML = ICONS.chat + '<span class="dot"></span><span class="label">Ask</span>';
    b.addEventListener("click", () => toggle());
    document.body.appendChild(b);
    updateButton();
  }

  /* ---------- API call ---------- */

  function askNow(text) {
    el.input.value = text;
    send();
  }

  async function send() {
    const text = el.input.value.trim();
    if (!text || state.busy) return;

    const p = PROVIDERS[state.provider] || PROVIDERS.gemini;
    const base = (state.bases[state.provider] || p.defaultBase).replace(/\/+$/, "");
    const customBase = base !== p.defaultBase.replace(/\/+$/, "");
    if (!state.key && !customBase) {
      toggle(true);
      el.settings.classList.add("open");
      el.key.focus();
      addMessage("assistant", "First add your API key (top-right gear). It stays in your browser.");
      return;
    }

    const quote = state.selection;
    const apiText = quote
      ? 'Selected passage:\n"""' + quote + '"""\n\nQuestion: ' + text
      : text;

    el.input.value = "";
    el.input.style.height = "auto";
    addMessage("user", text, quote);
    state.history.push({ role: "user", text: apiText });
    if (state.history.length > MAX_TURNS) state.history = state.history.slice(-MAX_TURNS);
    setSelection("");

    state.busy = true;
    el.send.disabled = true;
    const thinking = addMessage("assistant thinking", "Thinking…");

    const model = state.model || p.defaultModel;
    const req = p.build(base, state.key, model, systemPrompt(), state.history);

    try {
      const res = await fetch(req.url, {
        method: "POST",
        headers: req.headers,
        body: JSON.stringify(req.body),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) {
        const detail = (data.error && (data.error.message || data.error.status)) || res.status + " " + res.statusText;
        throw new Error(detail);
      }
      const answer = req.read(data) || "(empty answer)";
      thinking.remove();
      state.history.push({ role: "assistant", text: answer });
      addMessage("assistant", answer);
    } catch (err) {
      thinking.remove();
      addMessage(
        "assistant",
        "**Request failed:** " + String(err.message || err) + "\n\n" +
        "Check the key, base URL and model in the gear menu, and that your provider allows browser calls."
      );
    } finally {
      state.busy = false;
      el.send.disabled = false;
      el.input.focus();
    }
  }

  /* ---------- init ---------- */

  document$.subscribe(() => {
    build();
    ensureButton();
    if (!window.getSelection) return; // no selection API
    let t = null;
    const queue = () => {
      clearTimeout(t);
      t = setTimeout(showSelectionBtn, 120);
    };
    document.addEventListener("mouseup", queue);
    document.addEventListener("touchend", queue);
    document.addEventListener("keyup", (e) => { if (e.shiftKey || e.key.indexOf("Arrow") === 0) queue(); });
    document.addEventListener("selectionchange", queue);
    document.addEventListener("mousedown", (e) => {
      if (selBtn && e.target === selBtn) return;
      hideSelectionBtn();
    });
    window.addEventListener("scroll", hideSelectionBtn, true);
    window.addEventListener("resize", hideSelectionBtn);
    document.addEventListener("keydown", (e) => {
      if (e.key !== "Escape") return;
      hideSelectionBtn();
      if (state.open) toggle(false);
    });
  });
})();
