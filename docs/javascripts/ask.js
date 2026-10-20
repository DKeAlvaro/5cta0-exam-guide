// Ask-the-guide: a small chat panel that answers questions about the current
// page using the reader's own LLM API key (stored only in localStorage).
(function () {
  const LS = {
    provider: "ssp-ask-provider",
    key: "ssp-ask-key",
    model: "ssp-ask-model",
  };

  const MAX_CONTEXT = 14000; // chars of page text sent as context
  const MAX_TURNS = 12; // messages kept in the conversation

  const PROVIDERS = {
    openai: {
      name: "OpenAI",
      keyHint: "sk-...",
      keyUrl: "https://platform.openai.com/api-keys",
      defaultModel: "gpt-4o-mini",
      build: (key, model, system, messages) => ({
        url: "https://api.openai.com/v1/chat/completions",
        headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" },
        body: { model: model, messages: [{ role: "system", content: system }].concat(messages) },
        read: (d) => d.choices[0].message.content,
      }),
    },
    gemini: {
      name: "Google Gemini",
      keyHint: "AIza...",
      keyUrl: "https://aistudio.google.com/apikey",
      defaultModel: "gemini-2.5-flash",
      build: (key, model, system, messages) => ({
        url:
          "https://generativelanguage.googleapis.com/v1beta/models/" +
          encodeURIComponent(model) + ":generateContent?key=" + encodeURIComponent(key),
        headers: { "Content-Type": "application/json" },
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
      }),
    },
    openrouter: {
      name: "OpenRouter",
      keyHint: "sk-or-...",
      keyUrl: "https://openrouter.ai/keys",
      defaultModel: "openai/gpt-4o-mini",
      build: (key, model, system, messages) => ({
        url: "https://openrouter.ai/api/v1/chat/completions",
        headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" },
        body: { model: model, messages: [{ role: "system", content: system }].concat(messages) },
        read: (d) => d.choices[0].message.content,
      }),
    },
  };

  const state = {
    provider: localStorage.getItem(LS.provider) || "gemini",
    key: localStorage.getItem(LS.key) || "",
    model: localStorage.getItem(LS.model) || "",
    history: [], // {role: "user"|"assistant", text}
    busy: false,
    open: false,
  };

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

  /* ---------- UI ---------- */

  let el = {};

  function build() {
    if (document.getElementById("ask-panel")) return;
    const wrap = document.createElement("div");
    wrap.id = "ask-panel";
    wrap.innerHTML =
      '<div class="ask-head">' +
        '<span class="ask-title">Ask about this page</span>' +
        '<button type="button" class="ask-icon" data-act="settings" title="API key settings">&#9881;</button>' +
        '<button type="button" class="ask-icon" data-act="close" title="Close">&times;</button>' +
      '</div>' +
      '<div class="ask-settings">' +
        '<p class="ask-note">The key is stored only in this browser (localStorage) and is sent straight to the provider. Nothing passes through this site.</p>' +
        '<label>Provider <select class="ask-provider"></select></label>' +
        '<label>API key <input type="password" class="ask-key" placeholder="paste your key" autocomplete="off" spellcheck="false"></label>' +
        '<label>Model <input type="text" class="ask-model" spellcheck="false"></label>' +
        '<div class="ask-actions">' +
          '<button type="button" class="ask-save">Save</button>' +
          '<a class="ask-keylink" target="_blank" rel="noopener">Get a key</a>' +
        '</div>' +
      '</div>' +
      '<div class="ask-msgs"></div>' +
      '<form class="ask-form">' +
        '<textarea class="ask-input" rows="1" placeholder="Ask about the topics on this page…"></textarea>' +
        '<button type="submit" class="ask-send">Send</button>' +
      '</form>';

    document.body.appendChild(wrap);
    el = {
      panel: wrap,
      settings: wrap.querySelector(".ask-settings"),
      provider: wrap.querySelector(".ask-provider"),
      key: wrap.querySelector(".ask-key"),
      model: wrap.querySelector(".ask-model"),
      keylink: wrap.querySelector(".ask-keylink"),
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
      const act = e.target.getAttribute && e.target.getAttribute("data-act");
      if (act === "close") toggle(false);
      if (act === "settings") el.settings.classList.toggle("open");
    });
    el.provider.addEventListener("change", syncSettings);
    wrap.querySelector(".ask-save").addEventListener("click", saveSettings);

    el.form.addEventListener("submit", (e) => { e.preventDefault(); send(); });
    el.input.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
    });
    el.input.addEventListener("input", () => {
      el.input.style.height = "auto";
      el.input.style.height = Math.min(el.input.scrollHeight, 140) + "px";
    });

    syncSettings();
  }

  function syncSettings() {
    const p = PROVIDERS[el.provider.value] || PROVIDERS.gemini;
    el.model.placeholder = p.defaultModel;
    el.key.placeholder = p.keyHint;
    el.keylink.href = p.keyUrl;
  }

  function saveSettings() {
    state.provider = el.provider.value;
    state.key = el.key.value.trim();
    state.model = el.model.value.trim();
    localStorage.setItem(LS.provider, state.provider);
    localStorage.setItem(LS.key, state.key);
    localStorage.setItem(LS.model, state.model);
    el.settings.classList.remove("open");
    if (state.key) {
      addMessage("assistant", "Key saved. Ask me anything about the material on this page.");
    }
    updateButton();
  }

  function addMessage(role, text) {
    const div = document.createElement("div");
    div.className = "ask-msg " + role;
    if (role === "user") {
      div.textContent = text;
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
    if (state.open) {
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
    b.innerHTML = '<span class="dot"></span><span class="label">Ask</span>';
    b.addEventListener("click", () => toggle());
    document.body.appendChild(b);
    updateButton();
  }

  /* ---------- API call ---------- */

  async function send() {
    const text = el.input.value.trim();
    if (!text || state.busy) return;
    if (!state.key) {
      toggle(true);
      el.settings.classList.add("open");
      el.key.focus();
      addMessage("assistant", "First add your API key (top-right gear). It stays in your browser.");
      return;
    }

    el.input.value = "";
    el.input.style.height = "auto";
    addMessage("user", text);
    state.history.push({ role: "user", text: text });
    if (state.history.length > MAX_TURNS) state.history = state.history.slice(-MAX_TURNS);

    state.busy = true;
    el.send.disabled = true;
    const thinking = addMessage("assistant thinking", "Thinking…");

    const p = PROVIDERS[state.provider] || PROVIDERS.gemini;
    const model = state.model || p.defaultModel;
    const req = p.build(state.key, model, systemPrompt(), state.history);

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
        "Check the key and model in the gear menu, and that your provider allows browser calls."
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
  });
})();
