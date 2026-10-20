// Ask-the-guide: chat panel that answers questions about the current page using
// the reader's own LLM API key (kept only in localStorage). Selecting text on the
// page pops up "Ask about this" and the passage becomes the visible context.
(function () {
  "use strict";
  if (window.__sspAskLoaded) return; // instant navigation may re-run scripts
  window.__sspAskLoaded = true;

  /* ---------------- config ---------------- */

  const LS = {
    provider: "ssp-ask-provider",
    key: "ssp-ask-key",
    model: "ssp-ask-model",
    bases: "ssp-ask-bases",
  };

  const MAX_CONTEXT = 14000;
  const MAX_TURNS = 12;
  const MAX_SELECTION = 6000;

  const LEGACY_MODELS = {
    "gpt-4o-mini": "gpt-5.6-terra",
    "gpt-4o": "gpt-5.6-terra",
    "gemini-2.5-flash": "gemini-3.8-flash",
    "gemini-2.0-flash": "gemini-3.8-flash",
    "openai/gpt-4o-mini": "google/gemini-3.8-flash",
  };

  function chatHeaders(key) {
    const h = { "Content-Type": "application/json" };
    if (key) h.Authorization = "Bearer " + key;
    return h;
  }

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
        body: {
          model: model,
          messages: [{ role: "system", content: system }].concat(
            messages.map((m) => ({ role: m.role, content: m.text }))
          ),
        },
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
        body: {
          model: model,
          messages: [{ role: "system", content: system }].concat(
            messages.map((m) => ({ role: m.role, content: m.text }))
          ),
        },
        read: (d) => d.choices[0].message.content,
      }),
    },
  };

  const ICONS = {
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    settings: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h9M19 7h1M4 17h3M13 17h7"/><circle cx="16" cy="7" r="2.3"/><circle cx="10" cy="17" r="2.3"/></svg>',
    send: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V6M6 12l6-6 6 6"/></svg>',
    chat: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12a7.5 7.5 0 0 1-7.5 7.5H8l-4 2.5V12A7.5 7.5 0 0 1 11.5 4.5h1A7.5 7.5 0 0 1 20 12z"/></svg>',
    quote: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 7h4v4a5.5 5.5 0 0 1-4 5v-2.2c1.2-.5 1.9-1.3 2-2.3H7V7zm8 0h4v4a5.5 5.5 0 0 1-4 5v-2.2c1.2-.5 1.9-1.3 2-2.3h-2V7z"/></svg>',
  };

  /* ---------------- state ---------------- */

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
    selection: "",
    history: [],
    busy: false,
    open: false,
  };
  if (LEGACY_MODELS[state.model]) {
    state.model = LEGACY_MODELS[state.model];
    localStorage.setItem(LS.model, state.model);
  }

  /* ---------------- markdown + math ---------------- */

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
        html += "<pre><code>" + escapeHtml(chunk.replace(/^[a-zA-Z0-9+#-]*\n/, "")) + "</code></pre>";
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
          const tag = ordered ? "ol" : "ul";
          html += "<" + tag + ">" +
            lines.map((l) => "<li>" + inline(escapeHtml(l.replace(/^\s*([-*]|\d+\.)\s+/, ""))) + "</li>").join("") +
            "</" + tag + ">";
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

  /* ---------------- page context ---------------- */

  function pageTitle() {
    const h = document.querySelector(".md-content__inner h1");
    return (h && h.textContent.trim()) || document.title;
  }

  function pageContext() {
    const main = document.querySelector(".md-content__inner");
    if (!main) return "";
    const clone = main.cloneNode(true);
    clone.querySelectorAll("script, style, .noprint, #ask-panel, .md-content__button").forEach((n) => n.remove());
    clone.querySelectorAll(".katex").forEach((katex) => {
      const ann = katex.querySelector('annotation[encoding="application/x-tex"]');
      const tex = ann ? ann.textContent.trim() : katex.textContent;
      katex.replaceWith(document.createTextNode(" $" + tex + "$ "));
    });
    const text = clone.textContent.replace(/[ \t\u00a0]+/g, " ").replace(/\n{3,}/g, "\n\n").trim();
    return ("Page: " + pageTitle() + "\n\n" + text).slice(0, MAX_CONTEXT);
  }

  function systemPrompt() {
    return (
      "You are a tutor for 5CTA0 Statistical Signal Processing (TU/e). " +
      "The student is revising for the exam and asks about the material in this guide. " +
      "Answer from the PAGE CONTENT below when the question is about the guide; " +
      "if it goes beyond it, say so and answer from general knowledge. " +
      "When a message starts with 'Selected passage', that is the exact text the student highlighted: " +
      "treat it as the immediate context and focus your answer on it. " +
      "Be concise and exam-focused: short derivation steps, state the formula before using it, " +
      "point out the mistakes the exams punish. " +
      "Write maths in LaTeX between $...$ (inline) or $$...$$ (display); never use MathML. " +
      "Reply in the same language the student writes in.\n\n--- PAGE CONTENT ---\n" +
      pageContext()
    );
  }

  /* ---------------- UI ---------------- */

  const ui = {};
  let chip = null;

  function ensureLauncher() {
    let b = document.getElementById("ask-toggle");
    if (b) return b;
    b = document.createElement("button");
    b.id = "ask-toggle";
    b.type = "button";
    b.title = "Ask about the material on this page";
    b.innerHTML = ICONS.chat + '<span class="dot"></span><span class="label">Ask</span>';
    b.addEventListener("click", () => open()); // always open, never toggles
    document.body.appendChild(b);
    return b;
  }

  function buildPanel() {
    const old = document.getElementById("ask-panel");
    if (old) old.remove();

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
        '<p class="ask-note">The key is kept only in this browser and goes straight to the provider. Nothing passes through this site.</p>' +
        '<label>Provider <select class="ask-provider"></select></label>' +
        '<label>API key <input type="password" class="ask-key" placeholder="paste your key" autocomplete="off" spellcheck="false"></label>' +
        '<label>Base URL <input type="url" class="ask-base" spellcheck="false" placeholder="https://"></label>' +
        '<label>Model <input type="text" class="ask-model" spellcheck="false"></label>' +
        '<div class="ask-actions">' +
          '<button type="button" class="ask-save">Save</button>' +
          '<a class="ask-keylink" target="_blank" rel="noopener">Get a key</a>' +
        '</div>' +
      '</div>' +
      '<div class="ask-context">' +
        '<div class="ask-context-head">' +
          '<span class="ask-context-label">Context</span>' +
          '<button type="button" class="ask-icon" data-act="clear-ctx" title="Use the whole page instead">' + ICONS.close + '</button>' +
        '</div>' +
        '<div class="ask-context-text"></div>' +
      '</div>' +
      '<div class="ask-msgs">' +
        '<div class="ask-empty">' +
          '<div class="ask-empty-title">Ask anything on this page</div>' +
          'Select a passage and hit <i>Ask about this</i>, or type below. Maths welcome.' +
          '<div class="ask-chips">' +
            '<button type="button" class="ask-chip">Explain this page in 5 bullets</button>' +
            '<button type="button" class="ask-chip">Quiz me on this topic</button>' +
            '<button type="button" class="ask-chip">Where do people lose points?</button>' +
          '</div>' +
        '</div>' +
      '</div>' +
      '<form class="ask-form">' +
        '<textarea class="ask-input" rows="1" placeholder="Ask about the topics on this page"></textarea>' +
        '<button type="submit" class="ask-send" title="Send">' + ICONS.send + '</button>' +
      '</form>';

    document.body.appendChild(wrap);

    ui.panel = wrap;
    ui.settings = wrap.querySelector(".ask-settings");
    ui.provider = wrap.querySelector(".ask-provider");
    ui.key = wrap.querySelector(".ask-key");
    ui.base = wrap.querySelector(".ask-base");
    ui.model = wrap.querySelector(".ask-model");
    ui.keylink = wrap.querySelector(".ask-keylink");
    ui.ctxLabel = wrap.querySelector(".ask-context-label");
    ui.ctxText = wrap.querySelector(".ask-context-text");
    ui.ctxClear = wrap.querySelector('[data-act="clear-ctx"]');
    ui.msgs = wrap.querySelector(".ask-msgs");
    ui.input = wrap.querySelector(".ask-input");
    ui.send = wrap.querySelector(".ask-send");

    Object.keys(PROVIDERS).forEach((id) => {
      const o = document.createElement("option");
      o.value = id;
      o.textContent = PROVIDERS[id].name;
      ui.provider.appendChild(o);
    });

    // delegated clicks (closest() so clicks on inner <svg> work too)
    wrap.addEventListener("click", (e) => {
      const hit = e.target.closest ? e.target.closest("[data-act], .ask-chip") : null;
      if (!hit) return;
      const act = hit.getAttribute("data-act");
      if (hit.classList.contains("ask-chip")) {
        ui.input.value = hit.textContent.trim();
        send();
        return;
      }
      if (act === "close") close();
      else if (act === "settings") ui.settings.classList.toggle("open");
      else if (act === "clear-ctx") setSelection("");
    });

    ui.provider.addEventListener("change", () => loadProviderFields(ui.provider.value));
    wrap.querySelector(".ask-save").addEventListener("click", saveSettings);

    wrap.querySelector(".ask-form").addEventListener("submit", (e) => {
      e.preventDefault();
      send();
    });
    ui.input.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        send();
      }
    });
    ui.input.addEventListener("input", () => {
      ui.input.style.height = "auto";
      ui.input.style.height = Math.min(ui.input.scrollHeight, 150) + "px";
    });

    loadProviderFields(state.provider);
    updateContextCard();
  }

  function loadProviderFields(id) {
    const p = PROVIDERS[id] || PROVIDERS.gemini;
    ui.provider.value = id;
    ui.key.value = id === state.provider ? state.key : "";
    ui.model.value = id === state.provider ? state.model : "";
    ui.base.value = state.bases[id] || "";
    ui.model.placeholder = p.defaultModel;
    ui.key.placeholder = p.keyHint;
    ui.base.placeholder = p.baseHint;
    ui.keylink.href = p.keyUrl;
  }

  function saveSettings() {
    state.provider = ui.provider.value;
    state.key = ui.key.value.trim();
    state.model = ui.model.value.trim();
    const base = ui.base.value.trim();
    if (base) state.bases[state.provider] = base;
    else delete state.bases[state.provider];
    localStorage.setItem(LS.provider, state.provider);
    localStorage.setItem(LS.key, state.key);
    localStorage.setItem(LS.model, state.model);
    localStorage.setItem(LS.bases, JSON.stringify(state.bases));
    ui.settings.classList.remove("open");
    updateLauncher();
    if (state.key) {
      addMessage("assistant", "Saved. Ask anything about this page — or select a passage and hit *Ask about this*.");
    }
  }

  /* ---------------- context card ---------------- */

  function setSelection(text) {
    state.selection = String(text || "").trim().slice(0, MAX_SELECTION);
    updateContextCard();
  }

  function updateContextCard() {
    if (!ui.ctxText) return;
    const sel = state.selection;
    ui.ctxLabel.textContent = sel ? "Selected passage" : "Current page";
    ui.ctxText.textContent = sel || pageTitle();
    ui.ctxClear.style.display = sel ? "" : "none";
    ui.ctxText.classList.toggle("selection", !!sel);
    ui.input.placeholder = sel ? "Ask about the selected passage" : "Ask about the topics on this page";
  }

  /* ---------------- messages ---------------- */

  function addMessage(role, text, quote) {
    const isThinking = role.indexOf("thinking") > -1;
    const empty = ui.msgs.querySelector(".ask-empty");
    if (empty && !isThinking) empty.remove();

    const div = document.createElement("div");
    div.className = "ask-msg " + role.replace(" thinking", "") + (isThinking ? " thinking" : "");
    if (role.indexOf("user") === 0) {
      if (quote) {
        const q = document.createElement("div");
        q.className = "ask-msg-quote";
        q.textContent = quote.length > 220 ? quote.slice(0, 220) + "…" : quote;
        div.appendChild(q);
      }
      div.appendChild(document.createTextNode(text));
    } else {
      div.innerHTML = renderMarkdown(text);
      renderMath(div);
    }
    ui.msgs.appendChild(div);
    ui.msgs.scrollTop = ui.msgs.scrollHeight;
    return div;
  }

  /* ---------------- open / close ---------------- */

  function open(opts) {
    ensureLauncher();
    if (!document.getElementById("ask-panel")) buildPanel();
    state.open = true;
    ui.panel.classList.add("open");
    updateLauncher();
    if (!state.key) ui.settings.classList.add("open");
    if (opts && opts.selection !== undefined) setSelection(opts.selection);
    else updateContextCard();
    hideChip();
    setTimeout(() => ui.input.focus(), 30);
  }

  function close() {
    state.open = false;
    if (ui.panel) ui.panel.classList.remove("open");
    updateLauncher();
    hideChip();
  }

  function updateLauncher() {
    const b = document.getElementById("ask-toggle");
    if (!b) return;
    b.classList.toggle("hidden", state.open); // never overlap the panel
    b.classList.toggle("has-key", !!state.key);
  }

  /* ---------------- selection chip ---------------- */

  function hideChip() {
    if (chip) chip.style.display = "none";
  }

  function ensureChip() {
    if (chip) return chip;
    chip = document.createElement("button");
    chip.id = "ask-select-btn";
    chip.type = "button";
    chip.title = "Ask about the selected text";
    chip.innerHTML = ICONS.quote + "<span>Ask about this</span>";
    // capture-phase pointerdown first: never hide when the press is ON the chip
    chip.addEventListener("pointerdown", (e) => e.preventDefault());
    chip.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      const text = chip.dataset.text || "";
      hideChip();
      open({ selection: text });
    });
    document.body.appendChild(chip);
    return chip;
  }

  function showChip() {
    const sel = window.getSelection ? window.getSelection() : null;
    const text = sel ? String(sel).replace(/\s+/g, " ").trim() : "";
    const content = document.querySelector(".md-content__inner");
    const inside = (n) => n && content && content.contains(n.nodeType === 1 ? n : n.parentNode);
    if (!sel || sel.isCollapsed || text.length < 3 || text.length > MAX_SELECTION ||
        !inside(sel.anchorNode) || !inside(sel.focusNode) || state.open) {
      hideChip();
      return;
    }
    const range = sel.getRangeAt(0);
    const rects = range.getClientRects();
    const r = rects.length ? rects[rects.length - 1] : range.getBoundingClientRect();
    if (!r || (!r.top && !r.left)) {
      hideChip();
      return;
    }
    const btn = ensureChip();
    btn.dataset.text = text;
    btn.style.display = "flex";
    const w = btn.offsetWidth || 120;
    const x = Math.min(Math.max(8, r.left + r.width / 2 - w / 2), window.innerWidth - w - 8);
    const above = r.top > 56;
    btn.style.left = x + "px";
    btn.style.top = (above ? r.top - 42 : Math.min(r.bottom + 10, window.innerHeight - 56)) + "px";
    btn.classList.toggle("below", !above);
  }

  /* ---------------- API call ---------------- */

  async function send() {
    const text = ui.input.value.trim();
    if (!text || state.busy) return;

    const p = PROVIDERS[state.provider] || PROVIDERS.gemini;
    const base = (state.bases[state.provider] || p.defaultBase).replace(/\/+$/, "");
    const customBase = base !== p.defaultBase.replace(/\/+$/, "");
    if (!state.key && !customBase) {
      ui.settings.classList.add("open");
      ui.key.focus();
      addMessage("assistant", "First add your API key (gear button, top right). It stays in your browser.");
      return;
    }

    const quote = state.selection;
    const apiText = quote
      ? 'Selected passage:\n"""' + quote + '"""\n\nQuestion: ' + text
      : text;

    ui.input.value = "";
    ui.input.style.height = "auto";
    addMessage("user", text, quote);
    state.history.push({ role: "user", text: apiText });
    if (state.history.length > MAX_TURNS) state.history = state.history.slice(-MAX_TURNS);
    setSelection("");

    state.busy = true;
    ui.send.disabled = true;
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
        const detail = (data.error && (data.error.message || data.error.status)) ||
          res.status + " " + res.statusText;
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
      ui.send.disabled = false;
      ui.input.focus();
    }
  }

  /* ---------------- boot ---------------- */

  let listenersBound = false;

  function bindGlobalListeners() {
    if (listenersBound) return;
    listenersBound = true;

    // hide the chip when pressing anywhere that is not the chip itself
    document.addEventListener("pointerdown", (e) => {
      if (chip && chip.style.display !== "none" && chip.contains(e.target)) return;
      if (e.target.closest && e.target.closest("#ask-panel")) return;
      hideChip();
    }, true);

    let t = null;
    const queue = () => {
      clearTimeout(t);
      t = setTimeout(showChip, 120);
    };
    document.addEventListener("mouseup", queue);
    document.addEventListener("touchend", queue);
    document.addEventListener("keyup", (e) => {
      if (e.shiftKey || e.key.indexOf("Arrow") === 0) queue();
    });
    document.addEventListener("selectionchange", queue);
    window.addEventListener("scroll", hideChip, true);
    window.addEventListener("resize", hideChip);

    document.addEventListener("keydown", (e) => {
      if (e.key !== "Escape") return;
      if (chip && chip.style.display !== "none") {
        hideChip();
        return;
      }
      if (state.open) close();
    });
  }

  function boot() {
    try {
      ensureLauncher();
      updateLauncher();
      bindGlobalListeners();
      if (state.open) open(); // rebuild the panel after an instant navigation
      else updateContextCard();
    } catch (e) {
      if (window.console && console.warn) console.warn("ask-the-guide failed to start", e);
    }
  }

  // Run immediately (this script sits at the end of <body>, so the DOM is ready).
  // document$ is only used to refresh after instant navigations — never relied on,
  // because Material's observable can already have emitted before we subscribe.
  boot();
  if (typeof document$ !== "undefined" && document$ && typeof document$.subscribe === "function") {
    try {
      document$.subscribe(() => boot());
    } catch (e) { /* instant navigation refresh is optional */ }
  }
})();
