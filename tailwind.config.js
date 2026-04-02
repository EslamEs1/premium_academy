/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Django templates
    "./apps/templates/**/*.html",
    // frontend source files
    "./frontend/src/**/*.{html,js}",
    "./frontend/**/*.html",
    // app-level templates
    "./apps/**/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"IBM Plex Sans Arabic"', 'sans-serif'],
        arabic: ['Tajawal', 'sans-serif'],
      },
      colors: {
        // Legacy abwaab palette
        abwaab: {
          blue: '#141E46',
          ocean: '#0052CC',
          light: '#F4F7FE',
          yellow: '#FFC800',
          teal: '#00D2D3',
        },
        // Brand palette (used in Django templates)
        brand: {
          50:  '#eff6ff',
          100: '#dbeafe',
          500: '#2563eb',
          600: '#1d4ed8',
          700: '#0f3aa9',
          900: '#0f172a',
        },
        accent: {
          300: '#fde047',
          400: '#facc15',
        },
      },
      boxShadow: {
        'float': '0 20px 40px -15px rgba(0, 0, 0, 0.1)',
        'card': '0 4px 12px rgba(0,0,0,0.05)',
        'shell': '0 28px 80px rgba(15, 23, 42, 0.10)',
      }
    }
  },
  plugins: [],
}
