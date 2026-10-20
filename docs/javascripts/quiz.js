// Quiz mode: hide every solution so you can try the question first.
(function () {
  const KEY = "ssp-quiz-mode";
  const isQuiz = () => localStorage.getItem(KEY) === "1";

  function apply(root) {
    const quiz = isQuiz();
    root.querySelectorAll("details.solution").forEach((d) => { d.open = !quiz; });
    const btn = document.getElementById("quiz-toggle");
    if (btn) {
      btn.classList.toggle("on", quiz);
      btn.querySelector(".label").textContent = quiz ? "Quiz ON" : "Quiz OFF";
    }
  }

  function ensureButton() {
    if (document.getElementById("quiz-toggle")) return;
    const b = document.createElement("button");
    b.id = "quiz-toggle";
    b.type = "button";
    b.title = "Hide/show all solutions on the page";
    b.innerHTML = '<span class="dot"></span><span class="label"></span>';
    b.addEventListener("click", () => {
      localStorage.setItem(KEY, isQuiz() ? "0" : "1");
      apply(document);
    });
    document.body.appendChild(b);
  }

  document$.subscribe(() => {
    const hasSolutions = document.querySelector("details.solution");
    ensureButton();
    document.getElementById("quiz-toggle").style.display = hasSolutions ? "" : "none";
    apply(document);
  });
  // Also run immediately: document$ may have emitted before this script loaded.
  ensureButton();
  const has = document.querySelector("details.solution");
  document.getElementById("quiz-toggle").style.display = has ? "" : "none";
  apply(document);
})();
