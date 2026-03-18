(function () {
  var namespace = window.PremiumAcademy || (window.PremiumAcademy = {});
  var initialized = false;

  function callModuleInit(moduleName) {
    var module = window[moduleName];

    if (module && typeof module.init === "function") {
      module.init();
    }
  }

  function runPageInitializers() {
    if (!Array.isArray(namespace.pageInitializers)) {
      return;
    }

    namespace.pageInitializers.forEach(function (initializer) {
      if (typeof initializer === "function") {
        initializer();
      }
    });
  }

  function initFilterGroups() {
    document.querySelectorAll("[data-filter-group]").forEach(function (group) {
      var buttons = Array.from(
        group.querySelectorAll("[data-filter-button]")
      );
      var items = Array.from(
        document.querySelectorAll(
          '[data-filter-items="' + group.getAttribute("data-filter-group") + '"] [data-filter-item]'
        )
      );

      if (buttons.length === 0 || items.length === 0) {
        return;
      }

      function applyFilter(activeValue) {
        buttons.forEach(function (button) {
          var isActive =
            button.getAttribute("data-filter-button") === activeValue;

          button.classList.toggle("bg-blue-600", isActive);
          button.classList.toggle("border-blue-600", isActive);
          button.classList.toggle("text-white", isActive);
          button.classList.toggle("bg-slate-50", !isActive);
          button.classList.toggle("border-slate-200", !isActive);
          button.classList.toggle("text-slate-600", !isActive);
          button.setAttribute("aria-pressed", String(isActive));
        });

        items.forEach(function (item) {
          var tags = (item.getAttribute("data-filter-item") || "")
            .split(",")
            .map(function (tag) {
              return tag.trim();
            })
            .filter(Boolean);
          var isVisible =
            activeValue === "all" || tags.indexOf(activeValue) !== -1;

          item.classList.toggle("hidden", !isVisible);
        });
      }

      buttons.forEach(function (button) {
        button.addEventListener("click", function () {
          applyFilter(button.getAttribute("data-filter-button"));
        });
      });

      applyFilter(
        (group.querySelector('[data-filter-button][aria-pressed="true"]') ||
          buttons[0]
        ).getAttribute("data-filter-button")
      );
    });
  }

  namespace.pageInitializers = namespace.pageInitializers || [];
  namespace.registerPageInit = function (initializer) {
    if (typeof initializer === "function") {
      namespace.pageInitializers.push(initializer);
    }
  };

  namespace.init = function () {
    if (initialized) {
      return;
    }

    initialized = true;
    document.documentElement.classList.add("js");
    callModuleInit("PremiumAcademyNavigation");
    callModuleInit("PremiumAcademyAnimations");
    callModuleInit("PremiumAcademyCarousel");
    callModuleInit("PremiumAcademyAccordion");
    initFilterGroups();
    runPageInitializers();
  };

  document.addEventListener("DOMContentLoaded", function () {
    namespace.init();
  });
})();
