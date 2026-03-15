document.addEventListener("DOMContentLoaded", () => {
  initProgramsListing();
});

function initProgramsListing() {
  const page = document.body.dataset.page;
  if (page !== "programs-listing") {
    return;
  }

  const tabs = Array.from(document.querySelectorAll("[data-program-tab]"));
  const cards = Array.from(document.querySelectorAll("[data-program-card]"));
  const resultCount = document.getElementById("visible-program-count");
  const currentCategory = document.getElementById("current-program-category");
  const emptyState = document.getElementById("programs-empty-state");

  if (tabs.length === 0 || cards.length === 0) {
    return;
  }

  const setActiveCategory = (category) => {
    tabs.forEach((tab) => {
      const isActive = tab.dataset.programTab === category;
      tab.classList.toggle("is-active", isActive);
      tab.setAttribute("aria-pressed", isActive ? "true" : "false");
    });

    const visibleCards = [];

    cards.forEach((card) => {
      const isVisible =
        category === "all" || card.dataset.programCategory === category;
      card.classList.toggle("is-hidden", !isVisible);

      if (isVisible) {
        visibleCards.push(card);
      }
    });

    if (resultCount) {
      resultCount.textContent = String(visibleCards.length);
    }

    if (currentCategory) {
      const activeTab = tabs.find((tab) => tab.dataset.programTab === category);
      currentCategory.textContent = activeTab?.dataset.programLabel || "All";
    }

    if (emptyState) {
      emptyState.classList.toggle("hidden", visibleCards.length > 0);
    }
  };

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      setActiveCategory(tab.dataset.programTab || "all");
    });
  });

  setActiveCategory("all");
}
