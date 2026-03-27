(function () {
  var api = window.PremiumAcademyNavigation || {};
  var isInitialized = false;
  var isMenuOpen = false;
  var lastFocusedElement = null;

  function getElements() {
    return {
      header: document.querySelector("[data-site-header]"),
      menuButton: document.querySelector("[data-menu-toggle]"),
      menuCloseButton: document.querySelector("[data-menu-close]"),
      menuPanel: document.querySelector("[data-mobile-menu]"),
      backdrop: document.querySelector("[data-menu-backdrop]")
    };
  }

  function getPageName(pathValue) {
    var cleanPath = (pathValue || "").split("#")[0].split("?")[0];
    var segments = cleanPath.split("/").filter(Boolean);

    if (segments.length === 0) {
      return "index.html";
    }

    return segments[segments.length - 1];
  }

  function getLinkTarget(href) {
    if (
      !href ||
      href.indexOf("http://") === 0 ||
      href.indexOf("https://") === 0 ||
      href.indexOf("mailto:") === 0 ||
      href.indexOf("tel:") === 0 ||
      href.indexOf("whatsapp:") === 0 ||
      href.charAt(0) === "#"
    ) {
      return "";
    }

    return getPageName(href);
  }

  function syncHeaderShadow() {
    var elements = getElements();

    if (!elements.header) {
      return;
    }

    elements.header.classList.toggle("shadow-md", window.scrollY > 10);
  }

  function syncActiveLinks() {
    var currentPage = getPageName(window.location.pathname);
    var links = document.querySelectorAll("[data-nav-link]");

    links.forEach(function (link) {
      var linkTarget = getLinkTarget(link.getAttribute("href"));
      var isActive = linkTarget !== "" && linkTarget === currentPage;

      link.classList.toggle("nav-link-active", isActive);
      link.classList.toggle(
        "mobile-nav-link-active",
        isActive && link.getAttribute("data-nav-type") === "mobile"
      );

      if (isActive) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  function setMenuState(nextOpenState) {
    var elements = getElements();

    if (
      !elements.menuButton ||
      !elements.menuPanel ||
      !elements.backdrop
    ) {
      return;
    }

    isMenuOpen = nextOpenState;
    lastFocusedElement =
      nextOpenState &&
      document.activeElement &&
      typeof document.activeElement.focus === "function"
        ? document.activeElement
        : lastFocusedElement;

    elements.menuButton.setAttribute("aria-expanded", String(nextOpenState));
    elements.menuPanel.setAttribute("aria-hidden", String(!nextOpenState));
    elements.menuPanel.classList.toggle("translate-x-0", nextOpenState);
    elements.menuPanel.classList.toggle("translate-x-full", !nextOpenState);
    elements.backdrop.classList.toggle("opacity-0", !nextOpenState);
    elements.backdrop.classList.toggle("pointer-events-none", !nextOpenState);
    document.body.classList.toggle("overflow-hidden", nextOpenState);

    if (nextOpenState && elements.menuCloseButton) {
      elements.menuCloseButton.focus();
    } else if (!nextOpenState && lastFocusedElement) {
      lastFocusedElement.focus();
      lastFocusedElement = null;
    }
  }

  function toggleMenu() {
    setMenuState(!isMenuOpen);
  }

  function closeMenu() {
    setMenuState(false);
  }

  function handleDocumentKeydown(event) {
    if (event.key === "Escape" && isMenuOpen) {
      closeMenu();
    }
  }

  function handleResize() {
    if (window.innerWidth >= 768 && isMenuOpen) {
      closeMenu();
    }
  }

  function bindMenuLinks() {
    var menuLinks = document.querySelectorAll("[data-mobile-menu] a[href]");

    menuLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        closeMenu();
      });
    });
  }

  api.init = function () {
    var elements;

    if (isInitialized) {
      syncHeaderShadow();
      syncActiveLinks();
      return;
    }

    isInitialized = true;
    elements = getElements();

    syncHeaderShadow();
    syncActiveLinks();

    window.addEventListener("scroll", syncHeaderShadow, { passive: true });
    window.addEventListener("resize", handleResize, { passive: true });
    document.addEventListener("keydown", handleDocumentKeydown);

    if (elements.menuButton) {
      elements.menuButton.addEventListener("click", toggleMenu);
    }

    if (elements.menuCloseButton) {
      elements.menuCloseButton.addEventListener("click", closeMenu);
    }

    if (elements.backdrop) {
      elements.backdrop.addEventListener("click", closeMenu);
    }

    bindMenuLinks();
    closeMenu();
  };

  window.PremiumAcademyNavigation = api;
})();
