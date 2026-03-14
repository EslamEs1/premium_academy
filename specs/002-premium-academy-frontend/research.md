# Research: Premium Academy Frontend Website

**Branch**: `002-premium-academy-frontend` | **Date**: 2026-03-14

## Research Areas

1. Tailwind CSS CDN Setup & Configuration
2. Design System (Colors, Typography, Spacing, Shadows)
3. Static Site Architecture & JavaScript Patterns
4. Image Placeholder Strategy
5. SEO & Performance Best Practices

---

## 1. Tailwind CSS CDN Setup

### Decision: Use Tailwind v3 CDN (Play CDN)

**Rationale**: The v3 CDN provides the mature `tailwind.config` JS API that allows full theme customization inline. The v4 CDN uses a different CSS-native config model (`@theme` directives) that is less documented and uses different patterns. For a static site with no build step, v3 CDN is the most practical choice.

**Alternatives considered**:
- Tailwind v4 CDN (`@tailwindcss/browser@4`): Different config syntax, less community examples, newer and less battle-tested.
- Tailwind build step (PostCSS + CLI): Would produce smaller output via purging, but adds build complexity that contradicts the "no build tools" constraint.
- No Tailwind (pure CSS): Would require far more custom CSS for the same quality, dramatically increasing development time.

### Implementation

```html
<!-- Google Fonts (load first) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- Tailwind v3 CDN with typography plugin -->
<script src="https://cdn.tailwindcss.com?plugins=typography"></script>

<!-- Inline config -->
<script>
  tailwind.config = {
    theme: {
      extend: {
        // ... custom theme values
      }
    }
  }
</script>
```

### Limitations Accepted

- No tree-shaking/purging (~350KB script loaded per page)
- Runtime CSS generation (slight FOUC possible)
- No custom JS plugins (first-party plugins only via query string)
- No IDE IntelliSense for inline config
- Explicitly not recommended by Tailwind Labs for production, but acceptable for a static demo/prototype site

### Plugin: Typography

Include the `typography` plugin via CDN query parameter for blog article prose styling:
```html
<script src="https://cdn.tailwindcss.com?plugins=typography"></script>
```

This enables the `prose` class for rich content (blog detail page).

---

## 2. Design System

### Decision: Deep Sapphire + Burnished Gold Palette

**Rationale**: The primary color `#1B3F6B` (deep sapphire navy) conveys institutional trust and authority, similar to leading universities and financial institutions. This avoids the overused SaaS blue (`#3B82F6`) and immediately differentiates from template-based sites. The accent `#E8A830` (burnished gold) evokes achievement and premium positioning, common in university crests and luxury education brands. Warm neutral grays prevent the sterile feeling of pure cool grays.

**Alternatives considered**:
- Standard blue palette (too generic, looks like every SaaS template)
- Teal/emerald palette (trendy but doesn't convey educational authority)
- Purple/violet palette (too tech-focused, less trust in education context)

### Color Palette

#### Primary (Sapphire)

| Token | Hex | Usage |
|-------|-----|-------|
| `primary-50` | `#EEF2F7` | Tinted backgrounds, hover surfaces |
| `primary-100` | `#D4DFEC` | Hover backgrounds |
| `primary-200` | `#A9BFDA` | Borders, dividers |
| `primary-300` | `#7E9FC7` | Disabled states |
| `primary-400` | `#5380B5` | Secondary text on dark |
| `primary-500` | `#2B5A8C` | Mid-weight primary |
| `primary-600` | `#1B3F6B` | **Main brand** - headings, nav, buttons |
| `primary-700` | `#142F52` | Deep hover states |
| `primary-800` | `#0E2240` | Dark backgrounds |
| `primary-900` | `#091730` | Footer, dark sections |
| `primary-950` | `#050D1C` | Near-black brand |

#### Secondary (Warm Slate)

| Token | Hex | Usage |
|-------|-----|-------|
| `secondary-50` | `#F5F3F0` | Alternate section backgrounds |
| `secondary-100` | `#E8E4DE` | Card backgrounds on colored sections |
| `secondary-200` | `#D1C9BE` | Subtle borders |
| `secondary-300` | `#B5A999` | Placeholder text |
| `secondary-400` | `#9A8E7D` | Muted icons |
| `secondary-500` | `#7A6F5F` | Body text secondary |
| `secondary-600` | `#5E5549` | Strong secondary text |

#### Accent (Burnished Gold)

| Token | Hex | Usage |
|-------|-----|-------|
| `accent-50` | `#FEF9EE` | Badge backgrounds |
| `accent-100` | `#FBF0D1` | Highlight tint |
| `accent-200` | `#F6DDA3` | Light accent borders |
| `accent-300` | `#F0C56B` | Star ratings fill |
| `accent-400` | `#E8A830` | **Primary accent** - CTAs, highlights, badges |
| `accent-500` | `#D4901A` | Hover on accent CTAs |
| `accent-600` | `#B07316` | Active/pressed accent |

#### Neutral

| Token | Hex | Usage |
|-------|-----|-------|
| `neutral-50` | `#FAFAF9` | Page background |
| `neutral-100` | `#F3F2F0` | Card backgrounds, input backgrounds |
| `neutral-150` | `#EAEAE7` | Section alternate bg |
| `neutral-200` | `#DDDCDA` | Borders, dividers |
| `neutral-300` | `#C4C3C0` | Disabled text, placeholder |
| `neutral-400` | `#A3A2A0` | Muted icons, captions |
| `neutral-500` | `#7A7977` | Secondary body text |
| `neutral-600` | `#585755` | Body text |
| `neutral-700` | `#3D3C3A` | Strong body text |
| `neutral-800` | `#262524` | Headings |
| `neutral-900` | `#171716` | Near-black text |

#### Semantic

| Token | Hex | Light Variant | Usage |
|-------|-----|---------------|-------|
| `success-50` | — | `#ECFDF3` | Success bg |
| `success-500` | `#16794A` | — | Verified, success text |
| `success-600` | `#126239` | — | Hover on success |
| `warning-50` | — | `#FFFAEB` | Warning bg |
| `warning-500` | `#C77C1A` | — | Notices |
| `warning-600` | `#A66514` | — | Hover on warning |
| `error-50` | — | `#FEF3F2` | Error bg |
| `error-500` | `#C4321C` | — | Errors, validation |
| `error-600` | `#A02917` | — | Hover on error |

### Typography

#### Decision: Playfair Display (headings) + Inter (body)

**Rationale**: Playfair Display is a transitional serif with high contrast strokes that reads as editorial, authoritative, and refined. It avoids the stiffness of traditional serifs while being far more distinctive than sans-serif-only approaches. Inter is designed specifically for screens with excellent readability at all sizes. The pairing avoids overused combinations (Poppins, Montserrat) that create immediate "template" recognition.

**Alternatives considered**:
- Poppins + Inter: Poppins is overused on educational sites
- Montserrat + Open Sans: Generic, no personality
- DM Serif Display + DM Sans: Good pairing but less established
- All-Inter (no serif): Loses the premium editorial quality

**Google Fonts URL**:
```
https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap
```

#### Type Scale (1.25 ratio - Major Third)

| Token | Element | Size | Line Height | Weight | Font | Letter Spacing |
|-------|---------|------|-------------|--------|------|----------------|
| `text-display` | Hero headline | 3.052rem (~49px) | 1.1 | 700 | Playfair Display | -0.02em |
| `text-h1` | Page titles | 2.441rem (~39px) | 1.15 | 700 | Playfair Display | -0.015em |
| `text-h2` | Section headings | 1.953rem (~31px) | 1.2 | 600 | Playfair Display | -0.01em |
| `text-h3` | Subsection heads | 1.563rem (~25px) | 1.3 | 600 | Playfair Display | 0 |
| `text-h4` | Card titles | 1.25rem (20px) | 1.4 | 600 | Inter | 0 |
| `text-body-lg` | Lead text | 1.125rem (18px) | 1.7 | 400 | Inter | 0 |
| `text-body` | Body text | 1rem (16px) | 1.7 | 400 | Inter | 0 |
| `text-body-sm` | Secondary text | 0.875rem (14px) | 1.6 | 400 | Inter | 0.01em |
| `text-caption` | Labels, meta | 0.75rem (12px) | 1.5 | 500 | Inter | 0.03em |
| `text-overline` | Overline labels | 0.75rem (12px) | 1.5 | 600 | Inter | 0.1em |

**Note**: H4 switches to Inter (body font) to prevent serif overuse on smaller headings. `text-overline` is uppercase with wide tracking, used for section labels like "OUR TEACHERS".

### Spacing Scale (4px base)

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Tight inline spacing |
| `space-2` | 8px | Icon-to-text gaps |
| `space-3` | 12px | Input padding, small gaps |
| `space-4` | 16px | Standard component gap |
| `space-5` | 20px | Card padding (mobile) |
| `space-6` | 24px | Card padding (desktop) |
| `space-8` | 32px | Between components in a section |
| `space-10` | 40px | Section sub-group spacing |
| `space-12` | 48px | Between section heading and content |
| `space-16` | 64px | Section vertical padding (mobile) |
| `space-20` | 80px | Section vertical padding (tablet) |
| `space-24` | 96px | Section vertical padding (desktop) |
| `space-32` | 128px | Hero padding, major section breaks |

#### Semantic Spacing

| Token | Maps To | Usage |
|-------|---------|-------|
| Section py (mobile) | 64px | `py-16` |
| Section py (tablet) | 80px | `md:py-20` |
| Section py (desktop) | 96px | `lg:py-24` |
| Card padding | 24px | `p-6` |
| Container max-width | 1280px | `max-w-container` |
| Container px | 16px / 24px / 32px | `px-4 md:px-6 lg:px-8` |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `rounded-sm` | 4px | Badges, tags, small pills |
| `rounded-md` | 8px | Inputs, buttons, small cards |
| `rounded-lg` | 12px | Primary cards, dropdowns, modals |
| `rounded-xl` | 16px | Feature cards, hero cards, images |
| `rounded-2xl` | 24px | Large feature sections |
| `rounded-full` | 9999px | Avatars, pill buttons |

**Design rule**: Cards use `rounded-lg` (12px) as the standard. This avoids the boxy 4px look and the toy-like 24px trend.

### Shadow / Elevation

Shadows use `rgba(27,63,107,...)` (primary navy) instead of pure black for warmer, cohesive shadows.

| Token | Value | Usage |
|-------|-------|-------|
| `shadow-sm` | `0 1px 2px 0 rgba(27,63,107,0.05)` | Input fields, inactive cards |
| `shadow-md` | `0 2px 4px -1px rgba(27,63,107,0.06), 0 4px 12px -2px rgba(27,63,107,0.08)` | Default card elevation |
| `shadow-lg` | `0 4px 8px -2px rgba(27,63,107,0.08), 0 12px 28px -4px rgba(27,63,107,0.12)` | Hovered cards, dropdowns |
| `shadow-xl` | `0 8px 16px -4px rgba(27,63,107,0.1), 0 20px 48px -8px rgba(27,63,107,0.16)` | Modals, lightboxes |

### Complete Tailwind Config

```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: {
          50:  '#EEF2F7',
          100: '#D4DFEC',
          200: '#A9BFDA',
          300: '#7E9FC7',
          400: '#5380B5',
          500: '#2B5A8C',
          600: '#1B3F6B',
          700: '#142F52',
          800: '#0E2240',
          900: '#091730',
          950: '#050D1C',
        },
        secondary: {
          50:  '#F5F3F0',
          100: '#E8E4DE',
          200: '#D1C9BE',
          300: '#B5A999',
          400: '#9A8E7D',
          500: '#7A6F5F',
          600: '#5E5549',
        },
        accent: {
          50:  '#FEF9EE',
          100: '#FBF0D1',
          200: '#F6DDA3',
          300: '#F0C56B',
          400: '#E8A830',
          500: '#D4901A',
          600: '#B07316',
        },
        neutral: {
          50:  '#FAFAF9',
          100: '#F3F2F0',
          150: '#EAEAE7',
          200: '#DDDCDA',
          300: '#C4C3C0',
          400: '#A3A2A0',
          500: '#7A7977',
          600: '#585755',
          700: '#3D3C3A',
          800: '#262524',
          900: '#171716',
        },
        success: { 50: '#ECFDF3', 500: '#16794A', 600: '#126239' },
        warning: { 50: '#FFFAEB', 500: '#C77C1A', 600: '#A66514' },
        error:   { 50: '#FEF3F2', 500: '#C4321C', 600: '#A02917' },
      },
      fontFamily: {
        display: ['"Playfair Display"', 'Georgia', 'serif'],
        body:    ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
      fontSize: {
        'display': ['3.052rem', { lineHeight: '1.1',  letterSpacing: '-0.02em',  fontWeight: '700' }],
        'h1':      ['2.441rem', { lineHeight: '1.15', letterSpacing: '-0.015em', fontWeight: '700' }],
        'h2':      ['1.953rem', { lineHeight: '1.2',  letterSpacing: '-0.01em',  fontWeight: '600' }],
        'h3':      ['1.563rem', { lineHeight: '1.3',  letterSpacing: '0',        fontWeight: '600' }],
        'h4':      ['1.25rem',  { lineHeight: '1.4',  letterSpacing: '0',        fontWeight: '600' }],
        'body-lg': ['1.125rem', { lineHeight: '1.7',  letterSpacing: '0',        fontWeight: '400' }],
        'body':    ['1rem',     { lineHeight: '1.7',  letterSpacing: '0',        fontWeight: '400' }],
        'body-sm': ['0.875rem', { lineHeight: '1.6',  letterSpacing: '0.01em',   fontWeight: '400' }],
        'caption': ['0.75rem',  { lineHeight: '1.5',  letterSpacing: '0.03em',   fontWeight: '500' }],
        'overline':['0.75rem',  { lineHeight: '1.5',  letterSpacing: '0.1em',    fontWeight: '600' }],
      },
      borderRadius: {
        'sm':   '4px',
        'md':   '8px',
        'lg':   '12px',
        'xl':   '16px',
        '2xl':  '24px',
        'full': '9999px',
      },
      boxShadow: {
        'sm':  '0 1px 2px 0 rgba(27,63,107,0.05)',
        'md':  '0 2px 4px -1px rgba(27,63,107,0.06), 0 4px 12px -2px rgba(27,63,107,0.08)',
        'lg':  '0 4px 8px -2px rgba(27,63,107,0.08), 0 12px 28px -4px rgba(27,63,107,0.12)',
        'xl':  '0 8px 16px -4px rgba(27,63,107,0.1), 0 20px 48px -8px rgba(27,63,107,0.16)',
        'none': 'none',
      },
      maxWidth: {
        'container': '1280px',
      },
    },
  },
}
```

---

## 3. Static Site Architecture

### Decision: JavaScript Injection for Shared Components

**Rationale**: In a static site without a build step or templating engine, the header and footer must appear on all 13 pages. JS injection via a shared `main.js` file is the most practical approach: it works with `file://` protocol during development, works on GitHub Pages, and keeps a single source of truth for shared components. The alternative (HTML partials loaded via `fetch()`) requires a web server and breaks during local development.

**Alternatives considered**:
- `fetch()` + HTML partials: Requires a server, breaks on `file://`, adds async complexity
- Copy-paste across 13 pages: Unmaintainable, error-prone
- Web Components (`customElements`): Adds unnecessary complexity for this scope
- Server-side includes (SSI): Requires server config, not static-file compatible

### Decision: IIFE Namespace Pattern for JavaScript

**Rationale**: ES modules (`import/export`) require `<script type="module">` which enforces CORS and breaks on `file://` protocol. The IIFE + namespace pattern (`PremiumAcademy.*`) is universally compatible, works with `defer`, and is perfectly adequate for the scope of interactions needed (mobile menu, accordion, sticky header, form validation).

**Alternatives considered**:
- ES modules: CORS issues with `file://`, adds complexity for no real benefit at this scope
- Global functions: No encapsulation, pollutes global namespace
- Class-based modules: Over-engineered for the interaction scope

### JavaScript Architecture

```
src/js/
├── main.js         # App init, header/footer injection, mobile menu, sticky header, announcement bar
├── accordion.js    # FAQ accordion behavior (reused on homepage FAQ preview)
├── filters.js      # Teachers listing filter/sort UI visual interactions
└── forms.js        # Contact form validation with data-validate attributes
```

**Loading strategy**: Use `defer` attribute on all scripts. This downloads in parallel but executes in order after DOM parsing.

```html
<script src="js/main.js" defer></script>
<script src="js/accordion.js" defer></script>
<!-- Page-specific -->
<script src="js/filters.js" defer></script>  <!-- only on teachers.html -->
<script src="js/forms.js" defer></script>     <!-- only on contact.html -->
```

### Event Delegation Pattern

Use `data-*` attributes for interactive elements and delegate events to parent containers:

```html
<div data-accordion>
  <div data-accordion-item>
    <button data-accordion-trigger>Question</button>
    <div data-accordion-content>Answer</div>
  </div>
</div>
```

---

## 4. Image Placeholder Strategy

### Decision: URL-based Placeholders During Development

**Rationale**: Using external placeholder services keeps the repo small and speeds up development. For teacher photos, `randomuser.me` provides realistic, diverse faces. For content images, specific Unsplash photo IDs (not random) ensure consistent, high-quality visuals. For generic placeholders, `placehold.co` provides branded solid-color blocks.

**Alternatives considered**:
- Downloaded local images: Bloats repo during development, requires image optimization pipeline
- Lorem Picsum (random): Inconsistent results, unprofessional for a demo
- AI-generated images: Copyright concerns, inconsistent quality, adds external dependency

### Services Used

| Service | Purpose | URL Pattern |
|---------|---------|-------------|
| randomuser.me | Teacher profile photos | `https://randomuser.me/api/portraits/men/32.jpg` |
| Unsplash (specific IDs) | Hero, course, blog images | `https://images.unsplash.com/photo-{ID}?w=800&h=400&fit=crop` |
| placehold.co | Branded placeholder blocks | `https://placehold.co/400x300/1B3F6B/ffffff?text=Course` |

### Image Loading Best Practices

- Hero image: eager load with `fetchpriority="high"`
- All other images: `loading="lazy"` and `decoding="async"`
- All images include `width` and `height` attributes to prevent layout shift
- All images include descriptive `alt` text

---

## 5. SEO & Performance

### Decision: Comprehensive SEO Structure

**Rationale**: Even though this is a static demo, proper SEO structure from the start means the site is ready for production deployment without rework. JSON-LD structured data (EducationalOrganization, Course, FAQPage) provides rich snippet eligibility. Unique title/meta per page and Open Graph tags enable proper social sharing.

### SEO Elements Per Page

1. Unique `<title>` tag with brand suffix
2. Unique `<meta name="description">`
3. `<link rel="canonical">`
4. Open Graph tags (og:title, og:description, og:image, og:url, og:type)
5. Twitter Card tags
6. JSON-LD structured data (where applicable)
7. Semantic heading hierarchy (one H1 per page)
8. Breadcrumb navigation with Schema.org markup (inner pages)
9. Descriptive anchor text (no "click here")

### JSON-LD Types by Page

| Page | Schema Type |
|------|-------------|
| Homepage | `EducationalOrganization` |
| Teacher Profile | `Person` (instructor) |
| Program Detail | `Course` |
| Blog Post | `Article` |
| FAQ | `FAQPage` |

### Performance Strategy

- Preconnect to `fonts.googleapis.com`, `fonts.gstatic.com`, `images.unsplash.com`
- Google Fonts loaded with `display=swap` to prevent FOIT
- Tailwind CDN script in `<head>` (processes before paint)
- Custom CSS after Tailwind in `<head>`
- JS files at end of `<body>` with `defer`
- Reserved min-heights for header/footer placeholders to prevent layout shift
- IntersectionObserver for scroll-triggered animations (not scroll event listeners)
- Target: <2MB total page weight, <4s above-the-fold render on 3G

---

## Icons Decision

### Decision: Inline SVGs from Heroicons

**Rationale**: Heroicons has no official CDN for direct HTML use. Inline SVGs are zero-overhead (no HTTP requests), fully stylable with Tailwind classes (color via `currentColor`, size via `w-/h-` classes), and work without JavaScript. Copy SVG markup from heroicons.com directly into HTML.

**Alternatives considered**:
- Font Awesome CDN: Heavy (~100KB), introduces another CDN dependency
- Heroicons via UNPKG: Requires fetch or build step
- Custom icon sprite: Over-engineered for this scope

### Usage Pattern

```html
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
     stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-primary-600">
  <path stroke-linecap="round" stroke-linejoin="round" d="M..." />
</svg>
```

Icon styles used: Outline (24x24) for navigation/UI, Solid (24x24) for filled states (e.g., filled star rating), Mini (20x20) for compact UI elements.
