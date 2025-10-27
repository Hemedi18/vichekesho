document.addEventListener('DOMContentLoaded', function() {

  // --- Theme Toggler ---
  const themeToggle = document.getElementById('theme-toggle');
  const currentTheme = localStorage.getItem('theme');

  // Function to set the theme
  const setTheme = (theme) => {
    document.body.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (theme === 'dark') {
      themeToggle.checked = true;
    } else {
      themeToggle.checked = false;
    }
  };

  // Check for saved theme in localStorage or user's OS preference
  if (currentTheme) {
    setTheme(currentTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    setTheme('dark'); // Set dark mode if it's the OS preference
  }

  // Event listener for the toggle switch
  themeToggle.addEventListener('change', () => {
    setTheme(themeToggle.checked ? 'dark' : 'light');
  });

  // --- Active Navigation Link ---
  // Get all navigation links
  const navLinks = document.querySelectorAll('header nav a');
  // Get the current URL path
  const currentPath = window.location.pathname;

  navLinks.forEach(link => {
    // If the link's href matches the current path, add the 'active' class
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });


  // --- Add Shadow to Header on Scroll ---
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    // If page is scrolled more than 10px, add a class for a stronger shadow
    // The 'scrolled' class is defined in style.css
    // It adds a more pronounced box-shadow to the header
    header.classList.toggle('scrolled', window.scrollY > 10);
  });

});