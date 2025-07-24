document.addEventListener('DOMContentLoaded', () => {
  const tabs = document.querySelectorAll('.tab');
  const tabContents = document.querySelectorAll('.tab-content > div');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Remove active class and update aria-selected on tabs
      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });

      // Hide all tab content panels
      tabContents.forEach(tc => tc.classList.remove('active'));

      // Activate clicked tab
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      // Show associated content panel
      const target = tab.getAttribute('data-target');
      document.getElementById(target).classList.add('active');
    });
  });
});

