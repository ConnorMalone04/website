/** @type {import('tailwindcss').Config} */
console.log('Tailwind config loaded!');
module.exports = {
  
  content: [
    './src/app/**/*.{js,ts,jsx,tsx}',
    './src/components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

