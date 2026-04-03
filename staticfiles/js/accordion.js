(function () {
  var api = window.PremiumAcademyAccordion || {};
  var isInitialized = false;

  function setItemState(item, expanded) {
    var button = item.querySelector("[data-accordion-button]");
    var panel = item.querySelector("[data-accordion-panel]");
    var icon = item.querySelector("[data-accordion-icon]");

    if (!button || !panel) {
      return;
    }

    item.setAttribute("data-open", expanded ? "true" : "false");
    button.setAttribute("aria-expanded", String(expanded));
    panel.setAttribute("aria-hidden", String(!expanded));
    panel.style.maxHeight = expanded ? panel.scrollHeight + "px" : "0px";
    panel.style.opacity = expanded ? "1" : "0";

    if (icon) {
      icon.textContent = expanded ? "−" : "+";
    }
  }

  function initAccordion(container) {
    if (!container || container.getAttribute("data-accordion-ready") === "true") {
      return;
    }

    var items = Array.from(container.querySelectorAll("[data-accordion-item]"));

    function closeOthers(activeItem) {
      items.forEach(function (item) {
        if (item !== activeItem) {
          setItemState(item, false);
        }
      });
    }

    items.forEach(function (item) {
      var button = item.querySelector("[data-accordion-button]");

      if (!button) {
        return;
      }

      setItemState(item, false);

      function handleToggle() {
        var shouldOpen = button.getAttribute("aria-expanded") !== "true";

        closeOthers(item);
        setItemState(item, shouldOpen);
      }

      button.addEventListener("click", handleToggle);
      button.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          handleToggle();
        }
      });
    });

    container.setAttribute("data-accordion-ready", "true");
  }

  api.init = function () {
    if (isInitialized) {
      document.querySelectorAll("[data-accordion]").forEach(initAccordion);
      return;
    }

    isInitialized = true;
    document.querySelectorAll("[data-accordion]").forEach(initAccordion);
  };

  window.PremiumAcademyAccordion = api;
})();
