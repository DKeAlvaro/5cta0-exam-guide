// Zen mode: hides header, sidebars and footer; only the page content plus prev/next buttons.
// Prev/next come from the (hidden) Material footer links, so they follow the nav order.
(function () {
  "use strict";
  if (window.__sspZenLoaded) return;
  window.__sspZenLoaded = true;

  const KEY = "ssp-zen";
  const root = document.documentElement;
  let bar = null;
  let toggle = null;

  function isOn() { return root.classList.contains("zen"); }

  function set(on) {
    root.classList.toggle("zen", on);
    try { localStorage.setItem(KEY, on ? "1" : "0"); } catch (e) { /* ignore */ }
    if (toggle) toggle.textContent = on ? "Exit zen" : "Zen";
    if (on) window.scrollTo(0, 0);
  }

  function ensureUi() {
    if (!toggle) {
      toggle = document.createElement("button");
      toggle.id = "zen-toggle";
      toggle.type = "button";
      toggle.addEventListener("click", () => set(!isOn()));
      document.body.appendChild(toggle);
    }
    if (!bar) {
      bar = document.createElement("nav");
      bar.id = "zen-nav";
      bar.setAttribute("aria-label", "Zen navigation");
      bar.innerHTML = '<a class="zen-prev" hidden></a><a class="zen-next" hidden></a>';
      document.body.appendChild(bar);
    }
    toggle.textContent = isOn() ? "Exit zen" : "Zen";
  }

  function refreshLinks() {
    ensureUi();
    [["prev", ".md-footer__link--prev", "← "], ["next", ".md-footer__link--next", ""]].forEach((c) => {
      const a = bar.querySelector(".zen-" + c[0]);
      const src = document.querySelector(c[1]);
      if (!src) { a.hidden = true; return; }
      const t = src.querySelector(".md-ellipsis");
      const title = (t ? t.textContent : src.textContent).replace(/\s+/g, " ").trim()
        .replace(/^(Previous|Next)\s*/, "");
      a.href = src.getAttribute("href");
      a.textContent = c[0] === "prev" ? "← " + title : title + " →";
      a.hidden = false;
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOn() && !root.classList.contains("ask-open")) set(false);
  });

  function boot() {
    let saved = "0";
    try { saved = localStorage.getItem(KEY) || "0"; } catch (e) { /* ignore */ }
    if (!window.__zenInit) { window.__zenInit = true; root.classList.toggle("zen", saved === "1"); }
    refreshLinks();
  }

  boot();
  if (typeof document$ !== "undefined" && document$ && typeof document$.subscribe === "function") {
    document$.subscribe(() => refreshLinks());
  }
})();
