# DREAMVISION — website

Plain HTML / CSS / JS. No build step, no framework — open any `.html` file
directly, or better, serve the folder with VS Code's **Live Server**
extension so relative links behave exactly like they will once hosted.

## 1. Edit your contact details in ONE place

Open `assets/js/config.js`. Every phone number, WhatsApp link, email,
address and social link on the entire site is pulled from this file —
edit it once and every page updates:

```js
window.KNA = {
  whatsapp: "919656219376",   // digits only, country code first, no + or spaces
  phoneAustralia: "+61450719376",
  phoneIndia: "+919656219376",
  email: "info@dreamvisionedu.au",
  addressAustralia: "...",
  addressMuvattupuzha: "...",
  addressKannur: "...",
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
  index.html                 Compare all 4 courses
  iqn-training.html
  osce-training.html
  oet-preparation.html        (has the interactive OET/IELTS score checker)
best-oet-training-in-kerala.html
best-iqn-training-in-kerala.html
best-osce-training-in-kerala.html
best-nclex-rn-training-in-kerala.html
assets/
  css/style.css              Single stylesheet, everything is in here
  js/config.js                Your contact details (edit this)
  js/site.js                  Nav, forms, score checker and website assistant
  img/topo.svg, logo/logo.png, favicon/*
```

## 3. Things clearly marked as placeholders — replace before launch

Search the site for these and swap in real content:

- **Team photos & bios** — `about.html`, the "Meet the team" section
- **Testimonials** — `index.html`, the "What candidates say" section
- **Fees** — `faq.html`, the "Fees & logistics" group
- **Job openings** — `career.html`
- **Addresses** — Australia, Muvattupuzha and Kannur in `config.js`
- **Social links** — real Instagram/Facebook/YouTube/LinkedIn URLs in `config.js`

## 4. Enquiry forms and website assistant

The Contact and Career forms open WhatsApp with the submitted details
pre-filled. The visitor must tap **Send** in WhatsApp; the website cannot
send a WhatsApp message silently.

The floating website assistant gives conversational preset answers from
`assets/js/site.js` about courses, exam pathways, AHPRA, fees and contact
options. It uses a warm tone but identifies itself as a virtual assistant. It
does not collect enquiry details or send messages. Questions outside the
assistant's covered topics are directed to customer support.

It is a rules-based assistant, not an AI service; it does not send visitor data
to an AI provider or retain the conversation on a server. Keep its answers
aligned with the current site and official regulator information when updating
course requirements.

The home page impact metrics count up when they become visible. Visitors who
prefer reduced motion see the final values without the animation.

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
