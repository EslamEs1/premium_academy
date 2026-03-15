document.addEventListener("DOMContentLoaded", () => {
  initTeachersMarketplace();
  initTeacherProfileReviews();
});

function initTeachersMarketplace() {
  const page = document.body.dataset.page;
  if (page !== "teachers-marketplace") {
    return;
  }

  const filtersPanel = document.getElementById("filters-panel");
  const filtersOverlay = document.getElementById("filters-overlay");
  const openFiltersButton = document.getElementById("open-filters");
  const closeFiltersButton = document.getElementById("close-filters");
  const applyFiltersButton = document.getElementById("apply-filters");
  const clearButtons = document.querySelectorAll("[data-clear-filters]");
  const filtersForm = document.getElementById("teacher-filters-form");
  const sortSelect = document.getElementById("teacher-sort");
  const sortShell = document.getElementById("sort-shell");
  const sortCurrentLabel = document.getElementById("current-sort-label");
  const resultCount = document.getElementById("visible-result-count");
  const emptyState = document.getElementById("teachers-empty-state");
  const results = document.getElementById("teachers-results");
  const cards = Array.from(document.querySelectorAll("[data-teacher-card]"));
  const activeFiltersContainer = document.getElementById("active-filters");
  const viewButtons = Array.from(
    document.querySelectorAll("[data-view-target]"),
  );
  const defaultSort = sortSelect ? sortSelect.value : "recommended";

  if (!filtersForm || !results || cards.length === 0) {
    return;
  }

  const panelOpenClasses = ["translate-x-0"];
  const panelClosedClasses = ["-translate-x-full"];
  let lastFocusedElement = null;

  const getFocusableElements = () =>
    Array.from(
      filtersPanel?.querySelectorAll(
        'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])',
      ) || [],
    ).filter(
      (element) =>
        !element.hasAttribute("hidden") &&
        element.getAttribute("aria-hidden") !== "true",
    );

  const getInputs = () =>
    Array.from(
      filtersForm.querySelectorAll(
        "input[type='checkbox'], input[type='radio']",
      ),
    );

  const syncActiveStates = () => {
    getInputs().forEach((input) => {
      const option = input.closest(".filter-option");
      if (!option) {
        return;
      }

      option.classList.toggle("is-active", input.checked);
    });
  };

  const openPanel = () => {
    if (!filtersPanel || window.innerWidth >= 1024) {
      return;
    }

    lastFocusedElement = document.activeElement;
    document.body.classList.add("filters-panel-open");
    openFiltersButton?.setAttribute("aria-expanded", "true");
    filtersPanel.setAttribute("aria-hidden", "false");
    filtersOverlay?.setAttribute("aria-hidden", "false");
    filtersOverlay?.classList.remove("hidden");
    window.requestAnimationFrame(() => {
      filtersOverlay?.classList.remove("opacity-0");
      filtersOverlay?.classList.add("opacity-100");
      filtersPanel.classList.remove(...panelClosedClasses);
      filtersPanel.classList.add(...panelOpenClasses);
    });

    window.requestAnimationFrame(() => {
      const focusableElements = getFocusableElements();
      (focusableElements[0] || filtersPanel).focus();
    });
  };

  const closePanel = (restoreFocus = true) => {
    if (!filtersPanel || window.innerWidth >= 1024) {
      return;
    }

    openFiltersButton?.setAttribute("aria-expanded", "false");
    filtersPanel.setAttribute("aria-hidden", "true");
    filtersOverlay?.setAttribute("aria-hidden", "true");
    filtersOverlay?.classList.remove("opacity-100");
    filtersOverlay?.classList.add("opacity-0");
    filtersPanel.classList.remove(...panelOpenClasses);
    filtersPanel.classList.add(...panelClosedClasses);

    window.setTimeout(() => {
      filtersOverlay?.classList.add("hidden");
      document.body.classList.remove("filters-panel-open");
    }, 300);

    if (restoreFocus && lastFocusedElement instanceof HTMLElement) {
      lastFocusedElement.focus();
    }
  };

  const readCriteria = () => {
    const formData = new window.FormData(filtersForm);

    return {
      subjects: formData.getAll("subject"),
      experienceLevels: formData.getAll("experience"),
      format: formData.get("format") || "all",
      sort: sortSelect?.value || defaultSort,
    };
  };

  const matchesFormat = (card, format) => {
    const teacherFormat = card.dataset.format;

    if (format === "all") {
      return true;
    }

    if (format === "both") {
      return teacherFormat === "both";
    }

    if (format === "online") {
      return teacherFormat === "online" || teacherFormat === "both";
    }

    if (format === "in-person") {
      return teacherFormat === "in-person" || teacherFormat === "both";
    }

    return true;
  };

  const matchesSubjects = (card, selectedSubjects) => {
    if (selectedSubjects.length === 0) {
      return true;
    }

    const teacherSubjects = (card.dataset.subjects || "").split("|");
    return selectedSubjects.some((subject) =>
      teacherSubjects.includes(subject),
    );
  };

  const matchesExperience = (card, selectedExperience) => {
    if (selectedExperience.length === 0) {
      return true;
    }

    return selectedExperience.includes(card.dataset.experience);
  };

  const buildActiveFilterChip = (text, type, value) => {
    const chip = document.createElement("span");
    chip.className = "active-filter-chip";
    chip.innerHTML = `
      <span>${text}</span>
      <button type="button" aria-label="Remove ${text}" data-filter-type="${type}" data-filter-value="${value}">
        <svg class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
      </button>
    `;

    return chip;
  };

  const renderActiveFilters = (criteria) => {
    if (!activeFiltersContainer) {
      return;
    }

    activeFiltersContainer.innerHTML = "";

    criteria.subjects.forEach((subject) => {
      const input = filtersForm.querySelector(
        `[name="subject"][value="${subject}"]`,
      );
      const label = input?.dataset.label || subject;
      activeFiltersContainer.appendChild(
        buildActiveFilterChip(label, "subject", subject),
      );
    });

    criteria.experienceLevels.forEach((experience) => {
      const input = filtersForm.querySelector(
        `[name="experience"][value="${experience}"]`,
      );
      const label = input?.dataset.label || experience;
      activeFiltersContainer.appendChild(
        buildActiveFilterChip(label, "experience", experience),
      );
    });

    if (criteria.format !== "all") {
      const input = filtersForm.querySelector(
        `[name="format"][value="${criteria.format}"]`,
      );
      const label = input?.dataset.label || criteria.format;
      activeFiltersContainer.appendChild(
        buildActiveFilterChip(label, "format", criteria.format),
      );
    }
  };

  const updateResults = () => {
    const criteria = readCriteria();
    const visibleCards = [];

    cards.forEach((card) => {
      const shouldShow =
        matchesSubjects(card, criteria.subjects) &&
        matchesExperience(card, criteria.experienceLevels) &&
        matchesFormat(card, criteria.format);

      card.classList.toggle("is-hidden", !shouldShow);

      if (shouldShow) {
        visibleCards.push(card);
      }
    });

    sortCards(criteria.sort);
    syncActiveStates();
    renderActiveFilters(criteria);

    if (resultCount) {
      resultCount.textContent = String(visibleCards.length);
    }

    if (emptyState) {
      emptyState.classList.toggle("hidden", visibleCards.length > 0);
    }

    if (sortCurrentLabel && sortSelect) {
      sortCurrentLabel.textContent =
        sortSelect.options[sortSelect.selectedIndex]?.text || "Recommended";
    }

    if (sortShell) {
      sortShell.classList.toggle("is-active", criteria.sort !== defaultSort);
    }
  };

  const sortCards = (sortValue) => {
    const sortedCards = [...cards].sort((cardA, cardB) => {
      if (sortValue === "highest-rated") {
        return Number(cardB.dataset.rating) - Number(cardA.dataset.rating);
      }

      if (sortValue === "price-low-high") {
        return Number(cardA.dataset.price) - Number(cardB.dataset.price);
      }

      if (sortValue === "price-high-low") {
        return Number(cardB.dataset.price) - Number(cardA.dataset.price);
      }

      return (
        Number(cardA.dataset.recommended) - Number(cardB.dataset.recommended)
      );
    });

    sortedCards.forEach((card) => {
      results.appendChild(card);
    });
  };

  const resetAll = () => {
    filtersForm.reset();
    if (sortSelect) {
      sortSelect.value = defaultSort;
    }
    updateResults();
  };

  const setView = (view) => {
    results.dataset.view = view;

    viewButtons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.viewTarget === view);
      button.setAttribute(
        "aria-pressed",
        button.dataset.viewTarget === view ? "true" : "false",
      );
    });
  };

  filtersForm.addEventListener("change", updateResults);
  sortSelect?.addEventListener("change", updateResults);

  openFiltersButton?.addEventListener("click", openPanel);
  closeFiltersButton?.addEventListener("click", closePanel);
  applyFiltersButton?.addEventListener("click", closePanel);
  filtersOverlay?.addEventListener("click", closePanel);

  clearButtons.forEach((button) => {
    button.addEventListener("click", resetAll);
  });

  viewButtons.forEach((button) => {
    button.addEventListener("click", () => {
      setView(button.dataset.viewTarget || "grid");
    });
  });

  activeFiltersContainer?.addEventListener("click", (event) => {
    const target = event.target.closest("[data-filter-type]");
    if (!target) {
      return;
    }

    const input = filtersForm.querySelector(
      `[name="${target.dataset.filterType}"][value="${target.dataset.filterValue}"]`,
    );

    if (!input) {
      return;
    }

    if (input.type === "radio") {
      const allOption = filtersForm.querySelector(
        '[name="format"][value="all"]',
      );
      if (allOption) {
        allOption.checked = true;
      }
    } else {
      input.checked = false;
    }

    updateResults();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closePanel();
    }

    if (
      event.key === "Tab" &&
      document.body.classList.contains("filters-panel-open") &&
      filtersPanel
    ) {
      const focusableElements = getFocusableElements();

      if (focusableElements.length === 0) {
        event.preventDefault();
        filtersPanel.focus();
        return;
      }

      const firstElement = focusableElements[0];
      const lastElement = focusableElements[focusableElements.length - 1];

      if (event.shiftKey && document.activeElement === firstElement) {
        event.preventDefault();
        lastElement.focus();
      } else if (!event.shiftKey && document.activeElement === lastElement) {
        event.preventDefault();
        firstElement.focus();
      }
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1024) {
      filtersOverlay?.classList.add("hidden");
      filtersOverlay?.classList.remove("opacity-100");
      filtersOverlay?.classList.add("opacity-0");
      filtersPanel?.classList.remove(...panelClosedClasses);
      filtersPanel?.classList.add("translate-x-0");
      document.body.classList.remove("filters-panel-open");
      openFiltersButton?.setAttribute("aria-expanded", "false");
      filtersPanel?.setAttribute("aria-hidden", "false");
      filtersOverlay?.setAttribute("aria-hidden", "true");
    } else if (
      filtersPanel &&
      !document.body.classList.contains("filters-panel-open")
    ) {
      filtersPanel.classList.remove("translate-x-0");
      filtersPanel.classList.add("-translate-x-full");
      filtersPanel.setAttribute("aria-hidden", "true");
    }
  });

  setView("grid");
  syncActiveStates();
  updateResults();
  filtersPanel?.setAttribute(
    "aria-hidden",
    window.innerWidth >= 1024 ? "false" : "true",
  );
  filtersOverlay?.setAttribute("aria-hidden", "true");
}

function initTeacherProfileReviews() {
  const page = document.body.dataset.page;
  if (page !== "teacher-profile") {
    return;
  }

  const showMoreButton = document.getElementById("show-more-reviews");
  if (!showMoreButton) {
    return;
  }

  showMoreButton.addEventListener("click", () => {
    const hiddenReviews = document.querySelectorAll(
      ".review-card-premium.is-hidden",
    );
    hiddenReviews.forEach((review) => {
      review.classList.remove("is-hidden");
    });
    showMoreButton.remove();
  });
}
