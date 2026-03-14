# Quickstart: Sana Academy Frontend Website

**Branch**: `002-Sana-academy-frontend` | **Date**: 2026-03-14

## Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- A text/code editor (VS Code recommended)
- No build tools, Node.js, or package managers required

## Project Structure

```
src/
├── css/
│   └── custom.css               # Custom CSS (transitions, animations, overrides)
├── js/
│   ├── main.js                  # Shared: header/footer injection, mobile menu, sticky header, announcement bar
│   ├── accordion.js             # FAQ accordion behavior
│   ├── filters.js               # Teachers listing filter/sort UI
│   └── forms.js                 # Contact form validation
├── images/                      # Local images (favicon, logo, SVG assets)
├── index.html                   # Homepage
├── about.html                   # About page
├── teachers.html                # Teachers listing
├── teacher-profile.html         # Teacher profile (demo)
├── programs.html                # Programs listing
├── program-detail.html          # Program detail (demo)
├── how-it-works.html            # How It Works
├── contact.html                 # Contact page
├── faq.html                     # FAQ page
├── blog.html                    # Blog listing
├── blog-post.html               # Blog post (demo)
├── privacy-policy.html          # Privacy Policy
└── terms-of-service.html        # Terms of Service
```

## Running Locally

### Option 1: Open Files Directly (Simplest)

Double-click any `.html` file in the `src/` directory to open it in your browser. All features work with `file://` protocol, including:
- Header/footer injection via JS
- Mobile menu
- Accordion
- Form validation
- Sticky header

### Option 2: Local Server (Recommended for Development)

Using Python (pre-installed on macOS/Linux):
```bash
cd src/
python3 -m http.server 8000
# Open http://localhost:8000
```

Using Node.js (if available):
```bash
npx serve src/
# Open http://localhost:3000
```

Using VS Code:
- Install the "Live Server" extension
- Right-click any `.html` file and select "Open with Live Server"

## Technology Stack

| Technology | Version | Delivery | Purpose |
|------------|---------|----------|---------|
| HTML5 | — | Source files | Page structure, semantic markup |
| CSS3 | — | Source files + `custom.css` | Custom styles beyond Tailwind |
| Tailwind CSS | v3 | CDN (`cdn.tailwindcss.com`) | Utility-first styling |
| Tailwind Typography | v3 | CDN plugin (`?plugins=typography`) | Blog article prose styling |
| JavaScript | ES2020+ | Source files | Interactive behaviors |
| Google Fonts | — | CDN | Inter (body) + Playfair Display (headings) |
| Heroicons | v2 | Inline SVGs | Icon system |

## External CDN Dependencies

Every HTML page includes these in `<head>`:

```html
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- Tailwind CSS v3 CDN with Typography plugin -->
<script src="https://cdn.tailwindcss.com?plugins=typography"></script>

<!-- Tailwind Theme Config -->
<script src="js/tailwind-config.js"></script>

<!-- Custom CSS -->
<link rel="stylesheet" href="css/custom.css">
```

And these before `</body>`:

```html
<!-- Shared JS -->
<script src="js/main.js" defer></script>

<!-- Page-specific JS (only where needed) -->
<script src="js/accordion.js" defer></script>
```

## Design System Quick Reference

### Colors

| Role | Class Prefix | Primary Value |
|------|-------------|---------------|
| Brand primary | `primary-600` | `#1B3F6B` (deep sapphire) |
| Brand accent | `accent-400` | `#E8A830` (burnished gold) |
| Neutral bg | `neutral-50` | `#FAFAF9` |
| Body text | `neutral-600` | `#585755` |
| Headings | `neutral-800` | `#262524` |

### Typography

| Element | Classes |
|---------|---------|
| Hero heading | `font-display text-display text-neutral-800` |
| Page H1 | `font-display text-h1 text-neutral-800` |
| Section H2 | `font-display text-h2 text-neutral-800` |
| Body text | `font-body text-body text-neutral-600` |
| Overline label | `font-body text-overline uppercase text-primary-500 tracking-widest` |

### Component Patterns

| Component | Key Classes |
|-----------|-------------|
| Primary button | `bg-primary-600 hover:bg-primary-700 text-white rounded-md px-6 py-3 font-body font-semibold shadow-sm transition-colors` |
| Secondary button | `border border-primary-600 text-primary-600 hover:bg-primary-50 rounded-md px-6 py-3 font-body font-semibold transition-colors` |
| Accent CTA | `bg-accent-400 hover:bg-accent-500 text-primary-900 rounded-md px-6 py-3 font-body font-bold shadow-sm transition-colors` |
| Card | `bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow` |
| Section padding | `py-16 md:py-20 lg:py-24` |
| Container | `max-w-container mx-auto px-4 md:px-6 lg:px-8` |
| Input field | `bg-neutral-100 border border-neutral-200 rounded-md px-4 py-3 text-body font-body text-neutral-700 focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-colors` |

## Page-by-Page Build Order

Recommended implementation sequence:

1. **Foundation** (shared components): `main.js` with header/footer, `custom.css`, `tailwind-config.js`
2. **Homepage** (`index.html`): All 10 sections, establishes all component patterns
3. **Teachers listing** (`teachers.html`): Teacher cards, filter/sort UI
4. **Teacher profile** (`teacher-profile.html`): Sticky sidebar, reviews
5. **Programs listing** (`programs.html`): Course cards, category tabs
6. **Program detail** (`program-detail.html`): Full detail layout
7. **How It Works** (`how-it-works.html`): Step-by-step process
8. **About** (`about.html`): Academy story sections
9. **Contact** (`contact.html`): Form with validation
10. **FAQ** (`faq.html`): Full categorized accordion
11. **Blog listing** (`blog.html`): Article cards
12. **Blog post** (`blog-post.html`): Article layout with prose
13. **Legal pages** (`privacy-policy.html`, `terms-of-service.html`): Structured content

## Testing Checklist

- [ ] All 13 pages load without errors in browser console
- [ ] Header and footer render consistently on every page
- [ ] Mobile menu opens/closes correctly on mobile viewport
- [ ] Sticky header behavior works on scroll
- [ ] FAQ accordion expands/collapses with smooth transitions
- [ ] Contact form validates required fields and email format
- [ ] All pages are responsive at 320px, 768px, 1024px, 1280px
- [ ] Keyboard navigation (Tab, Enter, Escape) works on interactive elements
- [ ] No horizontal scrolling on any page at any breakpoint
- [ ] Images have alt text
- [ ] Each page has a unique `<title>` tag
- [ ] Lighthouse accessibility score is 90+ on all pages

## Deployment

The site can be deployed as static files to:
- **GitHub Pages**: Push `src/` contents to the `gh-pages` branch root
- **Netlify/Vercel**: Point build directory to `src/` with no build command
- **Any static file host**: Upload contents of `src/` to the server root

No build step, compilation, or server-side configuration required.
