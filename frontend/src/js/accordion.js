/**
 * Sana Academy - Accordion Component
 * Handles accessible FAQ accordion behavior with smooth CSS transitions and single-open logic.
 */

document.addEventListener("DOMContentLoaded", () => {
  initAccordions();
});

function initAccordions() {
  // Find all accordion containers
  const accordionContainers = document.querySelectorAll("[data-accordion]");

  accordionContainers.forEach((container, containerIndex) => {
    // Find all accordion items within this specific container
    const items = container.querySelectorAll("[data-accordion-item]");

    items.forEach((item, itemIndex) => {
      const trigger = item.querySelector("[data-accordion-trigger]");
      const content = item.querySelector("[data-accordion-content]");
      if (!trigger || !content) return;

      const icon = trigger.querySelector(".accordion-icon"); // Expected to have a rotating SVG

      const triggerId =
        trigger.id ||
        `accordion-trigger-${containerIndex + 1}-${itemIndex + 1}`;
      const contentId =
        content.id || `accordion-panel-${containerIndex + 1}-${itemIndex + 1}`;
      trigger.id = triggerId;
      content.id = contentId;
      trigger.setAttribute("aria-controls", contentId);
      content.setAttribute("role", "region");
      content.setAttribute("aria-labelledby", triggerId);

      // Set initial state
      // If the item doesn't have the active attribute, collapse its height initially
      const isOpen = item.hasAttribute("data-accordion-active");

      if (!isOpen) {
        content.hidden = true;
        content.setAttribute("aria-hidden", "true");
        content.style.height = "0px";
        content.style.opacity = "0";
        content.style.overflow = "hidden";
        if (icon) {
          icon.style.transform = "rotate(0deg)";
        }
      } else {
        // To display an open one by default
        content.hidden = false;
        content.setAttribute("aria-hidden", "false");
        content.style.height = "auto"; // Will be measured dynamically
        content.style.opacity = "1";
        content.style.overflow = "hidden"; // Keep hidden for safety during open transitions
        if (icon) {
          icon.style.transform = "rotate(180deg)";
        }
      }

      // Keyboard accessibility
      trigger.setAttribute("tabindex", "0");
      trigger.setAttribute("aria-expanded", isOpen ? "true" : "false");

      // Interaction Handlers
      function toggleAccordion() {
        const currentlyOpen = item.hasAttribute("data-accordion-active");

        // Single-open logic: close others in the same container
        if (!currentlyOpen) {
          items.forEach((sibling) => {
            if (
              sibling !== item &&
              sibling.hasAttribute("data-accordion-active")
            ) {
              closeAccordion(sibling);
            }
          });
          openAccordion(item, content, trigger, icon);
        } else {
          closeAccordion(item);
        }
      }

      trigger.addEventListener("click", toggleAccordion);
      trigger.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          toggleAccordion();
        }
      });
    });
  });
}

function openAccordion(item, content, trigger, icon) {
  // Set states
  item.setAttribute("data-accordion-active", "");
  trigger.setAttribute("aria-expanded", "true");
  trigger.classList.add("text-primary-600");
  trigger.classList.remove("text-slate-800");
  content.hidden = false;
  content.setAttribute("aria-hidden", "false");
  window.clearTimeout(content.closeTimerId);

  // Calculate full height needed
  const scrollHeight = content.scrollHeight;

  // Animate to full height
  content.style.height = `${scrollHeight}px`;
  content.style.opacity = "1";
  if (icon) {
    icon.classList.add("rotate-180");
  }

  // After animation clears
  setTimeout(() => {
    if (item.hasAttribute("data-accordion-active")) {
      content.style.height = "auto"; // Reset to auto so it adjusts if window resizes
    }
  }, 300); // Wait for transition duration
}

function closeAccordion(item) {
  const trigger = item.querySelector("[data-accordion-trigger]");
  const content = item.querySelector("[data-accordion-content]");
  const icon = trigger.querySelector(".accordion-icon");

  // Remove states
  item.removeAttribute("data-accordion-active");
  trigger.setAttribute("aria-expanded", "false");
  trigger.classList.remove("text-primary-600");
  trigger.classList.add("text-slate-800");

  // To animate height to 0, it must be an explicit pixel value first if it was 'auto'
  const scrollHeight = content.scrollHeight;
  content.style.height = `${scrollHeight}px`;

  // Force a repaint
  content.offsetHeight;

  // Animate to 0
  content.style.height = "0px";
  content.style.opacity = "0";
  if (icon) {
    icon.classList.remove("rotate-180");
  }

  content.closeTimerId = window.setTimeout(() => {
    if (!item.hasAttribute("data-accordion-active")) {
      content.hidden = true;
      content.setAttribute("aria-hidden", "true");
    }
  }, 300);
}
