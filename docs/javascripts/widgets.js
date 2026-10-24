// Interactive figures for the exam course. Markup: <div class="widget" data-w="name" data-preset="..."></div>.
// Each widget draws an SVG with its own controls and plays once by itself the first time it scrolls into view.
// Also here: .stepper (worked solutions revealed one step at a time) and .tf (true/false cards from a table).
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const W = {};

  // ---------- helpers ----------
  function S(tag, a, parent) {
    const e = document.createElementNS(NS, tag);
    for (const k in a || {}) if (k === "text") e.textContent = a[k]; else e.setAttribute(k, a[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function H(tag, a, parent) {
    const e = document.createElement(tag);
    for (const k in a || {}) {
      if (k === "html") e.innerHTML = a[k];
      else if (k === "text") e.textContent = a[k];
      else e.setAttribute(k, a[k]);
    }
    if (parent) parent.appendChild(e);
    return e;
  }
  const lin = (d0, d1, r0, r1) => (v) => r0 + ((v - d0) / (d1 - d0)) * (r1 - r0);
  const grid = (a, b, n) => Array.from({ length: n }, (_, i) => a + ((b - a) * i) / (n - 1));
  const pathOf = (pts) => "M" + pts.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" L");
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  function fmt(v, d) {
    const s = (+v).toFixed(d === undefined ? 2 : d);
    const t = s.includes(".") ? s.replace(/0+$/, "").replace(/\.$/, "") : s;
    return t === "-0" ? "0" : t;
  }
  function tex(el, html) {
    el.innerHTML = html;
    if (window.renderMathInElement) {
      renderMathInElement(el, { delimiters: [{ left: "$", right: "$", display: false }], throwOnError: false });
    }
  }
  function tween(ms, frame, done) {
    let alive = true;
    const t0 = performance.now();
    const ease = (u) => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2);
    (function loop(t) {
      if (!alive) return;
      const u = Math.min(1, (t - t0) / ms);
      frame(ease(u));
      if (u < 1) requestAnimationFrame(loop);
      else if (done) done();
    })(t0);
    return () => { alive = false; };
  }
  function mulberry(seed) {
    return function () {
      seed |= 0; seed = (seed + 0x6d2b79f5) | 0;
      let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function erf(x) {
    const s = Math.sign(x), a = Math.abs(x), t = 1 / (1 + 0.3275911 * a);
    const y = 1 - ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-a * a);
    return s * y;
  }
  const Phi = (z) => 0.5 * (1 + erf(z / Math.SQRT2));
  const npdf = (z) => Math.exp(-z * z / 2) / Math.sqrt(2 * Math.PI);

  function shell(root, w, h) {
    root.innerHTML = "";
    const svg = S("svg", { viewBox: "0 0 " + w + " " + h, class: "w-svg" }, H("div", { class: "w-scroll" }, root));
    const cap = H("div", { class: "w-cap" }, root);
    const bar = H("div", { class: "w-bar" }, root);
    return { svg, cap, bar };
  }
  function btn(bar, label, fn, cls) {
    const b = H("button", { type: "button", class: "w-btn" + (cls ? " " + cls : ""), text: label }, bar);
    b.addEventListener("click", fn);
    return b;
  }
  function slider(bar, label, min, max, step, val, fn, show) {
    const wrap = H("label", { class: "w-sl" }, bar);
    const name = H("span", { class: "w-sl-name" }, wrap);
    tex(name, label);
    const inp = H("input", { type: "range", min: min, max: max, step: step, value: val }, wrap);
    const out = H("span", { class: "w-sl-val", text: show ? show(val) : fmt(val) }, wrap);
    const upd = () => { const v = +inp.value; out.textContent = show ? show(v) : fmt(v); fn(v); };
    inp.addEventListener("input", upd);
    return { inp, wrap, set(v) { inp.value = v; upd(); }, get: () => +inp.value, upd };
  }
  function tabs(bar, names, fn) {
    const box = H("span", { class: "w-tabs" }, bar);
    const bs = names.map((n, i) => btn(box, n, () => pick(i)));
    function pick(i) { bs.forEach((b, j) => b.classList.toggle("on", i === j)); fn(i); }
    return pick;
  }
  // x axis with tick labels, returns the group
  function axes(g, X, Y, x0, x1, y0, ticks, opt) {
    opt = opt || {};
    S("line", { x1: X(x0), x2: X(x1), y1: Y(y0), y2: Y(y0), class: "ax" }, g);
    ticks.forEach(([v, lab]) => {
      S("line", { x1: X(v), x2: X(v), y1: Y(y0), y2: Y(y0) + 4, class: "ax" }, g);
      S("text", { x: X(v), y: Y(y0) + 17, class: "w-t s", "text-anchor": "middle", text: lab }, g);
    });
    if (opt.name) S("text", { x: X(x1), y: Y(y0) - 6, class: "w-t s", "text-anchor": "end", text: opt.name }, g);
  }
  // svg point from a pointer event (viewBox coordinates)
  function svgPoint(svg, e) {
    const p = svg.createSVGPoint();
    p.x = e.clientX; p.y = e.clientY;
    return p.matrixTransform(svg.getScreenCTM().inverse());
  }
  function drag(svg, fn) {
    let on = false;
    svg.addEventListener("pointerdown", (e) => { on = true; svg.setPointerCapture(e.pointerId); fn(svgPoint(svg, e)); });
    svg.addEventListener("pointermove", (e) => { if (on) fn(svgPoint(svg, e)); });
    ["pointerup", "pointercancel"].forEach((ev) => svg.addEventListener(ev, () => { on = false; }));
  }
  // repeat fn(u) for u in [0,1] over ms, then done; returns a stop function
  function sweep(ms, fn, done) {
    let alive = true;
    const t0 = performance.now();
    (function loop(t) {
      if (!alive) return;
      const u = Math.min(1, (t - t0) / ms);
      fn(u);
      if (u < 1) requestAnimationFrame(loop); else if (done) done();
    })(t0);
    return () => { alive = false; };
  }

  // ---------- morphing renderer: shapes keyed by id glide from one scene to the next ----------
  const MORPH = new Set(["x", "y", "width", "height", "x1", "x2", "y1", "y2", "cx", "cy", "r", "rx", "d", "opacity", "transform", "points"]);
  const NUM = /-?\d*\.?\d+(?:e[-+]?\d+)?/g;
  function mix(k, a, b, u) {
    if (a === undefined || a === b || !MORPH.has(k)) return b;
    if (typeof a === "number" && typeof b === "number") return a + (b - a) * u;
    const na = String(a).match(NUM) || [], nb = String(b).match(NUM) || [];
    if (na.length && na.length === nb.length) {
      let i = 0;
      return String(b).replace(NUM, () => { const v = +na[i] + (+nb[i] - +na[i]) * u; i++; return v.toFixed(2); });
    }
    return u < 1 ? a : b;
  }
  function Morph(svg) {
    const live = new Map();
    let cancel = null;
    function paint(n, a) {
      for (const k in a) { if (k === "text") n.el.textContent = a[k]; else n.el.setAttribute(k, a[k]); }
      n.a = a;
    }
    return function set(shapes, ms) {
      if (cancel) { cancel(); cancel = null; }
      const want = new Set(), plan = [];
      shapes.forEach((s) => {
        want.add(s.id);
        const to = Object.assign({ opacity: 1 }, s.a);
        if (s.text !== undefined) to.text = s.text;
        let n = live.get(s.id);
        if (!n) { n = { el: S(s.tag), a: {} }; live.set(s.id, n); paint(n, Object.assign({}, to, { opacity: 0 })); }
        svg.appendChild(n.el);
        plan.push([n, Object.assign({}, n.a), to, null]);
      });
      live.forEach((n, id) => { if (!want.has(id)) plan.push([n, Object.assign({}, n.a), Object.assign({}, n.a, { opacity: 0 }), id]); });
      const frame = (u) => plan.forEach(([n, a0, a1]) => { const c = {}; for (const k in a1) c[k] = mix(k, a0[k], a1[k], u); paint(n, c); });
      const end = () => plan.forEach(([n, , , gone]) => { if (gone) { n.el.remove(); live.delete(gone); } });
      if (!ms || still) { frame(1); end(); } else cancel = tween(ms, frame, end);
    };
  }
  const readTime = (s) => clamp(1500 + s.replace(/<[^>]+>/g, "").replace(/\$[^$]*\$/g, "xxxxxx").length * 42, 2800, 8000);

  // a widget that is a sequence of scenes with Back / Next / Replay
  function staged(root, w, h, n, scene, caption, extra) {
    const { svg, cap, bar } = shell(root, w, h);
    const set = Morph(svg);
    let k = 0, timer = null;
    const back = btn(bar, "‹ Back", () => go(k - 1));
    const next = btn(bar, "Next ›", () => go(k + 1), "main");
    const count = H("span", { class: "w-count" }, bar);
    btn(bar, "↻ Replay", () => { go(0, 400); play(); });
    if (extra) extra(bar, () => go(k, 600));
    function go(i, ms) {
      k = clamp(i, 0, n() - 1);
      set(scene(k), ms === undefined ? 850 : ms);
      tex(cap, caption(k));
      count.textContent = (k + 1) + " / " + n();
      back.disabled = k === 0;
      next.disabled = k === n() - 1;
    }
    function stop() { clearTimeout(timer); timer = null; }
    function play() {
      stop();
      const tick = () => {
        if (k >= n() - 1) return;
        timer = setTimeout(() => { go(k + 1); tick(); }, readTime(caption(k)));
      };
      tick();
    }
    go(0, 0);
    return { play, stop, go };
  }

  // ---------- 1.1 Bayes with counts ----------
  W.bayes = (root) => {
    const G = [["M₁", 0.40, 0.02], ["M₂", 0.35, 0.04], ["M₃", 0.25, 0.05]], N = 1000, pick = 1;
    const L = 20, R = 620, gap = 16, top = 48, BH = 120, EX = 8, pileY = 236, pileH = 30;
    const cnt = G.map((g) => g[1] * N), bad = G.map((g, i) => cnt[i] * g[2]);
    const tot = bad.reduce((a, b) => a + b, 0);
    const fills = ["f-sea", "f-plum", "f-teal"];
    function scene(k) {
      const out = [];
      const span = R - L - (k ? gap * (G.length - 1) : 0);
      let x = L, px = L;
      G.forEach((g, i) => {
        const wd = span * g[1];
        out.push({ id: "g" + i, tag: "rect", a: { x: x, y: top, width: wd, height: BH, rx: 3, class: k ? fills[i] : "f-grey", opacity: k >= 3 ? 0.35 : 1 } });
        if (k >= 1) out.push({ id: "gl" + i, tag: "text", text: g[0] + ": " + fmt(cnt[i]) + " chips", a: { x: x + wd / 2, y: top - 12, class: "w-t b", "text-anchor": "middle", opacity: k >= 3 ? 0.5 : 1 } });
        const bh = BH * g[2] * EX;
        const hl = k === 4 ? (i === pick ? 1 : 0.22) : 1;
        if (k === 2) {
          out.push({ id: "b" + i, tag: "rect", a: { x: x, y: top + BH - bh, width: wd, height: bh, rx: 2, class: "f-red solid" } });
          out.push({ id: "bl" + i, tag: "text", text: fmt(g[2] * 100) + " % of " + fmt(cnt[i]) + " = " + fmt(bad[i]), a: { x: x + wd / 2, y: top + BH - bh - 9, class: "w-t b red", "text-anchor": "middle" } });
        }
        if (k >= 3) {
          const pw = ((R - L) * bad[i]) / tot;
          out.push({ id: "b" + i, tag: "rect", a: { x: px, y: pileY, width: pw - 3, height: pileH, rx: 2, class: "f-red solid", opacity: hl } });
          out.push({ id: "bl" + i, tag: "text", text: G[i][0] + ": " + fmt(bad[i]), a: { x: px + pw / 2, y: pileY + pileH / 2 + 5, class: "w-t b inv", "text-anchor": "middle", opacity: hl } });
          px += pw;
        }
        x += wd + (k ? gap : 0);
      });
      if (k === 0) out.push({ id: "all", tag: "text", text: "1000 chips", a: { x: (L + R) / 2, y: top + BH / 2 + 8, class: "w-t big", "text-anchor": "middle" } });
      if (k >= 3) {
        out.push({ id: "pl", tag: "text", text: k === 3 ? "the defective pile: " + fmt(tot) + " chips" : fmt(bad[pick]) + " of the " + fmt(tot) + " defective chips came from M₂", a: { x: L, y: pileY - 12, class: "w-t b red" } });
      }
      return out;
    }
    const caps = [
      "Percentages are confusing; <b>counts</b> are not. Imagine exactly <b>1000 chips</b>.",
      "Split them by machine: 40 % of 1000 = <b>400</b> from M₁, 35 % = <b>350</b> from M₂, 25 % = <b>250</b> from M₃.",
      "Inside each group, the defective ones (red, drawn 8× taller so you can see them): $0.02\\times400=8$, $0.04\\times350=14$, $0.05\\times250=12.5$. Half a chip is fine: these are averages.",
      "Throw every defective chip on one pile: $8+14+12.5=34.5$ out of 1000. So $P(D)=34.5/1000=\\mathbf{0.0345}$. This is the <b>total probability</b> rule.",
      "Now look <b>only at the pile</b>. 14 of its 34.5 chips came from M₂: $P(M_2\\mid D)=14/34.5\\approx\\mathbf{0.41}$. This is <b>Bayes' rule</b>: divide by the pile, not by 1000.",
    ];
    return staged(root, 640, 280, () => caps.length, scene, (k) => caps[k]);
  };

  // ---------- 1.2 joint PDF: slice the region ----------
  W.region = (root, preset) => {
    const f = (v) => fmt(v, 2);
    const P = [
      { tab: "Apr 2024: $2$ on $0\\le y\\le x\\le1$", poly: [[0, 0], [1, 0], [1, 1]], dir: "h", lo: (t) => t, hi: () => 1, m: (t) => 2 * (1 - t), mmax: 2.2, mlab: "p_Y(y) = 2(1 − y)",
        cap: (t) => "Stand at height $y=" + f(t) + "$ and walk right through the triangle: you enter at the diagonal $x=y=" + f(t) + "$ and leave at $x=1$. So $p_Y(" + f(t) + ")=\\int_{" + f(t) + "}^{1}2\\,dx=2(1-" + f(t) + ")=" + f(2 * (1 - t)) + "$." },
      { tab: "Apr 2025: $cx+1$ on $x+y\\lt 1$", poly: [[0, 0], [1, 0], [0, 1]], dir: "v", lo: () => 0, hi: (t) => 1 - t, m: (t) => (3 * t + 1) * (1 - t), mmax: 1.5, mlab: "(cx+1)(1 − x), c = 3",
        cap: (t) => "At $x=" + f(t) + "$ the slice goes from $y=0$ up to the line $y=1-x=" + f(1 - t) + "$. The height $cx+1$ has no $y$ in it, so the slice integral is height × length: $(cx+1)(1-x)$. The blue area under that curve is the total, $\\frac c6+\\frac12$, which must be 1." },
      { tab: "Jun 2026: $6x^2y$ on the square", poly: [[0, 0], [1, 0], [1, 1], [0, 1]], dir: "v", lo: () => 0, hi: () => 1, m: (t) => 3 * t * t, mmax: 3.3, mlab: "p_X(x) = 3x²",
        cap: (t) => "At $x=" + f(t) + "$ the slice always runs from $y=0$ to $y=1$: the region is a <b>rectangle</b>, the limits never depend on $x$. So $p_X(" + f(t) + ")=\\int_0^1 6x^2y\\,dy=3x^2=" + f(3 * t * t) + "$." },
    ];
    let cur = clamp(+(preset || 0), 0, 2), t = 0.3, stopper = null;
    const { svg, cap, bar } = shell(root, 640, 290);
    const g = S("g", {}, svg);
    const pick = tabs(bar, P.map((p) => p.tab), (i) => { cur = i; draw(); });
    bar.querySelectorAll(".w-tabs .w-btn").forEach((b, i) => tex(b, P[i].tab));
    const sl = slider(bar, "slice at", 0.02, 0.98, 0.01, t, (v) => { t = v; draw(); });
    btn(bar, "▶ Sweep", () => play(), "main");
    const X = lin(0, 1, 60, 260), Y = lin(0, 1, 250, 50);
    const MX = lin(0, 1, 370, 610);
    function draw() {
      const p = P[cur];
      g.innerHTML = "";
      const MY = lin(0, p.mmax, 250, 50);
      // left: region
      S("rect", { x: X(0), y: Y(1), width: X(1) - X(0), height: Y(0) - Y(1), class: "frame" }, g);
      S("path", { d: pathOf(p.poly.map(([a, b]) => [X(a), Y(b)])) + " Z", class: "f-sea" }, g);
      [[0, "0"], [1, "1"]].forEach(([v, l]) => {
        S("text", { x: X(v), y: Y(0) + 17, class: "w-t s", "text-anchor": "middle", text: l }, g);
        S("text", { x: X(0) - 8, y: Y(v) + 4, class: "w-t s", "text-anchor": "end", text: l }, g);
      });
      S("text", { x: X(1) + 12, y: Y(0) + 4, class: "w-t s", text: "x" }, g);
      S("text", { x: X(0) - 4, y: Y(1) - 10, class: "w-t s", "text-anchor": "middle", text: "y" }, g);
      const lo = p.lo(t), hi = p.hi(t);
      if (p.dir === "h") {
        S("line", { x1: X(0), x2: X(1), y1: Y(t), y2: Y(t), class: "c-grey dash" }, g);
        S("line", { x1: X(lo), x2: X(hi), y1: Y(t), y2: Y(t), class: "c-red thick" }, g);
        S("circle", { cx: X(lo), cy: Y(t), r: 4.5, class: "dot-red" }, g);
        S("circle", { cx: X(hi), cy: Y(t), r: 4.5, class: "dot-red" }, g);
        S("text", { x: X(lo) - 6, y: Y(t) - 9, class: "w-t s red b", "text-anchor": "end", text: "x = y" }, g);
        S("text", { x: X(hi) + 6, y: Y(t) - 9, class: "w-t s red b", text: "x = 1" }, g);
      } else {
        S("line", { x1: X(t), x2: X(t), y1: Y(0), y2: Y(1), class: "c-grey dash" }, g);
        S("line", { x1: X(t), x2: X(t), y1: Y(lo), y2: Y(hi), class: "c-red thick" }, g);
        S("circle", { cx: X(t), cy: Y(lo), r: 4.5, class: "dot-red" }, g);
        S("circle", { cx: X(t), cy: Y(hi), r: 4.5, class: "dot-red" }, g);
        S("text", { x: X(t) + 8, y: Y(hi) - 6, class: "w-t s red b", text: cur === 1 ? "y = 1 − x" : "y = 1" }, g);
        S("text", { x: X(t) + 8, y: Y(lo) - 6, class: "w-t s red b", text: "y = 0" }, g);
      }
      // right: the marginal (or inner integral) traced as the slice moves
      const xs = grid(0, 1, 80);
      if (cur === 1) S("path", { d: pathOf(xs.map((v) => [MX(v), MY(p.m(v))])) + " L" + MX(1) + " " + MY(0) + " L" + MX(0) + " " + MY(0) + " Z", class: "f-sea" }, g);
      axes(g, MX, MY, 0, 1, 0, [[0, "0"], [0.5, "0.5"], [1, "1"]], { name: p.dir === "h" ? "y" : "x" });
      S("line", { x1: MX(0), x2: MX(0), y1: MY(0), y2: MY(p.mmax), class: "ax" }, g);
      S("path", { d: pathOf(xs.map((v) => [MX(v), MY(p.m(v))])), class: "c-grey dash" }, g);
      const done = xs.filter((v) => v <= t).concat([t]);
      S("path", { d: pathOf(done.map((v) => [MX(v), MY(p.m(v))])), class: "c-red" }, g);
      S("line", { x1: MX(t), x2: MX(t), y1: MY(0), y2: MY(p.m(t)), class: "c-red dash" }, g);
      S("circle", { cx: MX(t), cy: MY(p.m(t)), r: 5, class: "dot-red" }, g);
      S("text", { x: MX(0.5), y: 32, class: "w-t b", "text-anchor": "middle", text: p.mlab }, g);
      S("text", { x: X(0.5), y: 32, class: "w-t b", "text-anchor": "middle", text: "the region (draw it first)" }, g);
      tex(cap, p.cap(t));
    }
    function stop() { if (stopper) stopper(); stopper = null; }
    function play() { stop(); stopper = sweep(5000, (u) => sl.set(0.02 + 0.96 * u)); }
    pick(cur);
    return { play, stop };
  };

  // ---------- 1.3 ensemble vs time average ----------
  W.ensemble = (root, preset) => {
    const N = 64, ROWS = 4, rnd = mulberry(11);
    const K = [
      { tab: "Dice", lo: 0.3, hi: 6.7, mean: () => 3.5, dots: true, gen: () => Array.from({ length: N }, () => 1 + Math.floor(rnd() * 6)),
        cap: (ta, n) => "<b>Down the column</b> (blue, every die at the same time $n$): over infinitely many dice the average is $E[X[n]]=3.5$, at every $n$. <b>Along the row</b> (red, die 1 over time): running average so far $=" + fmt(ta) + "$, and it settles on 3.5. Same number → <b>ergodic in the mean</b> (the spread matches too → ergodic in the variance)." },
      { tab: "Random constant $A$", lo: -1.6, hi: 3.6, mean: () => 1, gen: (r) => Array(N).fill([2.6, 0.2, 1.7, -0.7][r]),
        cap: (ta) => "Each realisation is a <b>flat line at its own random height</b> $A$. Down the column: $E[A]=1$. Along row 1: always $" + fmt(ta) + "$, however long you wait. Different → <b>not ergodic</b>, even though the process is WSS (mean and $r$ do not change with time)." },
      { tab: "$\\cos(\\omega n+U)$", lo: -1.4, hi: 1.4, mean: () => 0, gen: (r) => { const U = [0.4, 2.2, 3.9, 5.4][r]; return Array.from({ length: N }, (_, n) => Math.cos(0.42 * n + U)); },
        cap: (ta) => "Random <b>phase</b> $U$: down the column the cosines are shifted at random and cancel, $E[X[n]]=0$ at every $n$. Along row 1 the wave goes up and down; its running average $=" + fmt(ta) + "$ → 0. Same → <b>WSS and ergodic in the mean</b>." },
      { tab: "$A\\cos(\\omega n)$", lo: -2.8, hi: 2.8, mean: (n) => Math.cos(0.42 * n), gen: (r) => { const A = [2.2, 0.5, 1.4, -0.9][r]; return Array.from({ length: N }, (_, n) => A * Math.cos(0.42 * n)); },
        cap: () => "Random <b>amplitude</b> $A$ with $E[A]=1$: down the column $E[X[n]]=E[A]\\cos(\\omega n)=\\cos(\\omega n)$ (blue dashed, row 1). It <b>changes with $n$</b> → <b>not WSS</b>, and so not ergodic either." },
    ];
    let cur = clamp(+(preset || 0), 0, 3), data = [], n0 = 20, stopper = null;
    const { svg, cap, bar } = shell(root, 640, 345);
    const g = S("g", {}, svg);
    const pick = tabs(bar, K.map((k) => k.tab), (i) => { cur = i; data = Array.from({ length: ROWS }, (_, r) => K[i].gen(r)); draw(); });
    bar.querySelectorAll(".w-tabs .w-btn").forEach((b, i) => tex(b, K[i].tab));
    const sl = slider(bar, "time $n$", 0, N - 1, 1, n0, (v) => { n0 = v; draw(); });
    btn(bar, "▶ Play", () => play(), "main");
    const X = lin(0, N - 1, 62, 620), RH = 72, T0 = 26;
    function draw() {
      const k = K[cur];
      g.innerHTML = "";
      S("rect", { x: X(n0) - 7, y: T0 - 6, width: 14, height: ROWS * RH, rx: 6, class: "f-sea" }, g);
      S("text", { x: X(n0), y: T0 + ROWS * RH + 20, class: "w-t s b sea", "text-anchor": "middle", text: "ensemble: down the column at n = " + n0 }, g);
      data.forEach((row, r) => {
        const y0 = T0 + r * RH, Y = lin(k.lo, k.hi, y0 + RH - 10, y0 + 4);
        S("text", { x: 8, y: y0 + RH / 2, class: "w-t s" + (r === 0 ? " b red" : ""), text: "row " + (r + 1) }, g);
        S("line", { x1: X(0), x2: X(N - 1), y1: Y((k.lo + k.hi) / 2), y2: Y((k.lo + k.hi) / 2), class: "grid" }, g);
        const cls = r === 0 ? "c-ink" : "c-grey";
        if (k.dots) row.forEach((v, n) => S("circle", { cx: X(n), cy: Y(v), r: 2.6, class: r === 0 ? "dot-ink" : "dot-grey" }, g));
        else S("path", { d: pathOf(row.map((v, n) => [X(n), Y(v)])), class: cls + " thin" }, g);
        S("circle", { cx: X(n0), cy: Y(row[n0]), r: 4.5, class: "dot-sea" }, g);
        if (r === 0) {
          const m = grid(0, N - 1, N).map((n) => [X(n), Y(k.mean(n))]);
          S("path", { d: pathOf(m), class: "c-sea dash" }, g);
          let s = 0;
          const run = row.slice(0, n0 + 1).map((v, n) => { s += v; return [X(n), Y(s / (n + 1))]; });
          if (run.length > 1) S("path", { d: pathOf(run), class: "c-red thick" }, g);
          S("text", { x: X(N - 1), y: y0 + 2, class: "w-t s b red", "text-anchor": "end", text: "time average of row 1 (red)  ·  ensemble mean (blue dashed)" }, g);
        }
      });
      let s = 0;
      for (let n = 0; n <= n0; n++) s += data[0][n];
      tex(cap, k.cap(s / (n0 + 1), n0));
    }
    function stop() { if (stopper) stopper(); stopper = null; }
    function play() { stop(); stopper = sweep(6500, (u) => sl.set(Math.round(u * (N - 1)))); }
    pick(cur);
    return { play, stop };
  };

  // ---------- 1.4 / 3.2 pole of L(z) = 1/(1 + a z^-1) and the PSD it makes ----------
  W.pole = (root, preset) => {
    const factor = preset === "factor";
    let a = +(root.dataset.a || (factor ? 0.3 : 0.8)), stopper = null;
    const { svg, cap, bar } = shell(root, 640, 280);
    const g = S("g", {}, svg);
    const sl = slider(bar, "$a$", -0.95, 0.95, 0.01, a, (v) => { a = v; draw(); });
    btn(bar, "▶ Play", () => play(), "main");
    const CX = 130, CY = 145, RAD = 92;
    const PX = lin(0, Math.PI, 330, 615);
    function draw() {
      g.innerHTML = "";
      S("line", { x1: CX - 120, x2: CX + 120, y1: CY, y2: CY, class: "ax" }, g);
      S("line", { x1: CX, x2: CX, y1: CY - 115, y2: CY + 115, class: "ax" }, g);
      S("circle", { cx: CX, cy: CY, r: RAD, class: "c-ink thin" }, g);
      S("text", { x: CX + 118, y: CY - 6, class: "w-t s", "text-anchor": "end", text: "Re z" }, g);
      S("text", { x: CX + RAD + 2, y: CY + 16, class: "w-t s", text: "1" }, g);
      S("text", { x: CX - RAD - 4, y: CY + 16, class: "w-t s", "text-anchor": "end", text: "−1" }, g);
      S("text", { x: CX, y: 18, class: "w-t b", "text-anchor": "middle", text: "pole of L(z) at z = −a" }, g);
      const px = CX - a * RAD;
      const cross = (x, y, cls) => { S("path", { d: "M" + (x - 7) + " " + (y - 7) + " L" + (x + 7) + " " + (y + 7) + " M" + (x - 7) + " " + (y + 7) + " L" + (x + 7) + " " + (y - 7), class: cls }, g); };
      cross(px, CY, "c-red thick");
      S("text", { x: px, y: CY - 14, class: "w-t s b red", "text-anchor": "middle", text: "−a = " + fmt(-a) }, g);
      if (factor && Math.abs(a) > 0.04) {
        const m = -1 / a, mx = CX + m * RAD;
        const off = Math.abs(m) * RAD > 118;
        const x = off ? CX + Math.sign(m) * 118 : mx;
        cross(x, CY, "c-grey thick");
        S("text", { x: x, y: CY + 30, class: "w-t s grey", "text-anchor": m > 0 ? "end" : "start", text: (off && m < 0 ? "← " : "") + "mirror −1/a = " + fmt(m) + (off && m > 0 ? " →" : "") }, g);
        S("text", { x: CX, y: CY + 128, class: "w-t s", "text-anchor": "middle", text: "keep the root inside the circle" }, g);
      }
      // PSD with sigma^2 = 1
      const D = (t) => 1 + a * a + 2 * a * Math.cos(t);
      const ts = grid(0, Math.PI, 120), vals = ts.map((t) => 1 / D(t));
      const top = Math.max.apply(null, vals) * 1.12;
      const PY = lin(0, top, 245, 35);
      axes(g, PX, PY, 0, Math.PI, 0, [[0, "0"], [Math.PI / 2, "π/2"], [Math.PI, "π"]], { name: "θ" });
      S("path", { d: pathOf(ts.map((t, i) => [PX(t), PY(vals[i])])), class: "c-red" }, g);
      S("circle", { cx: PX(0), cy: PY(vals[0]), r: 4, class: "dot-red" }, g);
      S("circle", { cx: PX(Math.PI), cy: PY(vals[119]), r: 4, class: "dot-red" }, g);
      S("text", { x: PX(0) + 6, y: PY(vals[0]) - 8, class: "w-t s b", text: "P(0) = " + fmt(vals[0]) }, g);
      S("text", { x: PX(Math.PI) - 6, y: PY(vals[119]) - 8, class: "w-t s b", "text-anchor": "end", text: "P(π) = " + fmt(vals[119]) }, g);
      S("text", { x: PX(Math.PI / 2), y: 18, class: "w-t b", "text-anchor": "middle", text: "PSD = 1 / (1 + a² + 2a cos θ)" }, g);
      const c0 = 1 + a * a, c1 = 2 * a;
      let txt = "Denominator: $1+a^2+2a\\cos\\theta=" + fmt(c0) + (c1 >= 0 ? "+" : "") + fmt(c1) + "\\cos\\theta$. ";
      if (factor) {
        txt += "Ratio cosine/constant $=\\frac{2a}{1+a^2}=" + fmt(c1 / c0, 3) + "$. The exam's $61+60\\cos\\theta$ has ratio $\\frac{60}{61}=0.984$: slide until they match ($a=\\frac56\\approx0.83$). The mirror root $-1/a$ gives the <b>same ratio</b> but lies outside the circle, so it is thrown away.";
      } else {
        txt += a > 0.05 ? "$a>0$: the pole sits on the <b>left</b> ($z\\approx-1$, i.e. $\\theta=\\pi$), so the peak is at <b>high</b> frequency." :
          a < -0.05 ? "$a\\lt 0$: the pole sits on the <b>right</b> ($z\\approx1$, i.e. $\\theta=0$), so the peak is at <b>low</b> frequency." : "$a\\approx0$: no pole to speak of, the PSD is flat (white noise).";
        txt += " Closer to the circle = sharper peak.";
      }
      tex(cap, txt);
    }
    function stop() { if (stopper) stopper(); stopper = null; }
    function play() {
      stop();
      if (factor) stopper = sweep(4000, (u) => sl.set(+(0.1 + (5 / 6 - 0.1) * (1 - Math.pow(1 - u, 2))).toFixed(2)), () => sl.set(0.83));
      else stopper = sweep(6000, (u) => sl.set(+(0.85 * Math.cos(u * 2 * Math.PI)).toFixed(2)));
    }
    draw();
    return { play, stop };
  };

  // ---------- 2.1 likelihood: which theta makes the data most likely ----------
  W.likelihood = (root) => {
    const xs = [1.2, 0.8, 2.1, 1.5, 1.0], Nn = xs.length;
    const best = xs.reduce((s, x) => s + x * x, 0) / (2 * Nn);
    const pdf = (x, th) => (x / th) * Math.exp((-x * x) / (2 * th));
    const lnL = (th) => xs.reduce((s, x) => s + Math.log(pdf(x, th)), 0);
    let th = 0.4, stopper = null;
    const { svg, cap, bar } = shell(root, 640, 340);
    const g = S("g", {}, svg);
    const sl = slider(bar, "$\\theta$", 0.2, 3, 0.01, th, (v) => { th = v; draw(); });
    btn(bar, "▶ Sweep θ", () => play(), "main");
    btn(bar, "Jump to the top", () => { stop(); const s0 = th; stopper = sweep(900, (u) => sl.set(+(s0 + (best - s0) * u).toFixed(3))); });
    const X = lin(0, 3.6, 60, 620), Y = lin(0, 1.25, 150, 28);
    const TX = lin(0.2, 3, 60, 620), lmin = -16, lmax = -3, TY = lin(lmin, lmax, 315, 205);
    function draw() {
      g.innerHTML = "";
      S("text", { x: 60, y: 16, class: "w-t b", text: "Top: the model p(x | θ) and the 5 data points. Each stick = how likely that point is." }, g);
      axes(g, X, Y, 0, 3.6, 0, [[0, "0"], [1, "1"], [2, "2"], [3, "3"]], { name: "x" });
      const gx = grid(0.001, 3.6, 150);
      S("path", { d: pathOf(gx.map((x) => [X(x), Y(Math.min(1.25, pdf(x, th)))])), class: "c-sea" }, g);
      xs.forEach((x) => {
        const p = pdf(x, th);
        S("line", { x1: X(x), x2: X(x), y1: Y(0), y2: Y(Math.min(1.25, p)), class: "c-red thick" }, g);
        S("circle", { cx: X(x), cy: Y(0), r: 4, class: "dot-ink" }, g);
      });
      S("text", { x: 60, y: 196, class: "w-t b", text: "Bottom: ln L(θ) = sum of the log stick heights, for every θ." }, g);
      axes(g, TX, TY, 0.2, 3, lmin, [[0.5, "0.5"], [1, "1"], [1.5, "1.5"], [2, "2"], [2.5, "2.5"], [3, "3"]], { name: "θ" });
      const gt = grid(0.2, 3, 140);
      S("path", { d: pathOf(gt.map((t) => [TX(t), TY(clamp(lnL(t), lmin, lmax))])), class: "c-plum" }, g);
      S("line", { x1: TX(best), x2: TX(best), y1: TY(lmin), y2: TY(lnL(best)), class: "c-moss dash" }, g);
      S("text", { x: TX(best) + 8, y: TY(lnL(best)) + 20, class: "w-t s b moss", text: "top: θ̂ = Σx²/(2N) = " + fmt(best) }, g);
      S("circle", { cx: TX(th), cy: TY(clamp(lnL(th), lmin, lmax)), r: 6, class: "dot-red" }, g);
      const v = lnL(th);
      const where = th < best - 0.12 ? "Too <b>narrow</b>: the point at 2.1 gets a tiny stick and drags the total down."
        : th > best + 0.12 ? "Too <b>wide</b>: every stick is short."
        : "Best compromise: all sticks as tall as possible <b>together</b>. This $\\theta$ is the MLE.";
      tex(cap, "$\\theta=" + fmt(th) + "$: $\\ln L=" + fmt(v, 2) + "$. " + where + " The MLE is the $\\theta$ at the top of the bottom curve, where its slope is 0: that is why we <b>differentiate and set to 0</b>.");
    }
    function stop() { if (stopper) stopper(); stopper = null; }
    function play() { stop(); stopper = sweep(6000, (u) => sl.set(+(0.25 + 2.6 * (0.5 - 0.5 * Math.cos(u * 2 * Math.PI))).toFixed(3)), () => { stopper = sweep(900, (u) => sl.set(+(0.25 + (best - 0.25) * u).toFixed(3))); }); }
    draw();
    return { play, stop };
  };

  // ---------- 2.2 prior x likelihood = posterior (Beta, coin-type data) ----------
  W.posterior = (root) => {
    let al = 2, be = 3, s = 10, fl = 12, stopper = null;
    const { svg, cap, bar } = shell(root, 640, 280);
    const g = S("g", {}, svg);
    const sA = slider(bar, "prior $\\alpha$", 1, 12, 1, al, (v) => { al = v; draw(); });
    const sB = slider(bar, "prior $\\beta$", 1, 12, 1, be, (v) => { be = v; draw(); });
    const sS = slider(bar, "successes", 0, 80, 1, s, (v) => { s = v; draw(); });
    const sF = slider(bar, "failures", 0, 80, 1, fl, (v) => { fl = v; draw(); });
    btn(bar, "×4 data", () => { stop(); const s0 = s, f0 = fl; stopper = sweep(1500, (u) => { sS.set(Math.round(s0 + 3 * s0 * u)); sF.set(Math.round(f0 + 3 * f0 * u)); }); }, "main");
    btn(bar, "Reset (Jun 2026)", () => { stop(); sA.set(2); sB.set(3); sS.set(10); sF.set(12); });
    const X = lin(0, 1, 50, 620), Y = lin(0, 1.15, 245, 30);
    const ts = grid(0.002, 0.998, 200);
    function curve(A, B) {
      const lv = ts.map((t) => (A - 1) * Math.log(t) + (B - 1) * Math.log(1 - t));
      const m = Math.max.apply(null, lv);
      return lv.map((v) => Math.exp(v - m));
    }
    function draw() {
      g.innerHTML = "";
      axes(g, X, Y, 0, 1, 0, [[0, "0"], [0.25, "0.25"], [0.5, "0.5"], [0.75, "0.75"], [1, "1"]], { name: "θ" });
      const pr = curve(al, be), lk = curve(s + 1, fl + 1), po = curve(al + s, be + fl);
      const pts = (v) => ts.map((t, i) => [X(t), Y(v[i])]);
      S("path", { d: pathOf(pts(po)) + " L" + X(0.998) + " " + Y(0) + " L" + X(0.002) + " " + Y(0) + " Z", class: "f-red" }, g);
      S("path", { d: pathOf(pts(pr)), class: "c-grey dash" }, g);
      S("path", { d: pathOf(pts(lk)), class: "c-sea" }, g);
      S("path", { d: pathOf(pts(po)), class: "c-red" }, g);
      const a = al + s, b = be + fl;
      const map = a > 1 && b > 1 ? (a - 1) / (a + b - 2) : null, mle = s + fl > 0 ? s / (s + fl) : null;
      if (mle !== null) { S("line", { x1: X(mle), x2: X(mle), y1: Y(0), y2: Y(1.06), class: "c-sea dash" }, g); S("text", { x: X(mle) + (mle > (map || 0) ? 5 : -5), y: Y(1.08), class: "w-t s b sea", "text-anchor": mle > (map || 0) ? "start" : "end", text: "MLE " + fmt(mle) }, g); }
      if (map !== null) { S("line", { x1: X(map), x2: X(map), y1: Y(0), y2: Y(1.06), class: "c-red dash" }, g); S("text", { x: X(map) + (mle !== null && mle > map ? -5 : 5), y: Y(1.08), class: "w-t s b red", "text-anchor": mle !== null && mle > map ? "end" : "start", text: "MAP " + fmt(map) }, g); }
      S("text", { x: 52, y: 16, class: "w-t s", text: "grey dashed = prior   ·   blue = likelihood   ·   red = posterior (all scaled to height 1)" }, g);
      tex(cap, "Prior $\\theta^{" + (al - 1) + "}(1-\\theta)^{" + (be - 1) + "}$ × likelihood $\\theta^{" + s + "}(1-\\theta)^{" + fl + "}$ = posterior $\\theta^{" + (a - 1) + "}(1-\\theta)^{" + (b - 1) + "}$: <b>the exponents just add</b>. That is Beta$(" + a + "," + b + ")$, whose top is $\\frac{a-1}{a+b-2}=\\frac{" + (a - 1) + "}{" + (a + b - 2) + "}" + (map !== null ? "=" + fmt(map) : "") + "$. Press <b>×4 data</b>: the prior matters less and MAP moves onto the MLE.");
    }
    function stop() { if (stopper) stopper(); stopper = null; }
    function play() { stop(); stopper = sweep(2600, (u) => { sS.set(Math.round(10 * u)); sF.set(Math.round(12 * u)); }); }
    draw();
    return { play, stop };
  };

  // ---------- 2.3 least squares: the line with the smallest total square area ----------
  W.ls = (root) => {
    const P = [[0, 3], [2, 4], [3, 3]], BM = 1 / 14, BB = 45 / 14;
    let m = 0.7, b = 2.2, stopper = null;
    const { svg, cap, bar } = shell(root, 640, 300);
    const g = S("g", {}, svg);
    const sm = slider(bar, "slope", -1, 1.2, 0.005, m, (v) => { m = v; draw(); }, (v) => fmt(v, 3));
    const sb = slider(bar, "intercept", 1.5, 4.5, 0.005, b, (v) => { b = v; draw(); }, (v) => fmt(v, 3));
    btn(bar, "▶ Find the best line", () => play(), "main");
    const X = lin(-0.5, 4, 50, 620), Y = lin(1, 5.2, 270, 20);
    function draw() {
      g.innerHTML = "";
      axes(g, X, Y, -0.5, 4, 1, [[0, "0"], [1, "1"], [2, "2"], [3, "3"], [4, "4"]], { name: "x" });
      S("line", { x1: X(-0.5), x2: X(-0.5), y1: Y(1), y2: Y(5.2), class: "ax" }, g);
      [2, 3, 4, 5].forEach((v) => S("text", { x: X(-0.5) - 6, y: Y(v) + 4, class: "w-t s", "text-anchor": "end", text: v }, g));
      let sse = 0;
      P.forEach(([x, y]) => {
        const yh = m * x + b, e = y - yh;
        sse += e * e;
        const side = Math.abs(Y(y) - Y(yh));
        S("rect", { x: X(x), y: Math.min(Y(y), Y(yh)), width: side, height: side, class: "f-amber" }, g);
        S("line", { x1: X(x), x2: X(x), y1: Y(y), y2: Y(yh), class: "c-amber thick" }, g);
      });
      S("line", { x1: X(-0.5), x2: X(4), y1: Y(m * -0.5 + b), y2: Y(m * 4 + b), class: "c-sea" }, g);
      P.forEach(([x, y]) => { S("circle", { cx: X(x), cy: Y(y), r: 5.5, class: "dot-ink" }, g); S("text", { x: X(x) - 8, y: Y(y) - 9, class: "w-t s b", "text-anchor": "end", text: "(" + x + ", " + y + ")" }, g); });
      S("text", { x: 620, y: 24, class: "w-t b amber", "text-anchor": "end", text: "total square area = " + fmt(sse, 3) }, g);
      const atBest = Math.abs(m - BM) < 0.004 && Math.abs(b - BB) < 0.004;
      tex(cap, "Each orange square has side = vertical miss of one point, so its <b>area</b> is that squared error. Least squares = pick slope and intercept so the <b>total area is as small as possible</b>. Now: $y=" + fmt(m, 3) + "x+" + fmt(b, 3) + "$, total $=" + fmt(sse, 3) + "$." + (atBest ? " <b>This is the LS line</b> $y=\\frac1{14}x+\\frac{45}{14}$; total $0.643$, no other line does better." : ""));
    }
    function stop() { if (stopper) stopper(); stopper = null; }
    function play() { stop(); const m0 = m, b0 = b; stopper = sweep(1600, (u) => { const e = 1 - Math.pow(1 - u, 3); sm.set(m0 + (BM - m0) * e); sb.set(b0 + (BB - b0) * e); }); }
    draw();
    return { play, stop };
  };

  // ---------- 3.1 correlogram built term by term ----------
  W.corr = (root, preset) => {
    const C = {
      jun26: { r: [3, 2, 1], lab: ["3", "2", "1"], tx: ["3", "+4\\cos\\theta", "+2\\cos2\\theta"] },
      apr25: { r: [2, -0.25, -0.1875], lab: ["2", "−1/4", "−3/16"], tx: ["2", "-\\tfrac12\\cos\\theta", "-\\tfrac38\\cos2\\theta"], extra: true },
    }[preset || "jun26"];
    const r = C.r, K = r.length;
    const ts = grid(0, Math.PI, 90);
    const term = (k) => (t) => (k === 0 ? r[0] : 2 * r[k] * Math.cos(k * t));
    const partial = (k) => (t) => { let s = 0; for (let j = 0; j <= k; j++) s += term(j)(t); return s; };
    const ar = (t) => { const a = -r[1] / r[0], s2 = r[0] + a * r[1]; return s2 / (1 + a * a + 2 * a * Math.cos(t)); };
    const ma = (t) => r[0] + 2 * r[1] * Math.cos(t);
    const all = [];
    for (let k = 0; k < K; k++) ts.forEach((t) => { all.push(term(k)(t), partial(k)(t)); });
    if (C.extra) ts.forEach((t) => all.push(ar(t), ma(t)));
    const lo = Math.min(0, Math.min.apply(null, all)), hi = Math.max.apply(null, all);
    const X = lin(0, Math.PI, 70, 610), Y = lin(lo - 0.08 * (hi - lo), hi + 0.12 * (hi - lo), 262, 30);
    const P = (f) => pathOf(ts.map((t) => [X(t), Y(f(t))]));
    const n = () => K + 1 + (C.extra ? 1 : 0);
    function scene(k) {
      const out = [
        { id: "ax", tag: "line", a: { x1: X(0), x2: X(Math.PI), y1: Y(0), y2: Y(0), class: "ax" } },
        { id: "t0", tag: "text", text: "0", a: { x: X(0), y: Y(lo - 0.08 * (hi - lo)) + 16, class: "w-t s", "text-anchor": "middle" } },
        { id: "t1", tag: "text", text: "π/2", a: { x: X(Math.PI / 2), y: Y(lo - 0.08 * (hi - lo)) + 16, class: "w-t s", "text-anchor": "middle" } },
        { id: "t2", tag: "text", text: "π  (θ)", a: { x: X(Math.PI), y: Y(lo - 0.08 * (hi - lo)) + 16, class: "w-t s", "text-anchor": "middle" } },
        { id: "z", tag: "text", text: "0", a: { x: X(0) - 8, y: Y(0) + 4, class: "w-t s", "text-anchor": "end" } },
      ];
      const j = Math.min(k, K - 1);
      if (k < K) out.push({ id: "term", tag: "path", a: { d: P(term(j)), class: "c-amber dash" } });
      const fin = partial(K - 1);
      out.push({ id: "sum", tag: "path", a: { d: P(partial(j)), class: "c-red thick" } });
      if (k < K) out.push({ id: "tl", tag: "text", text: j === 0 ? "r[0] = " + C.lab[0] : "new term: 2·r[" + j + "]·cos " + (j > 1 ? j : "") + "θ", a: { x: X(Math.PI) - 4, y: Y(term(j)(Math.PI)) + (term(j)(Math.PI) > (lo + hi) / 2 ? 18 : -10), class: "w-t s b amber", "text-anchor": "end" } });
      out.push({ id: "sl", tag: "text", text: k < K ? "running sum" : "P_corr(θ)", a: { x: X(0.55), y: Y(partial(j)(0.55)) - 10, class: "w-t s b red" } });
      if (k >= K) {
        [0, Math.PI].forEach((t, i) => {
          out.push({ id: "m" + i, tag: "circle", a: { cx: X(t), cy: Y(fin(t)), r: 6, class: "dot-red" } });
          out.push({ id: "ml" + i, tag: "text", text: (i ? "P(π) = " : "P(0) = ") + fmt(fin(t), 3), a: { x: X(t) + (i ? -10 : 10), y: Y(fin(t)) + (fin(t) > (lo + hi) / 2 ? 22 : -12), class: "w-t s b", "text-anchor": i ? "end" : "start" } });
        });
      }
      if (k === K + 1) {
        out.push({ id: "ar", tag: "path", a: { d: P(ar), class: "c-sea" } });
        out.push({ id: "ma", tag: "path", a: { d: P(ma), class: "c-moss dash" } });
        out.push({ id: "arl", tag: "text", text: "AR(1)", a: { x: X(2.2), y: Y(ar(2.2)) - 12, class: "w-t s b sea", "text-anchor": "middle" } });
        out.push({ id: "mal", tag: "text", text: "MA(1)", a: { x: X(2.2), y: Y(ma(2.2)) + 20, class: "w-t s b moss", "text-anchor": "middle" } });
      }
      return out;
    }
    const L = C.lab;
    const sumTex = (j) => C.tx.slice(0, j + 1).join("");
    const caps = [];
    caps.push("Start with lag 0: $r[0]=" + L[0] + "$ is a <b>flat line</b> (red).");
    for (let j = 1; j < K; j++) caps.push("Lags $\\pm" + j + "$ together add $r[" + j + "]e^{-j" + (j > 1 ? j : "") + "\\theta}+r[-" + j + "]e^{j" + (j > 1 ? j : "") + "\\theta}=2r[" + j + "]\\cos" + (j > 1 ? j : "") + "\\theta$ (orange). Running sum: $" + sumTex(j) + "$.");
    const f0 = partial(K - 1)(0), fp = partial(K - 1)(Math.PI);
    caps.push("Check the two ends. $\\theta=0$: every cosine is 1, $P(0)=" + fmt(f0, 3) + "$. $\\theta=\\pi$: $\\cos\\pi=-1$, $\\cos2\\pi=+1$, $P(\\pi)=" + fmt(fp, 3) + "$. These two numbers are how you <b>pick the right plot</b>.");
    if (C.extra) caps.push("Pick-the-plot: AR(1) (blue) gives $" + fmt(ar(0), 2) + "$ at 0 and $" + fmt(ar(Math.PI), 2) + "$ at $\\pi$; MA(1) (green) gives $" + fmt(ma(0), 2) + "$ and $" + fmt(ma(Math.PI), 2) + "$. All three <b>rise</b> from left to right: look for the plot where every curve goes up, with these end values.");
    return staged(root, 640, 285, n, scene, (k) => caps[k]);
  };

  // ---------- 3.3 Bartlett / Welch segments ----------
  W.welch = (root) => {
    const N = 1000, L = 200;
    let ov = 0.5, shown = 0, timer = null;
    const { svg, cap, bar } = shell(root, 640, 220);
    const set = Morph(svg);
    const X = lin(0, N, 30, 610);
    const K = () => Math.floor((N - L) / (L * (1 - ov))) + 1;
    const pick = tabs(bar, ["Bartlett (no overlap)", "Welch, 50 % overlap"], (i) => { ov = i ? 0.5 : 0; play(); });
    btn(bar, "▶ Replay", () => play(), "main");
    function scene() {
      const out = [{ id: "sig", tag: "rect", a: { x: X(0), y: 26, width: X(N) - X(0), height: 20, rx: 3, class: "f-grey" } },
        { id: "sl", tag: "text", text: "x[n], N = 1000 samples", a: { x: X(N / 2), y: 41, class: "w-t s b", "text-anchor": "middle" } }];
      [0, 200, 400, 600, 800, 1000].forEach((v) => out.push({ id: "tk" + v, tag: "text", text: String(v), a: { x: X(v), y: 62, class: "w-t s", "text-anchor": "middle" } }));
      const D = L * (1 - ov);
      for (let i = 0; i < shown; i++) {
        const row = ov ? i % 2 : 0;
        out.push({ id: "s" + i, tag: "rect", a: { x: X(i * D) + 1, y: 76 + row * 34, width: X(L) - X(0) - 2, height: 26, rx: 4, class: i % 2 ? "f-plum" : "f-sea" } });
        out.push({ id: "sn" + i, tag: "text", text: String(i + 1), a: { x: X(i * D + L / 2), y: 94 + row * 34, class: "w-t b", "text-anchor": "middle" } });
      }
      out.push({ id: "k", tag: "text", text: "K = " + shown + " segments", a: { x: X(N), y: 170, class: "w-t big", "text-anchor": "end" } });
      return out;
    }
    function caption() {
      const D = L * (1 - ov), k = K();
      return "Segment length $L=200$, hop $D=" + D + "$ " + (ov ? "(50 % overlap: each segment starts halfway through the previous one)" : "(no overlap: Bartlett)") +
        ". Count: $K=\\frac{N-L}{D}+1=\\frac{1000-200}{" + D + "}+1=" + k + "$. Averaging $K$ independent periodograms divides the variance by $K$: ratio $=\\frac1{" + k + "}\\approx" + fmt(1 / k, 3) + "$.";
    }
    function stop() { clearTimeout(timer); timer = null; }
    function play() {
      stop(); shown = 0; set(scene(), 300);
      const tick = () => { if (shown >= K()) return; shown++; set(scene(), 380); timer = setTimeout(tick, still ? 0 : 520); };
      timer = setTimeout(tick, 400);
      tex(cap, caption());
    }
    pick(1);
    stop(); shown = K(); set(scene(), 0);
    return { play, stop };
  };

  // ---------- 4.1 / 4.2 detection: drag the threshold ----------
  W.lrt = (root, preset) => {
    const priors = root.dataset.priors === "1";
    const C = [
      { tab: "Gaussian: N(0,1) vs N(2,1)", x0: -3.5, x1: 5.5, p0: npdf, p1: (x) => npdf(x - 2), F0: Phi, F1: (x) => Phi(x - 2), side: ">", g: 1,
        bayes: (P0, P1) => 1 + Math.log(P0 / P1) / 2, ticks: [-2, 0, 2, 4] },
      { tab: "Nov 2022: e^−y vs 2e^−2y", x0: 0, x1: 4, p0: (y) => Math.exp(-y), p1: (y) => 2 * Math.exp(-2 * y), F0: (y) => 1 - Math.exp(-y), F1: (y) => 1 - Math.exp(-2 * y), side: "<", g: 1,
        bayes: (P0, P1) => Math.log((2 * P1) / P0), ticks: [0, 1, 2, 3, 4] },
      { tab: "Jun 2026: Rayleigh σ₀=1, σ₁=2", x0: 0, x1: 7, p0: (x) => x * Math.exp(-x * x / 2), p1: (x) => (x / 4) * Math.exp(-x * x / 8), F0: (x) => 1 - Math.exp(-x * x / 2), F1: (x) => 1 - Math.exp(-x * x / 8), side: ">", g: 2,
        bayes: (P0, P1) => { const v = (4 * P0) / P1; return v > 1 ? Math.sqrt((8 / 3) * Math.log(v)) : 0; }, ticks: [0, 1, 2, 3, 4, 5, 6, 7] },
    ];
    let cur = clamp(+(root.dataset.case || 0), 0, 2), gam = C[cur].g, P1 = 0.5, stopper = null;
    const { svg, cap, bar } = shell(root, 640, 300);
    const g = S("g", {}, svg);
    const pick = tabs(bar, C.map((c) => c.tab), (i) => { cur = i; if (!priors) sg.set(C[i].g); syncRange(); draw(); });
    const sg = slider(bar, "threshold $\\gamma$", -3, 5, 0.01, gam, (v) => { gam = v; draw(); });
    const sp = slider(bar, "prior $P(H_1)$", 0.05, 0.95, 0.01, P1, (v) => { P1 = v; draw(); });
    if (priors) sg.wrap.hidden = true; else sp.wrap.hidden = true;
    btn(bar, "▶ Play", () => play(), "main");
    function syncRange() { const c = C[cur]; sg.inp.min = c.x0 + 0.01; sg.inp.max = c.x1 - 0.01; sg.set(clamp(gam, c.x0 + 0.01, c.x1 - 0.01)); }
    const X0 = 40, X1 = 440, YB = 262, YT = 52;
    // priors mode: the threshold is fixed by the prior, so dragging the line moves the prior
    // (bisection on the prior: the Bayes threshold is monotone in P1, so one prior hits the pointer)
    function priorFor(target) {
      const c = C[cur], f = (p1) => c.bayes(1 - p1, p1);
      const inc = f(0.05) < f(0.95);
      let a = 0.05, b = 0.95;
      for (let i = 0; i < 30; i++) {
        const m = (a + b) / 2;
        if ((f(m) < target) === inc) a = m; else b = m;
      }
      return clamp((a + b) / 2, 0.05, 0.95);
    }
    drag(svg, (p) => {
      if (p.x > X1 + 10) return;
      const c = C[cur];
      const target = clamp(lin(X0, X1, c.x0, c.x1)(p.x), c.x0 + 0.01, c.x1 - 0.01);
      if (priors) sp.set(+priorFor(target).toFixed(2)); else sg.set(+target.toFixed(2));
    });
    function errs(c, t) {
      const pfa = c.side === ">" ? 1 - c.F0(t) : c.F0(t);
      const pm = c.side === ">" ? c.F1(t) : 1 - c.F1(t);
      return [pfa, pm];
    }
    function draw() {
      const c = C[cur];
      const w0 = priors ? 1 - P1 : 1, w1 = priors ? P1 : 1;
      if (priors) gam = clamp(c.bayes(1 - P1, P1), c.x0, c.x1);
      g.innerHTML = "";
      const xs = grid(c.x0, c.x1, 260);
      const top = Math.max.apply(null, xs.map((x) => Math.max(w0 * c.p0(x), w1 * c.p1(x)))) * 1.08;
      const X = lin(c.x0, c.x1, X0, X1), Y = lin(0, top, YB, YT);
      const h1 = (x) => (c.side === ">" ? x > gam : x < gam);
      // decision bands
      const gx = X(gam);
      const left = c.side === ">" ? "decide H₀" : "decide H₁", right = c.side === ">" ? "decide H₁" : "decide H₀";
      S("rect", { x: X0, y: 22, width: Math.max(0, gx - X0), height: 20, class: c.side === ">" ? "f-sea" : "f-red" }, g);
      S("rect", { x: gx, y: 22, width: Math.max(0, X1 - gx), height: 20, class: c.side === ">" ? "f-red" : "f-sea" }, g);
      if (gx - X0 > 70) S("text", { x: (X0 + gx) / 2, y: 37, class: "w-t s b", "text-anchor": "middle", text: left }, g);
      if (X1 - gx > 70) S("text", { x: (gx + X1) / 2, y: 37, class: "w-t s b", "text-anchor": "middle", text: right }, g);
      // shaded error areas
      const area = (f, keep) => {
        const pts = xs.filter(keep);
        if (pts.length < 2) return null;
        return pathOf([[X(pts[0]), Y(0)]].concat(pts.map((x) => [X(x), Y(f(x))]), [[X(pts[pts.length - 1]), Y(0)]])) + " Z";
      };
      const fa = area((x) => w0 * c.p0(x), h1), mi = area((x) => w1 * c.p1(x), (x) => !h1(x));
      if (fa) S("path", { d: fa, class: "f-sea strong" }, g);
      if (mi) S("path", { d: mi, class: "f-red strong" }, g);
      axes(g, X, Y, c.x0, c.x1, 0, c.ticks.map((v) => [v, String(v)]), { name: cur === 1 ? "y" : "x" });
      S("path", { d: pathOf(xs.map((x) => [X(x), Y(w0 * c.p0(x))])), class: "c-sea" }, g);
      S("path", { d: pathOf(xs.map((x) => [X(x), Y(w1 * c.p1(x))])), class: "c-red" }, g);
      S("line", { x1: gx, x2: gx, y1: 22, y2: YB, class: "c-ink dash" }, g);
      S("circle", { cx: gx, cy: YB, r: 7, class: "dot-ink handle" }, g);
      S("text", { x: gx + 5, y: YB - 6, class: "w-t s b", text: "γ = " + fmt(gam) }, g);
      const lx = X1;
      S("text", { x: lx, y: 64, class: "w-t s b sea", "text-anchor": "end", text: (priors ? "P₀·" : "") + "p(x | H₀)" }, g);
      S("text", { x: lx, y: 80, class: "w-t s b red", "text-anchor": "end", text: (priors ? "P₁·" : "") + "p(x | H₁)" }, g);
      // ROC inset
      const RX = lin(0, 1, 478, 618), RY = lin(0, 1, 218, 78);
      S("rect", { x: RX(0), y: RY(1), width: RX(1) - RX(0), height: RY(0) - RY(1), class: "frame" }, g);
      S("line", { x1: RX(0), y1: RY(0), x2: RX(1), y2: RY(1), class: "c-grey dash thin" }, g);
      const roc = grid(c.x0, c.x1, 160).map((t) => { const [a, m] = errs(c, t); return [RX(a), RY(1 - m)]; });
      S("path", { d: pathOf(roc), class: "c-moss" }, g);
      const [pfa, pm] = errs(c, gam);
      S("circle", { cx: RX(pfa), cy: RY(1 - pm), r: 5.5, class: "dot-ink" }, g);
      S("text", { x: RX(0.5), y: RY(1) - 8, class: "w-t s b", "text-anchor": "middle", text: "ROC" }, g);
      S("text", { x: RX(0.5), y: RY(0) + 16, class: "w-t s", "text-anchor": "middle", text: "P_FA →" }, g);
      S("text", { x: RX(0) - 5, y: RY(0.5), class: "w-t s", "text-anchor": "end", text: "P_D" }, g);
      S("text", { x: 548, y: 256, class: "w-t s b sea", "text-anchor": "middle", text: "P_FA = " + fmt(pfa, 3) }, g);
      S("text", { x: 548, y: 272, class: "w-t s b red", "text-anchor": "middle", text: "P_M = " + fmt(pm, 3) + "  →  P_D = " + fmt(1 - pm, 3) }, g);
      const rule = c.side === ">" ? "x>\\gamma" : "y\\lt\\gamma";
      let t = "Decide $H_1$ when $" + rule + "$. <b>Blue area</b> $=P_{FA}=" + fmt(pfa, 3) + "$: $H_0$ was true but we said $H_1$ (it is the part of the $H_0$ curve inside the \"decide $H_1$\" zone). <b>Red area</b> $=P_M=" + fmt(pm, 3) + "$: $H_1$ was true and we missed it. $P_D=1-P_M=" + fmt(1 - pm, 3) + "$.";
      if (cur === 1) t += " Here $H_1$ is the curve that is <b>taller near 0</b>, so we decide $H_1$ for <b>small</b> $y$: the rule points left.";
      if (priors) t = "Each curve is multiplied by its prior ($P_0=" + fmt(1 - P1) + "$, $P_1=" + fmt(P1) + "$). With equal costs Bayes decides $H_1$ wherever the red hill is above the blue one: the threshold is where they <b>cross</b>, $\\gamma=" + fmt(gam) + "$. <b>Drag the crossing in the picture (or the slider)</b>: raising $P(H_1)$ moves it so that $H_1$ wins more often — a bigger prior makes $H_1$ <b>easier</b>, never harder. Error areas now total $P_e=P_0P_{FA}+P_1P_M=" + fmt((1 - P1) * pfa + P1 * pm, 3) + "$.";
      else t += " Drag the line (or the slider): pushing it to cut false alarms always adds misses. The ROC dot shows that trade-off.";
      tex(cap, t);
    }
    function stop() { if (stopper) stopper(); stopper = null; }
    function play() {
      stop();
      const c = C[cur];
      if (priors) { stopper = sweep(6000, (u) => sp.set(+(0.5 - 0.42 * Math.sin(u * 2 * Math.PI)).toFixed(2))); return; }
      const a = c.x0 + 0.15 * (c.x1 - c.x0), b = c.x1 - 0.15 * (c.x1 - c.x0);
      stopper = sweep(6500, (u) => sg.set(+(u < 0.5 ? a + (b - a) * 2 * u : b + (c.g - b) * (2 * u - 1)).toFixed(2)));
    }
    pick(cur);
    syncRange();
    return { play, stop };
  };

  // ---------- worked solutions revealed one step at a time ----------
  function steppers() {
    document.querySelectorAll(".stepper:not([data-ready])").forEach((box) => {
      box.dataset.ready = "1";
      const groups = [[]];
      [...box.children].forEach((c) => { if (c.tagName === "HR") { groups.push([]); c.remove(); } else groups[groups.length - 1].push(c); });
      const steps = groups.filter((gr) => gr.length).map((gr) => {
        const d = H("div", { class: "step" });
        gr[0].before(d);
        gr.forEach((c) => d.appendChild(c));
        return d;
      });
      if (steps.length < 2) return;
      let shown = 1;
      const bar = H("div", { class: "w-bar step-bar" }, box);
      const next = btn(bar, "", () => show(shown + 1), "main");
      const all = btn(bar, "Show all", () => show(steps.length));
      const reset = btn(bar, "Hide again", () => show(1));
      function show(n) {
        const prev = shown;
        shown = clamp(n, 1, steps.length);
        steps.forEach((s, i) => {
          s.hidden = i >= shown;
          if (i >= prev && i < shown) { s.classList.remove("in"); void s.offsetWidth; s.classList.add("in"); }
        });
        next.textContent = shown < steps.length ? "Next step (" + (shown + 1) + " of " + steps.length + ")" : "All " + steps.length + " steps shown";
        next.disabled = shown === steps.length;
        all.hidden = shown === steps.length;
        reset.hidden = shown === 1;
      }
      show(1);
    });
  }

  // ---------- true/false cards from a 3-column table: statement | T or F | why ----------
  function tfs() {
    document.querySelectorAll(".tf:not([data-ready])").forEach((box) => {
      const table = box.querySelector("table");
      if (!table) return;
      box.dataset.ready = "1";
      const list = H("div", { class: "tf-list" });
      const score = H("div", { class: "tf-score" });
      let right = 0, done = 0;
      const rows = [...table.querySelectorAll("tbody tr")];
      rows.forEach((tr) => {
        const [q, a, why] = tr.children;
        const ans = a.textContent.trim().toUpperCase().startsWith("T");
        const card = H("div", { class: "tf-card" }, list);
        const st = H("div", { class: "tf-st" }, card);
        while (q.firstChild) st.appendChild(q.firstChild);
        const btns = H("div", { class: "tf-btns" }, card);
        const res = H("div", { class: "tf-res" }, card);
        res.hidden = true;
        H("b", { text: ans ? "TRUE. " : "FALSE. " }, res);
        while (why.firstChild) res.appendChild(why.firstChild);
        ["True", "False"].forEach((lab) => {
          btn(btns, lab, () => {
            if (!res.hidden) return;
            const ok = (lab === "True") === ans;
            card.classList.add(ok ? "ok" : "no");
            res.hidden = false;
            btns.hidden = true;
            done++; if (ok) right++;
            score.textContent = right + " / " + done + " right so far (" + rows.length + " cards)";
          });
        });
      });
      score.textContent = rows.length + " cards: decide True or False, then read why.";
      table.closest(".md-typeset__scrollwrap") ? table.closest(".md-typeset__scrollwrap").replaceWith(list) : table.replaceWith(list);
      list.before(score);
    });
  }

  // ---------- boot ----------
  const io = "IntersectionObserver" in window ? new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting || e.intersectionRatio < 0.35) return;
    const r = e.target;
    io.unobserve(r);
    if (!still && r._w && r._w.play) r._w.play();
  }), { threshold: [0, 0.35] }) : null;

  function boot() {
    document.querySelectorAll(".widget[data-w]:not([data-ready])").forEach((root) => {
      const make = W[root.dataset.w];
      if (!make) return;
      root.dataset.ready = "1";
      try { root._w = make(root, root.dataset.preset) || {}; } catch (err) { console.error(err); root.textContent = "(figure failed to load)"; return; }
      // any touch of the controls takes over from the automatic play
      ["pointerdown", "keydown"].forEach((ev) => root.addEventListener(ev, () => { if (root._w.stop) root._w.stop(); }, true));
      if (io) io.observe(root);
    });
    steppers();
    tfs();
  }
  if (typeof document$ !== "undefined") document$.subscribe(boot);
  // Also run immediately: document$ may have emitted before this script loaded.
  boot();
})();
