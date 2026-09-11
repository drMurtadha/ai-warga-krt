'use strict';
let toastTimer;
function notify(message) {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.textContent = ''; }, 4000);
}
async function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    try { await navigator.clipboard.writeText(text); return; } catch (_) { /* Try legacy copy below. */ }
  }
  const active = document.activeElement;
  const field = document.createElement('textarea');
  field.value = text;
  field.setAttribute('readonly', '');
  field.style.cssText = 'position:fixed;left:-9999px;top:0';
  document.body.append(field);
  field.select();
  let copied = false;
  try { copied = document.execCommand('copy'); }
  finally { field.remove(); if (active) active.focus({preventScroll:true}); }
  if (!copied) throw new Error('Clipboard unavailable');
}
document.querySelectorAll('.copy-btn').forEach(button => {
  const original = button.textContent;
  let resetTimer;
  button.addEventListener('click', async () => {
    try {
      await copyText(button.dataset.prompt);
      button.textContent = 'Disalin ✅';
      notify('Prompt telah disalin ✅');
      clearTimeout(resetTimer);
      resetTimer = setTimeout(() => { button.textContent = original; }, 2000);
    } catch (_) { notify('Tidak dapat menyalin. Tekan lama pada teks untuk salin secara manual.'); }
  });
});
document.querySelectorAll('.answer-btn').forEach(button => {
  button.addEventListener('click', () => {
    const answer = document.getElementById(button.getAttribute('aria-controls'));
    const open = button.getAttribute('aria-expanded') !== 'true';
    answer.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
    button.textContent = open ? 'Sembunyi Jawapan' : 'Tunjuk Jawapan';
  });
});
const dialog = document.getElementById('poster-dialog');
document.getElementById('open-poster').addEventListener('click', () => {
  const poster = document.getElementById('poster-content').cloneNode(true);
  poster.removeAttribute('id');
  document.getElementById('poster-preview').replaceChildren(poster);
  dialog.showModal();
  document.body.classList.add('modal-open');
});
document.getElementById('close-poster').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => document.body.classList.remove('modal-open'));
document.getElementById('print-poster').addEventListener('click', () => window.print());
