(function () {
  var api = window.PremiumAcademyAnimations || {};
  var isInitialized = false;

  function revealAll(elements) {
    elements.forEach(function (element) {
      element.classList.add("visible");
    });
  }

  api.init = function () {
    var animatedElements;
    var observer;

    if (isInitialized) {
      return;
    }

    isInitialized = true;
    animatedElements = Array.from(
      document.querySelectorAll(".animate-on-scroll, .slide-left, .slide-right")
    );

    if (animatedElements.length === 0) {
      return;
    }

    if (typeof window.IntersectionObserver !== "function") {
      revealAll(animatedElements);
      return;
    }

    observer = new window.IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) {
            return;
          }

          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.1 }
    );

    animatedElements.forEach(function (element) {
      observer.observe(element);
    });
  };

  window.PremiumAcademyAnimations = api;
})();
