document$.subscribe(({ body }) => {
  renderMathInElement(body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true }
    ],
    ignoredClasses: ["md-search", "md-header"],
    throwOnError: false
  })
})

// Copying a selection that includes formulas puts their LaTeX source on the clipboard.
document.addEventListener("copy", (e) => {
  const sel = window.getSelection();
  if (!sel || sel.isCollapsed || !sel.rangeCount) return;
  const frag = sel.getRangeAt(0).cloneContents();
  if (!frag.querySelector(".katex")) return;
  frag.querySelectorAll(".katex").forEach((k) => {
    const tex = k.querySelector('annotation[encoding="application/x-tex"]');
    const display = k.parentElement && k.parentElement.classList.contains("katex-display");
    const src = tex ? tex.textContent : "";
    k.replaceWith(document.createTextNode(display ? "$$" + src + "$$" : "$" + src + "$"));
  });
  const box = document.createElement("div");
  box.appendChild(frag);
  e.clipboardData.setData("text/plain", box.textContent);
  e.preventDefault();
});

// Definition tooltips (abbr) are plain text built by the theme at hover time: typeset the math inside them.
new MutationObserver(() => {
  document.querySelectorAll(".md-tooltip2__inner").forEach((el) => {
    if (!el.textContent.includes("$")) return;
    renderMathInElement(el, {
      delimiters: [{ left: "$$", right: "$$", display: false }, { left: "$", right: "$", display: false }],
      throwOnError: false
    });
  });
}).observe(document.body, { childList: true, subtree: true, characterData: true });
