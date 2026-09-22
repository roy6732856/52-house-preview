if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
 const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => { if(entry.isIntersecting) {entry.target.classList.add('is-visible');observer.unobserve(entry.target);} });
 }, {threshold: .08});
 document.querySelectorAll('[data-reveal]').forEach(el => {el.classList.add('reveal-ready');observer.observe(el);});
}
document.addEventListener('keydown', event => {
 if(event.key === 'Escape') {
  const toggle = document.querySelector('.menu-toggle');
  if(toggle?.getAttribute('aria-expanded') === 'true') {
   toggle.click();toggle.focus();
  }
 }
});
