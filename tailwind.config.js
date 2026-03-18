/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./frontend/src/**/*.{html,js}",
    "./frontend/**/*.html"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"IBM Plex Sans Arabic"', 'sans-serif'],
      },
      colors: {
        abwaab: {
          blue: '#141E46',      // Dark indigo/navy for backgrounds/text
          ocean: '#0052CC',     // Primary ocean blue
          light: '#F4F7FE',     // Light background
          yellow: '#FFC800',    // Vibrant yellow accent
          teal: '#00D2D3',      // secondary accent
        }
      },
      boxShadow: {
        'float': '0 20px 40px -15px rgba(0, 0, 0, 0.1)',
        'card': '0 4px 12px rgba(0,0,0,0.05)',
      }
    }
  },
  plugins: [],
}
