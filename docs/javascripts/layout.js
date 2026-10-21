// Minimal reading layout: both sidebars start collapsed; two header buttons toggle them.
(function () {
  "use strict";
  if (window.__sspLayoutLoaded) return;
  window.__sspLayoutLoaded = true;

  const root = document.documentElement;
  const KEYS = { nav: "ssp-show-nav", toc: "ssp-show-toc" };
  const ICONS = {
    nav: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h10M4 18h16"/></svg>',
    toc: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/></svg>',
  };
  const TITLES = { nav: "Chapters", toc: "On this page" };

  const on = (k) => localStorage.getItem(KEYS[k]) === "1";

  function apply() {
    root.classList.toggle("show-nav", on("nav"));
    root.classList.toggle("show-toc", on("toc"));
    document.querySelectorAll(".layout-btn").forEach((b) => b.classList.toggle("active", on(b.dataset.k)));
  }

  function ensureButtons() {
    const inner = document.querySelector(".md-header__inner");
    if (!inner || inner.querySelector(".layout-btns")) return;
    const wrap = document.createElement("div");
    wrap.className = "layout-btns";
    ["nav", "toc"].forEach((k) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "layout-btn";
      b.dataset.k = k;
      b.title = TITLES[k];
      b.setAttribute("aria-label", TITLES[k]);
      b.innerHTML = ICONS[k];
      b.addEventListener("click", () => {
        localStorage.setItem(KEYS[k], on(k) ? "0" : "1");
        apply();
      });
      wrap.appendChild(b);
    });
    const search = inner.querySelector(".md-search");
    inner.insertBefore(wrap, search || null);
    apply();
  }

  function boot() { ensureButtons(); apply(); }
  boot();
  if (typeof document$ !== "undefined" && document$ && document$.subscribe) document$.subscribe(boot);
})();
