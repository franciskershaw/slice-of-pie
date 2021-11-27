/* Give the correct profile button the navBarDropdown ID */
let mobileDropdown = document.querySelector('[data-screen="small"]');
let largerDropdown = document.querySelector('[data-screen="large"]');

if (window.innerWidth > 767) {
  largerDropdown.setAttribute('id', 'navbarDropdown');
} else {
  mobileDropdown.setAttribute('id', 'navbarDropdown');
}
window.addEventListener('resize', () => {
  if (window.innerWidth > 767) {
      mobileDropdown.removeAttribute('id', 'navbarDropdown');
      largerDropdown.setAttribute('id', 'navbarDropdown');
  } else {
      largerDropdown.removeAttribute('id', 'navbarDropdown')
      mobileDropdown.setAttribute('id', 'navbarDropdown');
  }
})

/* Source - responsive navigation bar sourced and tweaked to spec from https://www.aleksandrhovhannisyan.com/blog/responsive-navbar-without-bootstrap/ */
const navbar = document.getElementById("navigation-bar");
const navbarToggle = navbar.querySelector(".navbar-toggle");

function openMobileNavbar() {
  navbar.classList.add("opened");
  navbarToggle.setAttribute("aria-label", "Close navigation menu.");
}

function closeMobileNavbar() {
  navbar.classList.remove("opened");
  navbarToggle.setAttribute("aria-label", "Open navigation menu.");
}

navbarToggle.addEventListener("click", () => {
  if (navbar.classList.contains("opened")) {
    closeMobileNavbar();
  } else {
    openMobileNavbar();
  }
});

const navbarMenu = navbar.querySelector(".navbar-menu");
const navbarLinksContainer = navbar.querySelector(".navbar-links");

navbarLinksContainer.addEventListener("click", (clickEvent) => {
  clickEvent.stopPropagation();
});

navbarMenu.addEventListener("click", closeMobileNavbar);