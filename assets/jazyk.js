// Přepínač jazyka v hlavičce vede na tentýž článek v druhém jazyce (cs/<slug> ↔ sk/<slug>),
// jinde na úvod druhého jazyka.
document.addEventListener("DOMContentLoaded", () => {
  const m = location.pathname.match(/^(.*\/)(cs|sk)\/([a-z0-9-]+)(\.html)?$/);
  if (!m || m[3] === "index") return;
  document.querySelectorAll(".md-select__link[hreflang]").forEach((a) => {
    if (a.hreflang !== m[2]) a.href = m[1] + a.hreflang + "/" + m[3] + (m[4] || "");
  });
});
