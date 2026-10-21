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
    back: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
    trash: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 12h10l1-12M9 7V4h6v3"/></svg>',
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
    view: "chat",
  };
  if (LEGACY_MODELS[state.model]) {
    state.model = LEGACY_MODELS[state.model];
    localStorage.setItem(LS.model, state.model);
  }

  /* ---------------- markdown + math ---------------- */

  function escapeHtml(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  // math spans are lifted out before inline formatting so `*` inside them survives
  function withMath(s, fn) {
    const saved = [];
    const masked = s.replace(/\$\$[\s\S]+?\$\$|\$[^$\n]+?\$/g, (m) => {
      saved.push(m);
      return "\u0001" + (saved.length - 1) + "\u0001";
    });
    return fn(masked).replace(/\u0001(\d+)\u0001/g, (_, i) => saved[+i]);
  }

  function inline(s) {
    return withMath(s, inlineFmt);
  }

  function inlineFmt(s) {
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
  let lastFocus = null;
  const isTouch = () => window.matchMedia && window.matchMedia("(pointer: coarse)").matches;

  function el(tag, cls, html) {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html !== undefined) n.innerHTML = html;
    return n;
  }

  function ensureLauncher() {
    let b = document.getElementById("ask-toggle");
    if (b) return b;
    b = el("button", "", ICONS.chat + '<span class="dot"></span><span class="label">Ask</span>');
    b.id = "ask-toggle";
    b.type = "button";
    b.setAttribute("aria-label", "Ask about this page");
    b.addEventListener("click", () => open());
    document.body.appendChild(b);
    return b;
  }

  function buildPanel() {
    ["ask-panel", "ask-backdrop"].forEach((id) => {
      const old = document.getElementById(id);
      if (old) old.remove();
    });

    const backdrop = el("div");
    backdrop.id = "ask-backdrop";
    backdrop.addEventListener("click", close);

    const wrap = el("aside");
    wrap.id = "ask-panel";
    wrap.setAttribute("role", "dialog");
    wrap.setAttribute("aria-label", "Ask the guide");
    wrap.innerHTML =
      '<div class="ask-grab"></div>' +
      '<header class="ask-head">' +
        '<button type="button" class="ask-btn ask-back" data-act="back" aria-label="Back to chat">' + ICONS.back + '</button>' +
        '<div class="ask-head-text">' +
          '<span class="ask-title">Ask the guide</span>' +
          '<span class="ask-sub"></span>' +
        '</div>' +
        '<button type="button" class="ask-btn ask-reset" data-act="reset" aria-label="New chat" title="New chat">' + ICONS.trash + '</button>' +
        '<button type="button" class="ask-btn ask-gear" data-act="settings" aria-label="API key settings" title="API key settings">' + ICONS.settings + '</button>' +
        '<button type="button" class="ask-btn ask-close" data-act="close" aria-label="Close" title="Close (Esc)">' + ICONS.close + '</button>' +
      '</header>' +
      '<div class="ask-body">' +
        '<div class="ask-msgs"></div>' +
        '<form class="ask-settings" autocomplete="off">' +
          '<p class="ask-note">The key stays in this browser and goes straight to the provider. Nothing passes through this site.</p>' +
          '<label>Provider<select class="ask-provider"></select></label>' +
          '<label>API key<input type="password" class="ask-key" autocomplete="off" spellcheck="false"></label>' +
          '<label>Model<input type="text" class="ask-model" spellcheck="false"></label>' +
          '<label>Base URL (optional)<input type="url" class="ask-base" spellcheck="false"></label>' +
          '<div class="ask-actions">' +
            '<button type="submit" class="ask-save">Save</button>' +
            '<a class="ask-keylink" target="_blank" rel="noopener">Get a key</a>' +
          '</div>' +
        '</form>' +
      '</div>' +
      '<footer class="ask-foot">' +
        '<div class="ask-quote" hidden>' +
          '<div class="ask-quote-text"></div>' +
          '<button type="button" class="ask-quote-x" data-act="clear-ctx" aria-label="Remove quoted passage">' + ICONS.close + '</button>' +
        '</div>' +
        '<form class="ask-form">' +
          '<textarea class="ask-input" rows="1" enterkeyhint="send"></textarea>' +
          '<button type="submit" class="ask-send" aria-label="Send">' + ICONS.send + '</button>' +
        '</form>' +
      '</footer>';

    document.body.appendChild(backdrop);
    document.body.appendChild(wrap);

    ui.panel = wrap;
    ui.backdrop = backdrop;
    ui.sub = wrap.querySelector(".ask-sub");
    ui.body = wrap.querySelector(".ask-body");
    ui.msgs = wrap.querySelector(".ask-msgs");
    ui.settings = wrap.querySelector(".ask-settings");
    ui.provider = wrap.querySelector(".ask-provider");
    ui.key = wrap.querySelector(".ask-key");
    ui.model = wrap.querySelector(".ask-model");
    ui.base = wrap.querySelector(".ask-base");
    ui.keylink = wrap.querySelector(".ask-keylink");
    ui.quote = wrap.querySelector(".ask-quote");
    ui.quoteText = wrap.querySelector(".ask-quote-text");
    ui.input = wrap.querySelector(".ask-input");
    ui.send = wrap.querySelector(".ask-send");

    Object.keys(PROVIDERS).forEach((id) => {
      const o = el("option");
      o.value = id;
      o.textContent = PROVIDERS[id].name;
      ui.provider.appendChild(o);
    });

    wrap.addEventListener("click", (e) => {
      const hit = e.target.closest ? e.target.closest("[data-act], .ask-chip") : null;
      if (!hit) return;
      if (hit.classList.contains("ask-chip")) {
        ui.input.value = hit.textContent.trim();
        send();
        return;
      }
      const act = hit.getAttribute("data-act");
      if (act === "close") close();
      else if (act === "settings") setView(state.view === "settings" ? "chat" : "settings");
      else if (act === "back") setView("chat");
      else if (act === "reset") resetChat();
      else if (act === "clear-ctx") setSelection("");
    });

    ui.provider.addEventListener("change", () => loadProviderFields(ui.provider.value));
    ui.settings.addEventListener("submit", (e) => {
      e.preventDefault();
      saveSettings();
    });
    wrap.querySelector(".ask-form").addEventListener("submit", (e) => {
      e.preventDefault();
      send();
    });
    ui.input.addEventListener("keydown", (e) => {
      // Enter sends on desktop; on touch keyboards Enter stays a newline
      if (e.key === "Enter" && !e.shiftKey && !e.isComposing && !isTouch()) {
        e.preventDefault();
        send();
      }
    });
    ui.input.addEventListener("input", autosize);

    loadProviderFields(state.provider);
    renderEmpty();
    updateQuote();
    setView(state.key ? "chat" : "settings");
  }

  function autosize() {
    ui.input.style.height = "auto";
    ui.input.style.height = Math.min(ui.input.scrollHeight, 130) + "px";
  }

  function setView(v) {
    state.view = v;
    ui.panel.dataset.view = v;
    ui.sub.textContent = v === "settings" ? "Settings" : pageTitle();
    if (v === "chat") setTimeout(() => ui.input && ui.input.focus({ preventScroll: true }), 30);
    else ui.body.scrollTop = 0;
  }

  function renderEmpty() {
    ui.msgs.appendChild(el("div", "ask-empty",
      '<div class="ask-empty-title">Ask anything about this page</div>' +
      '<p>Highlight a passage and press <b>Ask about this</b>, or just type below.</p>' +
      '<div class="ask-chips">' +
        '<button type="button" class="ask-chip">Explain this page in 5 bullets</button>' +
        '<button type="button" class="ask-chip">Quiz me on this topic</button>' +
        '<button type="button" class="ask-chip">Where do people lose points?</button>' +
      '</div>'));
  }

  function resetChat() {
    if (state.busy) return;
    state.history = [];
    ui.msgs.textContent = "";
    renderEmpty();
    setSelection("");
    ui.input.focus({ preventScroll: true });
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
    updateLauncher();
    setView("chat");
  }

  /* ---------------- quoted passage ---------------- */

  function setSelection(text) {
    state.selection = String(text || "").trim().slice(0, MAX_SELECTION);
    updateQuote();
  }

  function updateQuote() {
    if (!ui.quote) return;
    ui.quote.hidden = !state.selection;
    ui.quoteText.textContent = state.selection;
    ui.input.placeholder = state.selection ? "Ask about the quoted passage" : "Ask about this page";
  }

  /* ---------------- messages ---------------- */

  function addMessage(role, text, quote) {
    const isThinking = role.indexOf("thinking") > -1;
    const empty = ui.msgs.querySelector(".ask-empty");
    if (empty && !isThinking) empty.remove();

    const div = el("div", "ask-msg " + role.replace(" thinking", "") + (isThinking ? " thinking" : ""));
    if (role.indexOf("user") === 0) {
      if (quote) {
        const q = el("div", "ask-msg-quote");
        q.textContent = quote.length > 220 ? quote.slice(0, 220) + "…" : quote;
        div.appendChild(q);
      }
      div.appendChild(document.createTextNode(text));
    } else {
      div.innerHTML = renderMarkdown(text);
      renderMath(div);
    }
    ui.msgs.appendChild(div);
    ui.body.scrollTop = ui.body.scrollHeight;
    return div;
  }

  /* ---------------- open / close ---------------- */

  function open(opts) {
    ensureLauncher();
    if (!document.getElementById("ask-panel")) buildPanel();
    if (!state.open) lastFocus = document.activeElement;
    state.open = true;
    document.documentElement.classList.add("ask-open");
    ui.panel.classList.add("open");
    ui.backdrop.classList.add("open");
    if (opts && opts.selection !== undefined) {
      setSelection(opts.selection);
      if (state.key) setView("chat");
    }
    updateLauncher();
    hideChip();
    if (state.view === "chat") setTimeout(() => ui.input.focus({ preventScroll: true }), 30);
  }

  function close() {
    state.open = false;
    document.documentElement.classList.remove("ask-open");
    if (ui.panel) ui.panel.classList.remove("open");
    if (ui.backdrop) ui.backdrop.classList.remove("open");
    updateLauncher();
    hideChip();
    if (lastFocus && lastFocus.focus && document.contains(lastFocus)) {
      try { lastFocus.focus({ preventScroll: true }); } catch (e) { /* ignore */ }
    }
  }

  function updateLauncher() {
    const b = document.getElementById("ask-toggle");
    if (!b) return;
    b.classList.toggle("hidden", state.open);
    b.classList.toggle("has-key", !!state.key);
  }

  /* ---------------- selection chip ---------------- */

  function hideChip() {
    if (chip) chip.style.display = "none";
  }

  function ensureChip() {
    if (chip) return chip;
    chip = el("button", "", ICONS.quote + "<span>Ask about this</span>");
    chip.id = "ask-select-btn";
    chip.type = "button";
    // keep the text selected while pressing the chip
    chip.addEventListener("pointerdown", (e) => e.preventDefault());
    chip.addEventListener("mousedown", (e) => e.preventDefault());
    chip.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      const text = chip.dataset.text || "";
      hideChip();
      const s = window.getSelection && window.getSelection();
      if (s && s.removeAllRanges) s.removeAllRanges();
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
    if (!sel || sel.isCollapsed || sel.rangeCount === 0 || text.length < 3 || text.length > MAX_SELECTION ||
        !inside(sel.anchorNode) || !inside(sel.focusNode)) {
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
    const w = btn.offsetWidth || 130;
    const x = Math.min(Math.max(8, r.left + r.width / 2 - w / 2), window.innerWidth - w - 8);
    // touch browsers draw their own menu above the selection, so go below there
    const above = !isTouch() && r.top > 56;
    const y = above ? r.top - 44 : Math.min(r.bottom + (isTouch() ? 44 : 10), window.innerHeight - 52);
    btn.style.left = x + "px";
    btn.style.top = y + "px";
  }

  /* ---------------- API call ---------------- */

  async function send() {
    const text = ui.input.value.trim();
    if (!text || state.busy) return;

    const p = PROVIDERS[state.provider] || PROVIDERS.gemini;
    const base = (state.bases[state.provider] || p.defaultBase).replace(/\/+$/, "");
    const customBase = base !== p.defaultBase.replace(/\/+$/, "");
    if (!state.key && !customBase) {
      setView("settings");
      ui.key.focus();
      return;
    }

    const quote = state.selection;
    const apiText = quote
      ? 'Selected passage:\n"""' + quote + '"""\n\nQuestion: ' + text
      : text;

    ui.input.value = "";
    autosize();
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
      state.history.pop(); // a failed question must not poison the next request
      addMessage(
        "assistant",
        "**Request failed:** " + String(err.message || err) + "\n\n" +
        "Check the key, base URL and model in settings, and that your provider allows browser calls."
      );
    } finally {
      state.busy = false;
      ui.send.disabled = false;
      if (state.open && state.view === "chat") ui.input.focus({ preventScroll: true });
    }
  }

  /* ---------------- boot ---------------- */

  let listenersBound = false;

  function bindGlobalListeners() {
    if (listenersBound) return;
    listenersBound = true;

    let t = null;
    const queue = (ms) => {
      clearTimeout(t);
      t = setTimeout(showChip, ms);
    };
    document.addEventListener("mouseup", () => queue(60));
    document.addEventListener("touchend", () => queue(350));
    document.addEventListener("keyup", (e) => {
      if (e.shiftKey || e.key.indexOf("Arrow") === 0) queue(120);
    });
    document.addEventListener("selectionchange", () => {
      const s = window.getSelection();
      if (!s || s.isCollapsed) hideChip();
      else if (isTouch()) queue(450);
    });
    window.addEventListener("scroll", hideChip, { capture: true, passive: true });
    window.addEventListener("resize", hideChip);

    document.addEventListener("keydown", (e) => {
      if (e.key !== "Escape") return;
      if (chip && chip.style.display !== "none") hideChip();
      else if (state.open) close();
    });
  }

  function boot() {
    try {
      ensureLauncher();
      bindGlobalListeners();
      if (state.open) open(); // rebuild the panel after an instant navigation
      else updateLauncher();
    } catch (e) {
      if (window.console && console.warn) console.warn("ask-the-guide failed to start", e);
    }
  }

  boot();
  if (typeof document$ !== "undefined" && document$ && typeof document$.subscribe === "function") {
    try {
      document$.subscribe(() => boot());
    } catch (e) { /* instant navigation refresh is optional */ }
  }
})();
