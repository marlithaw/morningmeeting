(() => {
  "use strict";

  const printButton = document.getElementById("print-document");
  const progressBar = document.getElementById("reading-progress-bar");
  const tocLinks = Array.from(document.querySelectorAll(".toc-link"));

  printButton?.addEventListener("click", () => window.print());

  function updateReadingProgress() {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const progress = scrollable > 0 ? Math.min(1, window.scrollY / scrollable) : 0;
    if (progressBar) progressBar.style.width = `${Math.round(progress * 100)}%`;
  }

  window.addEventListener("scroll", updateReadingProgress, { passive: true });
  updateReadingProgress();

  if ("IntersectionObserver" in window && tocLinks.length) {
    const linksById = new Map(tocLinks.map(link => [link.getAttribute("href")?.slice(1), link]));
    const headings = Array.from(linksById.keys()).map(id => document.getElementById(id)).filter(Boolean);
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      tocLinks.forEach(link => link.classList.toggle("active", link === linksById.get(visible.target.id)));
    }, { rootMargin: "-18% 0px -70% 0px" });
    headings.forEach(heading => observer.observe(heading));
  }
})();
