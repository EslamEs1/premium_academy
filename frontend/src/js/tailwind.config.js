/* global tailwind */
tailwind.config = {
  theme: {
    extend: {
      colors: {
        // Core Brand Colors - Sana Academy
        primary: {
          50: "#fcfaf6",
          100: "#f8f4eb",
          200: "#efe8d5",
          300: "#e3d2b6",
          400: "#d1b18c", // Champagne Gold / Bronze
          500: "#c2976b",
          600: "#b48154",
          700: "#966645",
          800: "#7e563e",
          900: "#664734",
          950: "#372318",
        },
        // Refined Dark Mode / Navy base
        slate: {
          50: "#f7f8f9",
          100: "#eef1f4",
          200: "#dbe1e9",
          300: "#bdc9d7",
          400: "#9baabf",
          500: "#8091a9",
          600: "#67768e",
          700: "#536074",
          800: "#465061",
          900: "#3d4554", // Base body color for dark text
          950: "#0f172a", // Oxford Navy / Sana Dark
        },
        accent: {
          light: "#e8f0fe",
          DEFAULT: "#3b82f6", // Bright academic blue for active states
          dark: "#1e3a8a",
        },
        success: {
          50: "#f0fdf4",
          500: "#22c55e",
          900: "#14532d",
        },
        danger: {
          50: "#fef2f2",
          500: "#ef4444",
          900: "#7f1d1d",
        },
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        serif: ['"Playfair Display"', "Georgia", "serif"],
      },
      fontSize: {
        xs: ["0.75rem", { lineHeight: "1.5" }],
        sm: ["0.875rem", { lineHeight: "1.5715" }],
        base: ["1rem", { lineHeight: "1.5", letterSpacing: "-0.01em" }],
        lg: ["1.125rem", { lineHeight: "1.5", letterSpacing: "-0.01em" }],
        xl: ["1.25rem", { lineHeight: "1.5", letterSpacing: "-0.01em" }],
        "2xl": ["1.5rem", { lineHeight: "1.415", letterSpacing: "-0.02em" }],
        "3xl": ["1.875rem", { lineHeight: "1.333", letterSpacing: "-0.02em" }],
        "4xl": ["2.25rem", { lineHeight: "1.2", letterSpacing: "-0.02em" }],
        "5xl": ["3rem", { lineHeight: "1.1", letterSpacing: "-0.02em" }],
        "6xl": ["3.75rem", { lineHeight: "1.05", letterSpacing: "-0.03em" }],
        "7xl": ["4.5rem", { lineHeight: "1", letterSpacing: "-0.03em" }],
      },
      spacing: {
        18: "4.5rem",
        22: "5.5rem",
        26: "6.5rem",
        30: "7.5rem",
        112: "28rem",
        128: "32rem",
        144: "36rem",
      },
      boxShadow: {
        subtle: "0 1px 2px 0 rgba(15, 23, 42, 0.03)",
        elevated:
          "0 4px 6px -1px rgba(15, 23, 42, 0.06), 0 2px 4px -2px rgba(15, 23, 42, 0.03)",
        floating:
          "0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04)",
        Sana:
          "0 20px 25px -5px rgba(15, 23, 42, 0.1), 0 8px 10px -6px rgba(15, 23, 42, 0.05)",
        "inner-light": "inset 0 2px 4px 0 rgba(255, 255, 255, 0.3)",
        focus: "0 0 0 3px rgba(194, 151, 107, 0.4)", // Primary-500 alpha
      },
      borderRadius: {
        none: "0",
        sm: "0.125rem",
        DEFAULT: "0.25rem",
        md: "0.375rem",
        lg: "0.5rem",
        xl: "0.75rem",
        "2xl": "1rem",
        "3xl": "1.5rem",
        full: "9999px",
      },
      container: {
        center: true,
        padding: {
          DEFAULT: "1rem",
          sm: "1.5rem",
          lg: "2rem",
          xl: "2.5rem",
          "2xl": "3rem",
        },
        screens: {
          sm: "640px",
          md: "768px",
          lg: "1024px",
          xl: "1280px",
          "2xl": "1440px", // Slightly wider for Sana majestic layouts
        },
      },
      animation: {
        "fade-in": "fadeIn 0.5s ease-out forwards",
        "slide-up": "slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards",
        "slide-down": "slideDown 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards",
        "pulse-slow": "pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        float: "float 6s ease-in-out infinite",
      },
      keyframes: {
        fadeIn: {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
        slideUp: {
          "0%": { opacity: "0", transform: "translateY(20px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        slideDown: {
          "0%": { opacity: "0", transform: "translateY(-20px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-10px)" },
        },
      },
      transitionTimingFunction: {
        "bounce-soft": "cubic-bezier(0.34, 1.56, 0.64, 1)",
        "ease-smooth": "cubic-bezier(0.16, 1, 0.3, 1)",
      },
    },
  },
};
