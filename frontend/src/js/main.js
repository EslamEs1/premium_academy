/**
 * Premium Academy - Foundation Elements
 * Handles global injection of header, footer, announcement bar, mobile menu, and sticky behaviors.
 */

document.addEventListener("DOMContentLoaded", () => {
  initFoundation();
});

function initFoundation() {
  injectAnnouncementBar();
  injectHeader();
  injectMobileMenu();
  injectFooter();

  initStickyHeader();
  initMobileMenuState();
  highlightActiveLink();
}

/**
 * Announcement Bar
 */
function injectAnnouncementBar() {
  // Check session storage to see if user dismissed it
  if (sessionStorage.getItem("announcementDismissed") === "true") {
    return;
  }

  const html = `
        <div id="announcement-bar" class="relative z-50 bg-slate-950 text-primary-50 px-4 py-3 sm:px-6 lg:px-8 text-sm font-medium transition-all duration-300 ease-smooth">
            <div class="container mx-auto flex items-center justify-between">
                <div class="flex-1 flex justify-center items-center gap-x-3 text-center">
                    <span class="flex h-5 w-5 items-center justify-center rounded-full bg-primary-500/20">
                        <svg class="h-3 w-3 text-primary-400" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                        </svg>
                    </span>
                    <p>
                        <span class="hidden sm:inline">Enrollment for the Fall 2026 Semester is now open! </span>
                        <a href="/programs.html" class="inline-block underline underline-offset-4 decoration-primary-500 hover:text-primary-300 transition-colors">
                            Explore our new curriculum &rarr;
                        </a>
                    </p>
                </div>
                <button type="button" id="dismiss-announcement" class="flex-shrink-0 -mr-2 p-2 rounded-md hover:bg-slate-800 transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="Dismiss">
                    <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
        </div>
    `;

  document.body.insertAdjacentHTML("afterbegin", html);

  const dismissBtn = document.getElementById("dismiss-announcement");
  const bar = document.getElementById("announcement-bar");
  if (dismissBtn && bar) {
    dismissBtn.addEventListener("click", () => {
      bar.style.marginTop = `-${bar.offsetHeight}px`;
      bar.style.opacity = "0";
      setTimeout(() => bar.remove(), 300);
      sessionStorage.setItem("announcementDismissed", "true");
    });
  }
}

/**
 * Global Header
 */
function injectHeader() {
  const navLinks = [
    { name: "Home", href: "index.html" },
    { name: "Teachers", href: "teachers.html" },
    { name: "Programs", href: "programs.html" },
    { name: "How It Works", href: "how-it-works.html" },
    { name: "About", href: "about.html" },
    { name: "Blog", href: "blog.html" },
    { name: "Contact", href: "contact.html" },
  ];

  const generateNavLinks = () =>
    navLinks
      .map(
        (link) => `
        <a href="${link.href}" class="nav-link text-slate-600 hover:text-slate-950 font-medium text-[15px] transition-colors relative py-2">
            ${link.name}
            <span class="absolute bottom-0 left-0 w-full h-[2px] bg-primary-500 scale-x-0 transition-transform duration-300 origin-right hover:origin-left nav-link-underline"></span>
        </a>
    `,
      )
      .join("");

  const html = `
        <header id="global-header" class="fixed w-full z-[40] transition-all duration-300 bg-white/80 backdrop-blur-xl border-b border-white/10 top-0">
            <div id="header-container" class="container mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between transition-all duration-300 ease-smooth">
                <!-- Logo -->
                <a href="index.html" class="flex items-center gap-3 group focus:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 rounded-lg p-1 -ml-1">
                    <div class="w-10 h-10 bg-slate-950 rounded-lg flex items-center justify-center text-primary-400 transition-transform duration-300 group-hover:scale-105 group-hover:rotate-3 shadow-elegant">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" />
                           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />
                        </svg>
                    </div>
                    <span class="font-serif text-xl sm:text-2xl font-bold text-slate-900 tracking-tight transition-colors group-hover:text-primary-800">Premium<span class="text-primary-600">Academy</span></span>
                </a>

                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center gap-7">
                    ${generateNavLinks()}
                </nav>

                <!-- Actions -->
                <div class="flex items-center gap-4 lg:gap-6">
                    <a href="contact.html" class="hidden lg:inline-flex items-center justify-center px-6 py-2.5 text-sm font-semibold text-white bg-slate-950 rounded-full btn-transition focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-900 shadow-elevated hover:shadow-floating">
                        Book a Free Trial
                    </a>
                    
                    <!-- Mobile Toggle -->
                    <button id="mobile-menu-toggle" type="button" class="lg:hidden p-2 -mr-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="Toggle menu" aria-expanded="false">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path class="menu-open-icon" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                            <path class="menu-close-icon hidden" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            </div>
        </header>
    `;

  // Insert after announcement bar if it exists, otherwise at top
  const announcement = document.getElementById("announcement-bar");
  if (announcement) {
    announcement.insertAdjacentHTML("afterend", html);
  } else {
    document.body.insertAdjacentHTML("afterbegin", html);
  }
}

/**
 * Mobile Navigation Menu
 */
function injectMobileMenu() {
  const navLinks = [
    { name: "Home", href: "index.html" },
    { name: "Teachers", href: "teachers.html" },
    { name: "Programs", href: "programs.html" },
    { name: "How It Works", href: "how-it-works.html" },
    { name: "About", href: "about.html" },
    { name: "FAQ", href: "faq.html" },
    { name: "Blog", href: "blog.html" },
    { name: "Contact", href: "contact.html" },
  ];

  const generateLinks = () =>
    navLinks
      .map(
        (link) => `
        <a href="${link.href}" class="mobile-nav-link block px-6 py-4 text-xl font-serif text-slate-800 hover:text-primary-600 hover:bg-slate-50 border-b border-slate-100 transition-colors">
            ${link.name}
        </a>
    `,
      )
      .join("");

  const html = `
        <div id="mobile-menu-overlay" class="fixed inset-0 z-[50] bg-slate-950/20 backdrop-blur-sm opacity-0 pointer-events-none transition-opacity duration-300" aria-hidden="true"></div>
        <div id="mobile-menu-panel" class="fixed top-0 right-0 bottom-0 z-[55] w-[85%] max-w-sm bg-white shadow-premium transform translate-x-full transition-transform duration-500 ease-smooth flex flex-col overflow-y-auto" aria-hidden="true" tabindex="-1">
            <div class="p-6 flex items-center justify-between border-b border-slate-100">
                <span class="font-serif text-xl font-bold text-slate-900">Menu</span>
                <button id="mobile-menu-close" type="button" class="p-2 -mr-2 text-slate-500 hover:text-slate-900 hover:bg-slate-100 rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="Close menu">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
            
            <nav class="flex-1 py-2">
                ${generateLinks()}
            </nav>
            
            <div class="p-6 border-t border-slate-100 bg-slate-50">
                <a href="contact.html" class="flex items-center justify-center w-full px-6 py-3.5 text-base font-semibold text-white bg-slate-950 rounded-xl hover:bg-slate-800 transition-colors shadow-elevated">
                    Book a Free Trial
                </a>
                <p class="mt-4 text-center text-xs text-slate-500">
                    Questions? Call us at <br>
                    <a href="tel:+15551234567" class="text-primary-600 font-medium hover:underline">+1 (555) 123-4567</a>
                </p>
            </div>
        </div>
    `;

  document.body.insertAdjacentHTML("beforeend", html);
}

/**
 * Mobile Menu State & Interactions
 */
function initMobileMenuState() {
  const toggle = document.getElementById("mobile-menu-toggle");
  const close = document.getElementById("mobile-menu-close");
  const overlay = document.getElementById("mobile-menu-overlay");
  const panel = document.getElementById("mobile-menu-panel");
  const body = document.body;

  if (!toggle || !panel) return;

  let isOpen = false;

  const openMenu = () => {
    isOpen = true;
    toggle.setAttribute("aria-expanded", "true");

    // Remove structural hiding
    overlay.classList.remove("pointer-events-none");

    // Trigger animations
    requestAnimationFrame(() => {
      overlay.classList.remove("opacity-0");
      overlay.classList.add("opacity-100");
      panel.classList.remove("translate-x-full");
      panel.classList.add("translate-x-0");
      panel.setAttribute("aria-hidden", "false");
    });

    // Lock background scroll
    body.style.overflow = "hidden";

    // Focus management
    panel.focus();
  };

  const closeMenu = () => {
    isOpen = false;
    toggle.setAttribute("aria-expanded", "false");

    // Reverse animations
    overlay.classList.remove("opacity-100");
    overlay.classList.add("opacity-0");
    panel.classList.remove("translate-x-0");
    panel.classList.add("translate-x-full");
    panel.setAttribute("aria-hidden", "true");

    // Restore functionality after animation
    setTimeout(() => {
      overlay.classList.add("pointer-events-none");
      body.style.overflow = "";
    }, 300); // Matches duration-300
  };

  toggle.addEventListener("click", () => (isOpen ? closeMenu() : openMenu()));
  close?.addEventListener("click", closeMenu);
  overlay?.addEventListener("click", closeMenu);

  // Escape key handling
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOpen) {
      closeMenu();
      toggle.focus(); // Return focus to toggle
    }
  });
}

/**
 * Sticky Header Logic
 * Hide on scroll down, show on scroll up. Enhanced shadow on scroll.
 */
function initStickyHeader() {
  const header = document.getElementById("global-header");
  const headerContainer = document.getElementById("header-container");
  const announcementBar = document.getElementById("announcement-bar");

  if (!header) return;

  let lastScrollY = window.scrollY;
  let ticking = false;

  const updateHeader = () => {
    const currentScrollY = window.scrollY;
    const announcementHeight = announcementBar
      ? announcementBar.offsetHeight
      : 0;

    // Passed the announcement bar threshold
    if (currentScrollY > announcementHeight) {
      header.classList.add("shadow-subtle");
      header.classList.remove("border-white/10");
      header.classList.add("border-slate-200/60");
      headerContainer.classList.remove("h-20");
      headerContainer.classList.add("h-16"); // Shrink header

      // If scrolling down, hide header (push it up)
      if (currentScrollY > lastScrollY && currentScrollY > 200) {
        // Scrolling down past 200px
        header.style.transform = `translateY(-100%)`;
      } else {
        // Scrolling up
        header.style.transform = `translateY(0)`;
        // Fix position to top if we scrolled away from announcement
        if (announcementBar && header.style.position !== "fixed") {
          header.style.top = "0";
        }
      }
    } else {
      // Top of page
      header.classList.remove("shadow-subtle");
      header.classList.add("border-white/10");
      header.classList.remove("border-slate-200/60");
      headerContainer.classList.add("h-20");
      headerContainer.classList.remove("h-16");
      header.style.transform = `translateY(0)`;

      // Adjust position relative to announcement bar
      if (announcementBar) {
        // It stays below naturally if it's relative, but since it's fixed:
        // Wait, CSS approach: usually header top is 0. If announcement exists, it covers the top.
        // Actually, best to let the header take its natural top.
      }
    }

    lastScrollY = currentScrollY;
    ticking = false;
  };

  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        window.requestAnimationFrame(updateHeader);
        ticking = true;
      }
    },
    { passive: true },
  );

  // Initial call
  updateHeader();
}

/**
 * Global Footer
 */
function injectFooter() {
  const html = `
        <footer class="bg-slate-950 text-slate-300 pt-20 pb-10 border-t-4 border-primary-600 mt-auto">
            <div class="container mx-auto px-4 sm:px-6 lg:px-8">
                
                <!-- Main Footer Content -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-8 xl:gap-12 mb-16">
                    
                    <!-- Brand & Newsletter -->
                    <div class="lg:col-span-4 max-w-sm">
                        <a href="index.html" class="flex items-center gap-2 mb-6 focus:outline-none">
                            <div class="w-8 h-8 bg-slate-800 rounded flex items-center justify-center text-primary-400">
                                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" />
                                   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                                </svg>
                            </div>
                            <span class="font-serif text-2xl font-bold text-white tracking-tight">Premium<span class="text-primary-500">Academy</span></span>
                        </a>
                        <p class="text-slate-400 text-sm leading-relaxed mb-6">
                            Empowering students globally with world-class education. Discover experts in mathematics, languages, technology and more through personalized learning formats.
                        </p>
                        
                        <form class="flex flex-col sm:flex-row gap-2" onsubmit="event.preventDefault(); alert('Subscribed!');">
                            <label for="newsletter-email" class="sr-only">Email address</label>
                            <input id="newsletter-email" type="email" required placeholder="Enter your email" 
                                class="w-full bg-slate-900 border border-slate-800 text-white rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-primary-500 focus:ring-1 focus:ring-primary-500 transition-colors placeholder-slate-500">
                            <button type="submit" class="flex-shrink-0 px-5 py-2.5 bg-primary-600 text-white text-sm font-medium rounded-lg hover:bg-primary-500 transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-slate-950 focus:ring-primary-500">
                                Subscribe
                            </button>
                        </form>
                    </div>

                    <!-- Fast Links Grid -->
                    <div class="lg:col-span-8 grid grid-cols-2 md:grid-cols-4 gap-8">
                        <div>
                            <h3 class="text-white font-serif font-semibold mb-4 text-base">Explore</h3>
                            <ul class="space-y-3">
                                <li><a href="index.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Home</a></li>
                                <li><a href="about.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">About Us</a></li>
                                <li><a href="teachers.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Find a Teacher</a></li>
                                <li><a href="programs.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Programs</a></li>
                            </ul>
                        </div>
                        
                        <div>
                            <h3 class="text-white font-serif font-semibold mb-4 text-base">Learn</h3>
                            <ul class="space-y-3">
                                <li><a href="how-it-works.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">How It Works</a></li>
                                <li><a href="blog.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Blog</a></li>
                                <li><a href="faq.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">FAQ</a></li>
                                <li><a href="#" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Student Success</a></li>
                            </ul>
                        </div>

                        <div>
                            <h3 class="text-white font-serif font-semibold mb-4 text-base">Support</h3>
                            <ul class="space-y-3">
                                <li><a href="contact.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Contact Us</a></li>
                                <li><a href="#" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Help Center</a></li>
                                <li><a href="#" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">For Teachers</a></li>
                                <li>
                                    <span class="flex items-center text-sm text-slate-400">
                                        <svg class="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                        </svg>
                                        hello@premium.edu
                                    </span>
                                </li>
                            </ul>
                        </div>

                        <div>
                            <h3 class="text-white font-serif font-semibold mb-4 text-base">Legal</h3>
                            <ul class="space-y-3">
                                <li><a href="privacy-policy.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Privacy Policy</a></li>
                                <li><a href="terms-of-service.html" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Terms of Service</a></li>
                                <li><a href="#" class="text-sm text-slate-400 hover:text-primary-400 transition-colors">Cookie Settings</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Bottom Footer -->
                <div class="pt-8 border-t border-slate-800 flex flex-col md:flex-row items-center justify-between gap-4">
                    <p class="text-slate-500 text-sm">
                        &copy; ${new Date().getFullYear()} Premium Academy. All rights reserved.
                    </p>
                    
                    <!-- Social Links -->
                    <div class="flex items-center gap-4">
                        <a href="#" class="w-8 h-8 rounded bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:border-slate-600 transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="Twitter">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg>
                        </a>
                        <a href="#" class="w-8 h-8 rounded bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:border-slate-600 transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="Facebook">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"/></svg>
                        </a>
                        <a href="#" class="w-8 h-8 rounded bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:border-slate-600 transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="Instagram">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd"/></svg>
                        </a>
                        <a href="#" class="w-8 h-8 rounded bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:border-slate-600 transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="LinkedIn">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd"/></svg>
                        </a>
                    </div>
                </div>

            </div>
        </footer>
    `;

  document.body.insertAdjacentHTML("beforeend", html);
}

/**
 * Determine and highlight Active Link based on pathname
 */
function highlightActiveLink() {
  const path = window.location.pathname;
  // Map current path to a filename. Default to index.html if pointing at root
  const currentName = path.substring(path.lastIndexOf("/") + 1) || "index.html";

  const links = document.querySelectorAll(".nav-link, .mobile-nav-link");
  links.forEach((link) => {
    const linkHref = link.getAttribute("href");
    if (linkHref === currentName) {
      // Desktop logic
      if (link.classList.contains("nav-link")) {
        link.classList.add("text-primary-600");
        const underline = link.querySelector(".nav-link-underline");
        if (underline) {
          underline.classList.remove("scale-x-0");
          underline.classList.add("scale-x-100");
        }
      }
      // Mobile logic
      else {
        link.classList.add(
          "text-primary-600",
          "bg-slate-50",
          "border-l-4",
          "border-primary-600",
        );
        link.classList.remove("pl-6");
        link.classList.add("pl-5"); // Adjust padding for border
      }
    }
  });
}
