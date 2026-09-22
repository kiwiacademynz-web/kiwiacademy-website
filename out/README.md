# Kiwi Nurse Academy — website

Plain HTML / CSS / JS. No build step, no framework — open any `.html` file
directly, or better, serve the folder with VS Code's **Live Server**
extension so relative links behave exactly like they will once hosted.

## 1. Edit your contact details in ONE place

Open `assets/js/config.js`. Every phone number, WhatsApp link, email,
address and social link on the entire site is pulled from this file —
edit it once and every page updates:

```js
window.KNA = {
  whatsapp: "910000000000",   // digits only, country code first, no + or spaces
  phone: "+910000000000",
  phoneDisplay: "+91 00000 00000",
  email: "info@kiwinurseacademy.com",
  addressIndia: "...",
  addressNZ: "...",
  hours: "...",
  social: { instagram: "...", facebook: "...", youtube: "...", linkedin: "..." }
};
```

## 2. Folder structure

```
index.html                 Home
about.html
career.html
faq.html
contact.html
blog.html                   Blog index
blog/
  ncnz-competence-pathway-explained.html
  oet-vs-ielts-for-nurses.html
  what-happens-at-the-osce.html
courses/
  index.html                 Compare all 3 courses
  iqn-training.html
  osce-training.html
  oet-preparation.html        (has the interactive OET/IELTS score checker)
assets/
  css/style.css              Single stylesheet, everything is in here
  js/config.js                Your contact details (edit this)
  js/site.js                  Nav, forms, score-checker logic — shouldn't need editing
  img/topo.svg, favicon.svg
```

## 3. Things clearly marked as placeholders — replace before launch

Search the site for these and swap in real content:

- **Team photos & bios** — `about.html`, the "Meet the team" section
- **Testimonials** — `index.html`, the "What candidates say" section
- **Fees** — `faq.html`, the "Fees & logistics" group
- **Job openings** — `career.html`
- **Addresses** — India centre / NZ address in `config.js`
- **Social links** — real Instagram/Facebook/YouTube/LinkedIn URLs in `config.js`

## 4. The enquiry forms (Contact + Career)

Both forms currently work client-side only: on submit, they show a
confirmation message and reveal a **"Continue on WhatsApp"** button
pre-filled with the person's details. To actually receive submissions by
email or into a CRM, you'll need to either:
- point the `<form>` at a form backend (e.g. Formspree, Web3Forms), or
- wire up a small serverless function / backend endpoint.

The WhatsApp handoff works immediately with no setup, since it's just a
`wa.me` link built from `config.js`.

## 5. Colours & fonts, if you want to adjust the look

All design tokens (colours, fonts, spacing) are CSS variables at the very
top of `assets/css/style.css`, under `:root`. Change a value there and it
updates sitewide.

## 6. `src/` folder (not part of the live site)

`src/build.py` and `src/build_pages.py` are the Python scripts used to
generate these HTML files with a consistent header/footer/nav, so you
never had to hand-copy the header into 13 files. You don't need Python to
edit the site day-to-day — just edit the HTML/CSS/JS in `out/` directly
like any static site. Only touch `src/` if you want to regenerate pages
from templates instead of hand-editing HTML.
