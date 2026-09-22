const menu = document.querySelector('.menu-toggle');
menu?.addEventListener('click', () => {
 const opened = menu.getAttribute('aria-expanded') !== 'true';
 menu.setAttribute('aria-expanded', String(opened));
 menu.setAttribute('aria-label', opened ? '關閉導覽' : '開啟導覽');
 document.querySelector('.site-header nav').classList.toggle('open', opened);
});
document.querySelectorAll('.site-header nav a').forEach(a => a.addEventListener('click', () => {
 document.querySelector('.site-header nav').classList.remove('open');
 menu?.setAttribute('aria-expanded', 'false');
 menu?.setAttribute('aria-label', '開啟導覽');
}));
function showDialog(dialog) { dialog.showModal(); document.body.classList.add('modal-open'); }
document.querySelectorAll('[data-line]').forEach(b => b.addEventListener('click', () => showDialog(document.getElementById('line-dialog'))));
document.querySelectorAll('dialog').forEach(dialog => {
 dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
 dialog.addEventListener('close', () => document.body.classList.remove('modal-open'));
 dialog.addEventListener('click', e => {
  const rect = dialog.getBoundingClientRect();
  if(e.target === dialog && (e.clientX < rect.left || e.clientX > rect.right || e.clientY < rect.top || e.clientY > rect.bottom)) dialog.close();
 });
});
document.querySelectorAll('[data-photo]').forEach(b => b.addEventListener('click', () => {
 const d = document.getElementById('photo-dialog');
 d.querySelector('img').src = b.dataset.photo;
 d.querySelector('img').alt = b.dataset.caption;
 d.querySelector('p').textContent = b.dataset.caption;
 showDialog(d);
}));
function activateTab(button) {
 const list = button.closest('[role=tablist]');
 list.querySelectorAll('[role=tab]').forEach(tab => {
  const active = tab === button;
  tab.setAttribute('aria-selected', String(active)); tab.tabIndex = active ? 0 : -1;
  document.getElementById(tab.dataset.tab).hidden = !active;
 });
}
document.querySelectorAll('[role=tab]').forEach(button => {
 button.addEventListener('click', () => activateTab(button));
 button.addEventListener('keydown', e => {
  const tabs = [...button.closest('[role=tablist]').querySelectorAll('[role=tab]')];
  let idx = tabs.indexOf(button);
  if(e.key === 'ArrowRight') idx = (idx + 1) % tabs.length;
  else if(e.key === 'ArrowLeft') idx = (idx - 1 + tabs.length) % tabs.length;
  else if(e.key === 'Home') idx = 0;
  else if(e.key === 'End') idx = tabs.length - 1;
  else return;
  e.preventDefault(); activateTab(tabs[idx]); tabs[idx].focus();
 });
});
