/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./**/*.html",
    "./src/**/*.{html,js}",
    "./templates/*.html",
    "./app/templates/app/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
