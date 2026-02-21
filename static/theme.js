/* =====================================================
   theme.js — Dark / Light theme toggle for teachproj
   Place in: static/theme.js
   ===================================================== */

(function () {
  // Apply saved theme immediately to avoid flash
  const saved = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);

  window.addEventListener('DOMContentLoaded', function () {
    updateToggleBtn(saved);

    // Attach click to all toggle buttons on the page
    document.querySelectorAll('.theme-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        updateToggleBtn(next);
      });
    });
  });

  function updateToggleBtn(theme) {
    document.querySelectorAll('.theme-toggle').forEach(function (btn) {
      if (theme === 'dark') {
        btn.innerHTML = '<span class="icon">☀️</span> Light Mode';
      } else {
        btn.innerHTML = '<span class="icon">🌙</span> Dark Mode';
      }
    });
  }
})();