# DREAMVISION — website

Plain HTML / CSS / JS. The deployable website is in `out/`. Serve that folder
with VS Code's **Live Server** extension so relative links behave as they do
when hosted.

## 1. Edit your contact details in ONE place

Open `out/assets/js/config.js`. Phone numbers, WhatsApp links, email,
addresses and social links are pulled from this file — edit it once and every
page updates:

```js
window.KNA = {
  whatsapp: "919656219376",   // digits only, country code first, no + or spaces
  phoneAustralia: "+61450719376",
  phoneMuvattupuzha: "+918157919376",
  phoneMuvattupuzhaSecondary: "+919562319376",
  phoneKannur: "+919656219376",
  phoneChristchurch: "+642102019376",
  email: "info@dreamvisionedu.au",
  addressAustralia: "...",
  addressMuvattupuzha: "...",
  addressKannur: "...",
  addressChristchurch: "...",
  hours: "Monday – Friday: 9:30 AM – 4:30 PM; Saturday: 9:30 AM – 1:00 PM",
  social: {
    facebook: "https://www.facebook.com/dreamvision",
    instagram: "https://www.instagram.com/dreamvision_education/",
    youtube: "https://www.youtube.com/@Dreamvisioneducation"
  }
};
```

Verify business addresses, hours and social profiles before relying on them
for local SEO or publishing them as official contact details.

## 2. Folder structure

```
README.md
src/                         Development helper scripts
out/                         Deployable static site
  index.html
  about.html
  career.html
  faq.html
  contact.html
  blog.html
  blog/                      Nursing pathway articles
  courses/                   Course details and score checker
  assets/
    css/style.css
    js/config.js              Contact details
    js/site.js                Navigation, forms and website assistant
    img/
```

## 3. Trust and business evidence

The About page describes service areas rather than inventing staff biographies.
The homepage does not show unsupported numeric impact claims. Add trainer
profiles, student outcomes or business metrics only when the details are
verified and any required consent is in place.

The Careers page lists no current openings. Confirm office addresses, hours
and social profiles in `out/assets/js/config.js` before using them for local
profiles or citations.

## 4. Enquiry forms and website assistant

The Contact and Career forms open WhatsApp with the submitted details
pre-filled. The visitor must tap **Send** in WhatsApp; the website cannot
send a WhatsApp message silently.

The floating website assistant gives conversational preset answers from
`out/assets/js/site.js` about courses, exam pathways, AHPRA, fees and contact
options. It uses a warm tone but identifies itself as a virtual assistant. It
does not collect enquiry details or send messages. Questions outside the
assistant's covered topics are directed to customer support.

It is a rules-based assistant, not an AI service; it does not send visitor data
to an AI provider or retain the conversation on a server. Keep its answers
aligned with the current site and official regulator information when updating
course requirements.

The site-wide cookie banner saves necessary, analytics and course-information
choices in browser local storage. Necessary storage is always enabled. The
Google Tag Manager container (`GTM-T6Q4XT9T`) is included on every page, but
its script loads only when analytics consent is enabled. Configure any tags
inside the container to respect the visitor's saved consent choices.

## 5. Colours & fonts, if you want to adjust the look

All design tokens (colours, fonts, spacing) are CSS variables at the very
top of `out/assets/css/style.css`, under `:root`. Change a value there and it
updates sitewide.

## 6. Development scripts

`src/build.py` and `src/build_pages.py` are legacy development helpers. They
do not include every current landing page and site change, so do not use them
to regenerate the production site until they have been synchronized with
`out/`. The current deployment serves the static files in `out/` directly.

## 7. Search crawling and breadcrumbs

`robots.txt` allows Googlebot and references `sitemap.xml`. The sitemap,
canonical links and structured page URLs use the `www.dreamvisionedu.au`
host to match the live site's preferred host. Each page is set to
`index,follow`.

The shared `out/assets/js/site.js` script turns the page breadcrumb trail into
accessible breadcrumb navigation and adds Schema.org `BreadcrumbList` data.
The standalone `sitemap.html` page has its own static breadcrumb markup and
structured data.

After publishing site changes, check the affected page with Google Search
Console's live URL test and submit or resubmit `https://www.dreamvisionedu.au/sitemap.xml`.
Google controls when pages are recrawled and indexed; requesting indexing
does not guarantee immediate inclusion in search results.
