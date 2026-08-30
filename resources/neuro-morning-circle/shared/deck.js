(() => {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const notes = Array.from(document.querySelectorAll('[data-note]')).map((node) => node.dataset.note || '');
  const count = document.getElementById('count');
  const notePanel = document.getElementById('notes');
  let index = 0;

  const show = (next) => {
    index = Math.max(0, Math.min(slides.length - 1, next));
    slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
    count.textContent = `${index + 1} / ${slides.length}`;
    notePanel.innerHTML = notes[index] || '<strong>Teacher note:</strong> No additional note for this slide.';
  };

  const toggleNotes = () => notePanel.classList.toggle('show');
  document.getElementById('previous').addEventListener('click', () => show(index - 1));
  document.getElementById('next').addEventListener('click', () => show(index + 1));
  document.getElementById('toggle-notes').addEventListener('click', toggleNotes);

  window.addEventListener('keydown', (event) => {
    if (['ArrowRight', 'PageDown', ' '].includes(event.key)) {
      event.preventDefault();
      show(index + 1);
    } else if (['ArrowLeft', 'PageUp'].includes(event.key)) {
      event.preventDefault();
      show(index - 1);
    } else if (event.key === 'Home') {
      show(0);
    } else if (event.key === 'End') {
      show(slides.length - 1);
    } else if (event.key.toLowerCase() === 'n') {
      toggleNotes();
    }
  });

  let touchStart = null;
  window.addEventListener('touchstart', (event) => { touchStart = event.changedTouches[0].clientX; }, { passive: true });
  window.addEventListener('touchend', (event) => {
    if (touchStart === null) return;
    const delta = event.changedTouches[0].clientX - touchStart;
    if (Math.abs(delta) > 60) show(index + (delta < 0 ? 1 : -1));
    touchStart = null;
  }, { passive: true });

  show(0);
})();
