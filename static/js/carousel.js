(function () {
  var api = window.PremiumAcademyCarousel || {};
  var isInitialized = false;

  api.init = function () {
    if (isInitialized) {
      return;
    }

    isInitialized = true;

    document.querySelectorAll("[data-marquee-track]").forEach(function (track) {
      var duration = track.getAttribute("data-marquee-duration");

      if (duration) {
        track.style.animationDuration = duration;
      }
    });
  };

  window.PremiumAcademyCarousel = api;
})();
