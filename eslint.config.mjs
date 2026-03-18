import htmlPlugin from "eslint-plugin-html";

export default [
  {
    ignores: [
      "node_modules/**",
      "dist/**",
      "build/**",
      "coverage/**",
      "**/*.min.js"
    ]
  },
  {
    plugins: { html: htmlPlugin },
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: {
        window: "readonly",
        document: "readonly",
        console: "readonly",
        sessionStorage: "readonly",
        IntersectionObserver: "readonly",
        setTimeout: "readonly",
        tailwind: "readonly"
      }
    },
    rules: {
      "no-unused-vars": "warn",
      "no-console": "off",
      "eqeqeq": "error"
    }
  }
];
