# Research: Premium Arabic Academy Website Frontend

**Branch**: `004-premium-academy-frontend`
**Date**: 2026-03-18

## Research Topics

### 1. Arabic Web Font Selection

**Decision**: Use IBM Plex Arabic as the primary typeface, loaded
via Google Fonts CDN.

**Rationale**: IBM Plex Arabic offers the widest weight range
(300–700) among freely available Arabic web fonts, excellent
screen readability at all sizes, and strong Latin fallback for
mixed Arabic/English content. It renders cleanly at 16px body
text and 54px display sizes — both critical for this project.

**Alternatives considered**:

- **Tajawal**: Good readability but fewer weights (200–900 but
  the lighter weights render too thin for body text).
- **Cairo**: Excellent Arabic rendering but slightly wider
  letterforms that consume more horizontal space in RTL layouts.
- **Dubai**: Used by Abwaab — proprietary and self-hosted.
  Not available on Google Fonts CDN.
- **Noto Kufi Arabic**: Good coverage but Kufi style is less
  appropriate for modern educational marketing — too formal.

**Implementation**: Load via Google Fonts CDN link in `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap"
  rel="stylesheet"
/>
```

Font-family declaration:

```css
font-family: "IBM Plex Sans Arabic", sans-serif;
```

### 2. Tailwind CSS Delivery Method

**Decision**: Use Tailwind CSS via CDN script tag for this phase.

**Rationale**: The project is a static frontend with no build
pipeline. The Tailwind CDN (Play CDN) provides full utility
access without requiring Node.js, PostCSS, or any build tooling.
This aligns with the constitution's requirement for zero-build
deployment and file:// protocol compatibility.

**Alternatives considered**:

- **Tailwind CLI build**: Produces optimized CSS but requires
  Node.js and a build step. Contradicts the zero-build-step
  deployment target.
- **Pre-compiled Tailwind CSS**: Only includes default utilities.
  Custom values like `text-[22px]`, `rounded-[20px]`,
  `bg-[#25D366]` would not work without JIT compilation.

**Implementation**: Include in `<head>` of every page:

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
          arabic: ["IBM Plex Sans Arabic", "sans-serif"],
        },
        colors: {
          "brand-blue": "#2563EB",
          "brand-yellow": "#FACC15",
          whatsapp: "#25D366",
        },
      },
    },
  };
</script>
```

**Note**: For production deployment, a Tailwind CLI build step
SHOULD be added to generate optimized CSS. The CDN approach is
appropriate for development and static hosting during this phase.

### 3. RTL Layout Strategy

**Decision**: Rely on native browser RTL support via `dir="rtl"`
on the `<html>` element. Use Tailwind's logical utilities
sparingly for edge cases.

**Rationale**: Modern browsers handle RTL natively when
`dir="rtl"` is set at the document root. Flexbox and grid
directions automatically reverse. `text-align` defaults to
`right`. Margins and paddings are visually mirrored. This
approach is simpler and more maintainable than explicit RTL
utility classes on every element.

**Key findings from Abwaab reference analysis**:

- Abwaab uses only 3 explicit `rtl:` utility classes across
  the entire homepage — confirming that native RTL handling
  is sufficient for the vast majority of cases.
- Physical properties (`pl`, `pr`, `left`, `right`) work
  correctly in RTL context when the document direction is set.
- `dir="ltr"` is used selectively for app store badges and
  specific English-only elements.

**Edge cases requiring explicit handling**:

- App store badge containers: `dir="ltr"`
- Floating positioned elements: Manual left/right adjustment
- CSS animations with directional transforms: Manual mirroring
- Border-radius on directional corners (e.g., only left side
  rounded): Use logical properties or `rtl:` utilities

### 4. Scroll Animation Approach

**Decision**: Use Intersection Observer API with CSS transitions
for scroll-triggered entrance animations.

**Rationale**: Intersection Observer is the modern, performant
approach for detecting when elements enter the viewport. Combined
with CSS transitions (not JS-driven animations), this provides
smooth 60fps animations without layout thrashing.

**Implementation pattern**:

```javascript
// animations.js
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1 },
);

document.querySelectorAll(".animate-on-scroll").forEach((el) => {
  observer.observe(el);
});
```

```css
/* In Tailwind custom styles or inline */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(20px);
  transition:
    opacity 0.6s ease-out,
    transform 0.6s ease-out;
}
.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}
```

**Alternatives considered**:

- **AOS library**: Adds a dependency. Constitution prohibits
  unnecessary libraries.
- **GSAP**: Overkill for simple entrance animations. Heavy
  library for minimal benefit.
- **CSS-only animations**: `@keyframes` with `animation-play-
state` — less control over when animations trigger.

### 5. Partner Logo Marquee Strategy

**Decision**: Pure CSS infinite scroll using `@keyframes`
animation and duplicated logo track.

**Rationale**: The marquee effect can be achieved entirely with
CSS, requiring zero JavaScript. This matches the observed pattern
from leading Arabic edtech platforms.

**Implementation**:

- Container: `overflow: hidden`
- Track: Double the logos (8 unique × 2 = 16 items) in a single
  flex row
- Animation: `@keyframes scroll` translating the track by 50%
  (half the duplicated width) over 16–20s, linear, infinite
- No pause on hover (clean, continuous motion)

### 6. Accordion Component Strategy

**Decision**: Native JavaScript accordion with CSS height
transitions using `max-height`.

**Rationale**: A simple accordion can be implemented with ~30
lines of JavaScript. No library needed. CSS transitions on
`max-height` provide smooth expand/collapse animation.

**Implementation pattern**:

- Click handler on question element
- Toggle `aria-expanded` attribute
- Toggle answer panel visibility via `max-height` transition
- Single-open behavior: close other open items before opening
  clicked item
- Keyboard support: Enter/Space to toggle

### 7. Mobile Menu Strategy

**Decision**: CSS-transitioned slide-out panel from the right
(RTL context) with JavaScript toggle.

**Rationale**: A slide-out sidebar provides the premium mobile
navigation experience required by the constitution. The animation
uses CSS `transform: translateX()` for GPU-accelerated performance.

**Implementation**:

- Menu panel: `position: fixed`, full height, off-screen right
  (`transform: translateX(100%)` in RTL context)
- Toggle: Add/remove `.open` class that sets
  `transform: translateX(0)`
- Backdrop: Semi-transparent overlay that fades in
- Body scroll lock when menu is open
- Close on: backdrop click, close button, Escape key

### 8. Image Placeholder Strategy

**Decision**: Use CSS gradient backgrounds as image placeholders,
with descriptive Arabic `alt` text on all `<img>` tags.

**Rationale**: The project needs realistic-looking teacher photos,
educational imagery, and partner logos without actual photography
assets. CSS gradients provide clean, professional-looking
placeholders that feel intentional rather than broken.

**Implementation**:

- Teacher avatars: Colored gradient circles with initials
- Service illustrations: SVG illustrations created inline or
  gradient containers with icon overlays
- Partner logos: Clean SVG rectangles with institution names in
  Arabic text
- Blog thumbnails: Gradient backgrounds with category-specific
  color treatment
- All `<img>` tags include `alt` in Arabic for accessibility
  and SEO

### 9. File Organization Strategy

**Decision**: Flat file structure with page-based HTML files,
shared CSS, and feature-based JS modules at the repository root
inside a `frontend/` directory.

**Rationale**: The project is a static site with 12 HTML pages.
A flat structure within `frontend/` is navigable, requires no
routing, and maps directly to the URL structure. Shared assets
are organized by type.

**Directory structure**:

```
frontend/
├── index.html
├── about.html
├── teachers.html
├── teacher-profile.html
├── how-it-works.html
├── pricing.html
├── contact.html
├── faq.html
├── blog.html
├── blog-post.html
├── terms.html
├── privacy.html
├── css/
│   └── custom.css          # Custom CSS beyond Tailwind
├── js/
│   ├── main.js             # Entry point, shared init
│   ├── navigation.js       # Header, mobile menu
│   ├── accordion.js        # FAQ accordion
│   ├── carousel.js         # Logo carousel, testimonials
│   ├── animations.js       # Scroll-triggered animations
│   └── forms.js            # Form validation
└── assets/
    ├── images/             # Placeholder images, icons
    ├── icons/              # SVG icons
    └── logos/              # Partner logos, brand logo
```

### 10. Form Validation Strategy

**Decision**: Native HTML5 form validation enhanced with
JavaScript for Arabic error messages and custom styling.

**Rationale**: HTML5 `required`, `type="email"`, `pattern`
attributes provide baseline validation without JavaScript.
JS enhances this with Arabic error messages and consistent
styling.

**Implementation**:

- HTML `required` and `type` attributes for baseline validation
- `novalidate` on `<form>` to suppress browser-default messages
- JS `submit` event handler for custom Arabic validation
- Error messages displayed below inputs in Arabic
- Visual error states: red border, error icon, error text
- Form does NOT submit (no backend) — show success message modal
