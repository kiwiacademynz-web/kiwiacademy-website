#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the static Kiwi Nurse Academy site into out/.
Plain HTML/CSS/JS output — this script is only a dev-time convenience
so the header/footer/nav stay identical across every page.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")

SITE_NAME = "Kiwi Nurse Academy"

# ---------------------------------------------------------------- nav model
NAV = [
    ("index.html", "Home", None),
    ("courses/index.html", "Courses", [
        ("courses/iqn-training.html", "IQN Training", "Pearson VUE theory exam prep"),
        ("courses/osce-training.html", "OSCE Training", "Clinical stations, simulation lab"),
        ("courses/oet-preparation.html", "OET Preparation", "All 4 sub-tests, NCNZ bands"),
    ]),
    ("about.html", "About Us", None),
    ("blog.html", "Blog", None),
    ("career.html", "Career", None),
    ("faq.html", "FAQ", None),
    ("contact.html", "Contact", None),
]

ICONS = {
    "whatsapp": '<svg class="icon icon--fill" viewBox="0 0 32 32" aria-hidden="true"><path d="M16.02 3C9.1 3 3.5 8.6 3.5 15.52c0 2.5.68 4.83 1.87 6.84L3 29l6.83-2.3a12.4 12.4 0 0 0 6.19 1.65h.01c6.92 0 12.52-5.6 12.52-12.52C28.55 8.9 22.94 3 16.02 3zm7.35 17.7c-.31.87-1.8 1.67-2.48 1.76-.63.09-1.44.13-2.32-.15-.53-.17-1.22-.4-2.1-.78-3.71-1.6-6.14-5.34-6.32-5.59-.19-.25-1.52-2.02-1.52-3.86 0-1.83.96-2.73 1.3-3.1.34-.37.75-.46 1-.46.25 0 .5 0 .72.01.23.01.54-.09.84.64.31.75 1.06 2.58 1.15 2.77.09.19.15.41.03.66-.12.25-.19.4-.37.62-.19.22-.4.49-.56.66-.19.19-.38.4-.16.78.22.38.97 1.6 2.09 2.6 1.43 1.28 2.64 1.68 3.02 1.87.38.19.6.16.83-.09.22-.25.94-1.09 1.19-1.47.25-.38.5-.31.84-.19.34.13 2.17 1.02 2.54 1.21.37.19.62.28.71.44.09.16.09.9-.22 1.77z"/></svg>',
    "phone": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.2 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1L6.6 10.8z"/></svg>',
    "mail": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1z"/><path d="M3.5 7 12 13l8.5-6"/></svg>',
    "pin": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-7.4 7-12.5A7 7 0 0 0 5 9.5C5 14.6 12 22 12 22z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "clock": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
    "check-circle": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/></svg>',
    "menu": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
    "chevron": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    "insta": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1"/></svg>',
    "fb": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 21v-7h2.4l.4-3H14V9c0-.9.2-1.5 1.6-1.5H17V4.8c-.3 0-1.2-.1-2.2-.1-2.3 0-3.8 1.4-3.8 3.9V11H8.6v3H11v7h3z"/></svg>',
    "yt": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="4"/><path d="M10.5 9.5l5 2.5-5 2.5z" fill="currentColor" stroke="none"/></svg>',
    "linkedin": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M8 10.5V17M8 7.5v.01M12 17v-4c0-1.4.9-2.3 2.2-2.3 1.3 0 2 .9 2 2.3V17"/></svg>',
}


def icon(name):
    return ICONS[name]


def nav_html(base, current):
    """base = '' for root pages, '../' for one level deep."""
    out = []
    for href, label, sub in NAV:
        full = base + href
        is_current = current == href
        if sub:
            is_active_section = any(current == s[0] for s in sub)
            out.append(
                '<div class="has-sub">'
                '<button class="nav__btn" type="button" aria-expanded="false" aria-current="{cur}">{label} {chev}</button>'
                '<div class="sub">'.format(
                    cur="true" if is_active_section else "false",
                    label=label, chev=icon("chevron"),
                )
            )
            out.append('<a href="{href}">{label}<small>{d}</small></a>'.format(href=base + "courses/index.html", label="All courses", d="Compare IQN, OSCE and OET"))
            for shref, slabel, sdesc in sub:
                out.append('<a href="{href}">{label}<small>{d}</small></a>'.format(href=base + shref, label=slabel, d=sdesc))
            out.append('</div></div>')
        else:
            out.append('<a href="{href}"{cur}>{label}</a>'.format(
                href=full, label=label,
                cur=' aria-current="page"' if is_current else ""))
    return "\n".join(out)


def head(title, desc, base, canonical):
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://kiwinurseacademy.com/{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="{site}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
""".format(title=title, desc=desc, base=base, canonical=canonical, site=SITE_NAME)


def header(base, current):
    return """<header class="topbar">
  <div class="wrap">
    <span class="topbar__tagline">Kerala &amp; Aotearoa New Zealand &middot; Registered-nurse pathway specialists</span>
    <div class="topbar__links">
      <a data-tel data-tel-text href="#">+91 00000 00000</a>
      <a data-email data-email-text href="#">info@kiwinurseacademy.com</a>
    </div>
  </div>
</header>
<div class="site-header">
  <div class="wrap">
    <a class="brand" href="{base}index.html">
      <span class="brand__mark">{kiwi}</span>
      <span>Kiwi Nurse Academy<small>IQN &middot; OSCE &middot; OET training</small></span>
    </a>
    <nav class="nav" aria-label="Primary">
      {nav}
      <a class="btn btn--kowhai btn--small" data-wa href="#">{wa} WhatsApp Us</a>
    </nav>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Open menu">{menu}</button>
  </div>
</div>
""".format(base=base, nav=nav_html(base, current),
           kiwi='<svg viewBox="0 0 32 32" aria-hidden="true"><ellipse cx="15" cy="18" rx="10" ry="8.5" fill="#F5B921"/><circle cx="23.5" cy="12" r="3.4" fill="#F5B921"/><path d="M26.3 13.5 30 17" stroke="#F5B921" stroke-width="1.9" stroke-linecap="round"/><path d="M11 25v4M19 25v4" stroke="#F5B921" stroke-width="1.7" stroke-linecap="round"/><path d="M15 13v8M11 17h8" stroke="#0F3A46" stroke-width="2.1" stroke-linecap="round"/></svg>',
           wa=icon("whatsapp"), menu=icon("menu"))


def footer(base):
    return """<div class="cta-band">
  <div class="wrap cta-band__grid">
    <div>
      <h2>Ready to start your New Zealand nursing journey?</h2>
      <p>Book a free 20-minute pathway call. We'll tell you honestly what stage you're at and what to do next &mdash; no obligation.</p>
    </div>
    <div class="btn-row">
      <a class="btn btn--kowhai" data-wa href="#">{wa} Chat on WhatsApp</a>
      <a class="btn btn--ghost" href="{base}contact.html">Book a free call</a>
    </div>
  </div>
</div>
<footer class="site-footer">
  <div class="wrap footer__grid">
    <div>
      <a class="brand" href="{base}index.html">
        <span class="brand__mark">{kiwi}</span>
        <span>Kiwi Nurse Academy</span>
      </a>
      <p class="footer__about">Kerala-based training centre preparing internationally qualified nurses for IQN, OSCE and OET, with a support team in New Zealand.</p>
      <div class="social">
        <a data-social="instagram" href="#" aria-label="Instagram">{insta}</a>
        <a data-social="facebook" href="#" aria-label="Facebook">{fb}</a>
        <a data-social="youtube" href="#" aria-label="YouTube">{yt}</a>
        <a data-social="linkedin" href="#" aria-label="LinkedIn">{li}</a>
      </div>
    </div>
    <div>
      <h4>Courses</h4>
      <ul>
        <li><a href="{base}courses/iqn-training.html">IQN Training</a></li>
        <li><a href="{base}courses/osce-training.html">OSCE Training</a></li>
        <li><a href="{base}courses/oet-preparation.html">OET Preparation</a></li>
        <li><a href="{base}courses/index.html">Compare all courses</a></li>
      </ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="{base}about.html">About us</a></li>
        <li><a href="{base}career.html">Careers</a></li>
        <li><a href="{base}blog.html">Blog</a></li>
        <li><a href="{base}faq.html">FAQ</a></li>
        <li><a href="{base}contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Get in touch</h4>
      <ul>
        <li>{pin} <span data-addr-india>Add your India centre address, City, Kerala</span></li>
        <li>{phone} <a data-tel data-tel-text href="#">+91 00000 00000</a></li>
        <li>{mail} <a data-email data-email-text href="#">info@kiwinurseacademy.com</a></li>
        <li>{clock} <span data-hours>Mon &ndash; Sat, 9:00 am &ndash; 6:00 pm IST</span></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer__legal">
    <p>Kiwi Nurse Academy is an exam-preparation and training provider. We are not the Nursing Council of New Zealand (NCNZ), Pearson VUE, Cambridge Boxhill Language Assessment (OET), or IDP/British Council (IELTS), and we do not set or guarantee exam outcomes. Fees, syllabi and requirements shown on this site are correct to the best of our knowledge and should be confirmed on the relevant official website before you rely on them.</p>
    <div class="footer__bottom">
      <span>&copy; <span id="y"></span> Kiwi Nurse Academy. All rights reserved.</span>
      <ul><li><a href="{base}contact.html">Privacy</a></li><li><a href="{base}contact.html">Terms</a></li></ul>
    </div>
  </div>
</footer>
<a class="wa-float" data-wa href="#" aria-label="Chat on WhatsApp">{wa}<span>Chat with us</span></a>
<script src="{base}assets/js/config.js"></script>
<script src="{base}assets/js/site.js"></script>
<script>document.getElementById('y').textContent = new Date().getFullYear();</script>
</body>
</html>""".format(base=base, wa=icon("whatsapp"), insta=icon("insta"), fb=icon("fb"), yt=icon("yt"), li=icon("linkedin"),
                   pin=icon("pin"), phone=icon("phone"), mail=icon("mail"), clock=icon("clock"),
                   kiwi='<svg viewBox="0 0 32 32" aria-hidden="true"><ellipse cx="15" cy="18" rx="10" ry="8.5" fill="#F5B921"/><circle cx="23.5" cy="12" r="3.4" fill="#F5B921"/><path d="M26.3 13.5 30 17" stroke="#F5B921" stroke-width="1.9" stroke-linecap="round"/><path d="M11 25v4M19 25v4" stroke="#F5B921" stroke-width="1.7" stroke-linecap="round"/><path d="M15 13v8M11 17h8" stroke="#0F3A46" stroke-width="2.1" stroke-linecap="round"/></svg>')


def page(path, title, desc, current, base, body):
    html = head(title, desc, base, path) + header(base, current) + '<main id="main">' + body + '</main>' + footer(base)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path, len(html))


def page_hero(eyebrow_crumbs, title, lead, meta_items=None):
    meta = ""
    if meta_items:
        meta = '<ul class="page-hero__meta">' + "".join("<li>%s</li>" % m for m in meta_items) + "</ul>"
    return """<div class="topo page-hero">
  <div class="wrap">
    <p class="crumbs">{crumbs}</p>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    {meta}
  </div>
</div>""".format(crumbs=eyebrow_crumbs, title=title, lead=lead, meta=meta)


if __name__ == "__main__":
    print("build.py loaded — call the page-writer functions from build_pages.py")
