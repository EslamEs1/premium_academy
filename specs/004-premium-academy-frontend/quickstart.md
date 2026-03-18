# Quickstart: Premium Arabic Academy Website Frontend

**Branch**: `004-premium-academy-frontend`
**Date**: 2026-03-18

## Prerequisites

- A modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- A text editor
- No build tools, Node.js, or package managers required

## Getting Started

### 1. Open the project

Navigate to the `frontend/` directory at the repository root:

```
frontend/
├── index.html          ← Homepage (start here)
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
│   └── custom.css
├── js/
│   ├── main.js
│   ├── navigation.js
│   ├── accordion.js
│   ├── carousel.js
│   ├── animations.js
│   └── forms.js
└── assets/
    ├── images/
    ├── icons/
    └── logos/
```

### 2. View in browser

Open `frontend/index.html` directly in your browser:

```bash
# Option A: Double-click index.html in your file manager

# Option B: Use a terminal
open frontend/index.html          # macOS
xdg-open frontend/index.html      # Linux
start frontend/index.html         # Windows

# Option C: Use any local server (optional, for better experience)
python3 -m http.server 8000 --directory frontend
# Then open http://localhost:8000
```

### 3. Verify the setup

When the homepage loads, verify:

- [ ] Arabic text displays correctly (right-to-left)
- [ ] IBM Plex Sans Arabic font loads (check Network tab)
- [ ] Tailwind CSS CDN loads (check Network tab)
- [ ] Scroll-triggered animations work (scroll down)
- [ ] Mobile menu works (resize to < 768px, tap menu icon)
- [ ] FAQ accordion expands/collapses (scroll to FAQ section)

### 4. Navigate between pages

All pages are linked via the header navigation and footer links.
Click any link to navigate between pages. All links are relative
(`href="teachers.html"`) so they work from the filesystem.

## Technology Stack

| Technology      | Version  | Purpose                            |
| --------------- | -------- | ---------------------------------- |
| HTML5           | —        | Page structure and semantic markup |
| CSS3            | —        | Custom styles beyond Tailwind      |
| Tailwind CSS    | v3 (CDN) | Utility-first CSS framework        |
| JavaScript      | ES2020+  | Interactive behaviors only         |
| IBM Plex Arabic | (CDN)    | Primary Arabic typeface            |

## Key Conventions

### RTL Layout

Every page uses `<html dir="rtl" lang="ar">`. All layouts,
grids, and flex directions are RTL-native. Do NOT add `text-right`
on body text — it is the default in RTL context.

### Arabic Content

All user-facing text is in Arabic. When editing content:

- Use Modern Standard Arabic (فصحى حديثة)
- Keep numbers consistent (Arabic-European: 0123456789)
- Use Saudi educational terminology (القدرات, التحصيلي, etc.)
- Currency: ر.س (Saudi Riyal)

### Modifying Styles

- Use Tailwind utility classes directly in HTML
- Custom styles go in `css/custom.css`
- Color constants defined in the Tailwind config (`<script>` in
  each page's `<head>`)

### Adding Interactivity

- Shared JavaScript modules are in `js/`
- Each module handles one feature (accordion, carousel, etc.)
- `main.js` initializes all modules
- All JS files are loaded with `defer` attribute

## Common Tasks

### Add a new teacher card

Copy an existing teacher card HTML block and update:

1. Teacher name (Arabic)
2. Subject
3. Experience years
4. Rating
5. Student count
6. Card gradient color
7. Profile link

### Add a new FAQ question

Add a new accordion item in the FAQ section:

1. Copy an existing `.faq-item` block
2. Update the question text (Arabic)
3. Update the answer text (Arabic)
4. Ensure the accordion JS handles the new item

### Add a new blog article card

Copy an existing article card and update:

1. Article title (Arabic)
2. Excerpt (Arabic)
3. Author name
4. Date
5. Category tag
6. Thumbnail gradient color

## Deployment

The site is ready for static deployment:

```bash
# GitHub Pages: push the frontend/ directory
# Netlify: set publish directory to "frontend"
# Vercel: set output directory to "frontend"
# Any web server: serve the frontend/ directory
```

No build step is required. All dependencies load from CDNs.

## Troubleshooting

**Arabic text displays left-to-right**: Check that `<html>`
tag has `dir="rtl"` and `lang="ar"`.

**Font looks wrong**: Check browser Network tab for Google Fonts
CDN request. Ensure `font-arabic` class is applied to `<body>`.

**Animations not working**: Check that `js/animations.js` is
loaded and Intersection Observer is supported in the browser.

**Mobile menu not opening**: Check that `js/navigation.js` is
loaded and the menu toggle button has the correct data attribute.

**Tailwind classes not applying**: Check that the Tailwind CDN
script tag is present in `<head>` and loads successfully.
