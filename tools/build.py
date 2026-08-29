#!/usr/bin/env python3
"""Static builder for the AZSCO Security site."""
import os

# Output to the repository root (this script lives in <repo>/tools).
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

SITE = "AZSCO Security"
PHONE = "(+965) 1808606"
PHONE_HREF = "+9651808606"
EMAIL = "info@azsco.com"
ADDRESS = "Floor 27, Kuwait Building Tower,<br>Fahad Al Salem St., Qibla, Kuwait"
ADDRESS_1L = "Floor 27, Kuwait Building Tower, Fahad Al Salem St., Qibla, Kuwait"

# ---------------------------------------------------------------- icons
I = {
"shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
"shield-check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
"flame":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1.5.5-2.5 1-3"/><path d="M12 22a7 7 0 0 0 7-7c0-3-2-5-3-7 0 3-2 4-4 4"/><path d="M12 22a7 7 0 0 1-7-7c0-2 1-3.5 2-4.5"/></svg>',
"alarm":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg>',
"camera":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m2 7 16-4 1.5 5.8L4 13z"/><path d="M6 12v5a2 2 0 0 0 2 2h2"/><circle cx="15" cy="17" r="3"/></svg>',
"lock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
"users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
"home":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>',
"eye":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>',
"clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
"phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
"mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
"pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
"check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 13 4 4L19 7"/></svg>',
"arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>',
"up":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5"/><path d="m6 11 6-6 6 6"/></svg>',
"plus":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14"/><path d="M5 12h14"/></svg>',
"caret":'<svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
"close":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>',
"headset":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14v-2a8 8 0 0 1 16 0v2"/><path d="M4 14h2a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/><path d="M20 14h-2a1 1 0 0 0-1 1v4a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1z"/></svg>',
"cog":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-2.9 1.2v.1a2 2 0 1 1-4 0v-.1A1.7 1.7 0 0 0 7 19.4a1.7 1.7 0 0 0-1.9.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0-1.2-2.9H1a2 2 0 1 1 0-4h.1A1.7 1.7 0 0 0 2.3 7a1.7 1.7 0 0 0-.3-1.9l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1A1.7 1.7 0 0 0 7 2.6h.1a2 2 0 1 1 4 0"/></svg>',
"award":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="9" r="6"/><path d="m8.2 13.8-1.4 7L12 18l5.2 2.8-1.4-7"/></svg>',
"target":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg>',
"wallet":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h13v4"/><path d="M3 7v10a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6a2 2 0 0 0-2-2H5a2 2 0 0 1-2-2z"/><circle cx="17" cy="14" r="1.2"/></svg>',
"grid":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
"file":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/></svg>',
"calendar":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>',
"route":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6" cy="19" r="3"/><circle cx="18" cy="5" r="3"/><path d="M9 19h6a4 4 0 0 0 0-8H9a4 4 0 0 1 0-8h3"/></svg>',
"link":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>',
"phone-app":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/></svg>',
"facebook":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8.5V7a1.5 1.5 0 0 1 1.5-1.5H17V2.6A17 17 0 0 0 14.9 2.5C12.3 2.5 10.6 4 10.6 7v1.5H8V12h2.6v9.5H14V12h2.6l.5-3.5z"/></svg>',
"x":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 3h3l-6.6 7.5L21.7 21h-6l-4.7-6.1L5.6 21h-3l7-8L2.6 3h6.1l4.2 5.6zm-1 16h1.7L7.6 4.7H5.8z"/></svg>',
"instagram":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg>',
"linkedin":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6a4.2 4.2 0 0 1 3.7-2c3 0 4 1.9 4 5V21h-4v-6c0-1.5-.5-2.5-1.9-2.5-1 0-1.6.7-1.9 1.4-.1.3-.1.6-.1 1V21h-4z"/></svg>',
"whatsapp":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-3-.2-.3A8 8 0 1 1 12 20zm4.4-5.8c-.2-.1-1.4-.7-1.6-.8s-.4-.1-.5.1-.6.8-.7 1-.3.2-.5.1a6.6 6.6 0 0 1-3.2-2.8c-.2-.4.2-.4.6-1.2a.5.5 0 0 0 0-.5l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4 5 5 0 0 0 2.3.5 2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
}

def logo(variant="dark"):
    """Brand lockup. `dark` is the black artwork for light backgrounds;
    `light` is the white artwork used on dark backgrounds (the footer)."""
    src = "AZSCO_Logo_white.png" if variant == "light" else "AZSCO_Logo.png"
    return ('<img class="brand-logo" src="assets/img/%s" '
            'alt="AZSCO Security" width="1730" height="798">' % src)

# ---------------------------------------------------------------- nav model
NAV = [
    ("Home", "index.html", []),
    ("About", "about.html", []),
    ("Services", "services.html", [
        ("All Services", "services.html"),
        ("Security Manpower", "services.html#manpower"),
        ("Fire Alarm Systems", "services.html#fire"),
        ("Intrusion Detection", "services.html#intrusion"),
        ("CCTV &amp; Surveillance", "services.html#cctv"),
        ("Access Control", "services.html#access"),
        ("Smart Home &amp; Automation", "services.html#smart"),
    ]),
    ("Divisions", "security.html", [
        ("AZSCO Security", "security.html"),
        ("AZSCO Systems", "systems.html"),
    ]),
    ("Partners", "partners.html", []),
    ("Contact", "contact.html", []),
]

def desktop_nav():
    out = ['<ul class="nav">']
    for label, href, subs in NAV:
        if subs:
            out.append(f'<li><a href="{href}">{label} {I["caret"]}</a><ul class="subnav">')
            for s_label, s_href in subs:
                out.append(f'<li><a href="{s_href}">{s_label}</a></li>')
            out.append('</ul></li>')
        else:
            out.append(f'<li><a href="{href}">{label}</a></li>')
    out.append('</ul>')
    return "\n        ".join(out)

def mobile_nav():
    """Drawer navigation. Sections with children collapse behind a toggle so the
    whole list stays reachable without a long scroll."""
    out = ['<ul class="m-nav">']
    for n, (label, href, subs) in enumerate(NAV):
        if subs:
            out.append(f'<li class="m-group">')
            out.append(f'<button class="m-toggle" type="button" aria-expanded="false" '
                       f'aria-controls="m-sub-{n}">{label}{I["caret"]}</button>')
            out.append(f'<ul class="m-sub" id="m-sub-{n}">')
            for s_label, s_href in subs:
                out.append(f'<li><a href="{s_href}">{s_label}</a></li>')
            out.append('</ul></li>')
        else:
            out.append(f'<li><a href="{href}">{label}</a></li>')
    out.append('</ul>')
    return "\n      ".join(out)

# ---------------------------------------------------------------- shell
def head(title, desc, canonical):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d0d0d">
<link rel="canonical" href="https://www.azsco.com/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AZSCO Security">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://www.azsco.com/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta property="og:image" content="https://www.azsco.com/assets/img/AZSCO_Logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''

def header():
    return f'''
<div class="topbar">
  <div class="wrap">
    <ul class="topbar-list">
      <li class="hide-sm">{I["pin"]}<span>{ADDRESS_1L}</span></li>
      <li>{I["phone"]}<a href="tel:{PHONE_HREF}">{PHONE}</a></li>
      <li class="hide-md">{I["mail"]}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li class="hide-md">{I["clock"]}<span>24/7 Response</span></li>
    </ul>
    <div class="topbar-social" aria-label="AZSCO on social media">
      <a href="#" aria-label="AZSCO on Facebook">{I["facebook"]}</a>
      <a href="#" aria-label="AZSCO on X">{I["x"]}</a>
      <a href="#" aria-label="AZSCO on Instagram">{I["instagram"]}</a>
      <a href="#" aria-label="AZSCO on LinkedIn">{I["linkedin"]}</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="AZSCO Security — home">
      {logo("dark")}
    </a>

    <nav aria-label="Main navigation">
        {desktop_nav()}
    </nav>

    <div class="header-cta">
      <a class="btn btn-primary" href="contact.html">Get a Quote</a>
      <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><span></span></button>
    </div>
  </div>
</header>

<div class="backdrop"></div>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation">
  <div class="mobile-nav-head">
    <img class="brand-logo" src="assets/img/AZSCO_Logo.png" alt="AZSCO Security" width="1730" height="798">
    <button class="close" type="button" aria-label="Close menu">{I["close"]}</button>
  </div>
      {mobile_nav()}
  <div class="mobile-nav-foot">
    <a class="btn btn-primary" href="contact.html">Request a Consultation</a>
    <a class="m-contact" href="tel:{PHONE_HREF}">{I["phone"]}<span>{PHONE}</span></a>
    <a class="m-contact" href="mailto:{EMAIL}">{I["mail"]}<span>{EMAIL}</span></a>
  </div>
</nav>
'''

def footer():
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html" aria-label="AZSCO Security — home">
          {logo("light")}
        </a>
        <p>AZSCO is committed to providing unparalleled security services that ensure the safety and peace of mind of our clients across Kuwait — combining professionally trained manpower with advanced electronic security systems.</p>
        <div class="footer-social">
          <a href="#" aria-label="AZSCO on Facebook">{I["facebook"]}</a>
          <a href="#" aria-label="AZSCO on X">{I["x"]}</a>
          <a href="#" aria-label="AZSCO on Instagram">{I["instagram"]}</a>
          <a href="#" aria-label="AZSCO on LinkedIn">{I["linkedin"]}</a>
        </div>
      </div>

      <div>
        <h4>Company</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About AZSCO</a></li>
          <li><a href="security.html">AZSCO Security</a></li>
          <li><a href="systems.html">AZSCO Systems</a></li>
          <li><a href="partners.html">Our Partners</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>

      <div>
        <h4>Services</h4>
        <ul class="footer-links">
          <li><a href="services.html#manpower">Security Manpower</a></li>
          <li><a href="services.html#fire">Fire Alarm Systems</a></li>
          <li><a href="services.html#intrusion">Intrusion Detection</a></li>
          <li><a href="services.html#cctv">CCTV &amp; Surveillance</a></li>
          <li><a href="services.html#access">Access Control</a></li>
          <li><a href="services.html#smart">Smart Home &amp; Automation</a></li>
        </ul>
      </div>

      <div>
        <h4>Get In Touch</h4>
        <ul class="footer-contact">
          <li>{I["pin"]}<span>{ADDRESS}</span></li>
          <li>{I["phone"]}<a href="tel:{PHONE_HREF}">{PHONE}</a></li>
          <li>{I["mail"]}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{I["clock"]}<span>Sunday – Thursday, 8:00 – 17:00<br>Emergency response 24/7</span></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; <span data-year>2026</span> AZSCO Security Services Company. All rights reserved.</p>
      <ul>
        <li><a href="privacy-policy.html">Privacy Policy</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
  </div>
</footer>

<button class="to-top" type="button" aria-label="Back to top">{I["up"]}</button>

<div class="mobile-bar">
  <a class="mobile-bar-call" href="tel:{PHONE_HREF}">{I["phone"]}<span>Call Now</span></a>
  <a class="mobile-bar-quote" href="contact.html">{I["mail"]}<span>Get a Quote</span></a>
</div>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

def banner(title, sub, crumb):
    items = '<li><a href="index.html">Home</a></li>'
    items += f'<li aria-current="page">{crumb}</li>'
    return f'''
<section class="page-banner">
  <div class="wrap">
    <p class="eyebrow">AZSCO Security</p>
    <h1>{title}</h1>
    <p>{sub}</p>
    <ul class="crumbs">{items}</ul>
  </div>
</section>
'''

def cta(title="Ready to secure what matters most?",
        text="Talk to an AZSCO security consultant about a site survey and a tailored proposal for your premises."):
    return f'''
<section class="cta">
  <div class="wrap">
    <div>
      <h2>{title}</h2>
      <p>{text}</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-primary" href="contact.html">Request a Consultation {I["arrow"]}</a>
      <a class="btn btn-outline" href="tel:{PHONE_HREF}">{PHONE}</a>
    </div>
  </div>
</section>
'''

PAGES = {}

def page(fname, title, desc, body):
    PAGES[fname] = head(title, desc, fname) + header() + f'<main id="main">\n{body}\n</main>' + footer()

# ================================================================= HOME
SERVICE_CARDS = [
    ("manpower", "users", "Security Manpower",
     "Highly trained and professional security personnel to safeguard your premises, assets and people. Our manpower services are tailored to meet the specific requirements of each client."),
    ("fire", "flame", "Fire Alarm Systems",
     "Advanced fire alarm systems to protect lives and property. We provide cutting-edge fire detection and alarm solutions tailored to meet the unique needs of various establishments."),
    ("intrusion", "alarm", "Intrusion Detection",
     "Intrusion systems designed to detect and prevent unauthorized access to your property, using state-of-the-art technology to deliver robust intrusion detection solutions."),
    ("cctv", "camera", "CCTV &amp; Surveillance",
     "Professional CCTV design, installation and maintenance — with high-definition coverage, intelligent recording and remote viewing from any device, anywhere."),
    ("access", "lock", "Access Control",
     "Control exactly who goes where, and when. Card, PIN and biometric access control that integrates with your intrusion, CCTV and fire systems."),
    ("smart", "home", "Smart Home &amp; Automation",
     "Integration and management of smart home devices — lights, locks, thermostats and more — brought together in one secure, easy-to-use application."),
]

def service_cards(limit=None):
    items = SERVICE_CARDS[:limit] if limit else SERVICE_CARDS
    out = []
    for n, (anchor, icon, name, text) in enumerate(items):
        out.append(f'''      <article class="card reveal" data-delay="{n*80}">
        <span class="ico">{I[icon]}</span>
        <h3>{name}</h3>
        <p>{text}</p>
        <a class="more" href="services.html#{anchor}">Learn more {I["arrow"]}</a>
      </article>''')
    return "\n".join(out)

PARTNER_NAMES = ["Bosch", "Honeywell", "Hikvision", "Notifier", "Dahua", "Paradox",
                 "Ajax Systems", "Suprema", "ZKTeco", "Milestone", "Hochiki", "Axis"]

def partner_grid():
    return "\n".join(
        f'      <div class="partner reveal" data-delay="{i*40}">{name}</div>' for i, name in enumerate(PARTNER_NAMES))

HERO_SVG = '''<svg viewBox="0 0 320 300" role="img" aria-label="Illustration of a monitored, protected building">
<defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#9a9a9a"/></linearGradient></defs>
<rect x="70" y="70" width="180" height="180" rx="10" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="2"/>
<rect x="100" y="100" width="120" height="120" rx="8" fill="rgba(255,255,255,.10)" stroke="url(#hg)" stroke-width="2"/>
<path d="M160 118l38 14v26c0 24-16 42-38 50-22-8-38-26-38-50v-26z" fill="none" stroke="url(#hg)" stroke-width="3"/>
<path d="m148 168 9 9 20-20" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="70" cy="70" r="7" fill="#ffffff"/><circle cx="250" cy="70" r="7" fill="#ffffff"/>
<circle cx="70" cy="250" r="7" fill="#ffffff"/><circle cx="250" cy="250" r="7" fill="#ffffff"/>
<path d="M40 160h30M250 160h30M160 40v30M160 250v30" stroke="rgba(255,255,255,.28)" stroke-width="2" stroke-linecap="round"/>
</svg>'''

body = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="hero-badge">{I["shield-check"]} Licensed Security Provider &mdash; Kuwait</span>
        <h1>Professional Security<em>Services for Kuwait</em></h1>
        <p class="lead">AZSCO is committed to providing unparalleled security services that ensure the safety and peace of mind of our clients &mdash; combining highly trained security personnel with advanced fire, intrusion and surveillance systems.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="contact.html">Request a Consultation {I["arrow"]}</a>
          <a class="btn btn-outline" href="services.html">Explore Our Services</a>
        </div>
        <ul class="hero-points">
          <li>{I["check"]} 24/7 monitoring &amp; response</li>
          <li>{I["check"]} Licensed &amp; vetted personnel</li>
          <li>{I["check"]} Certified system integration</li>
        </ul>
      </div>

      <aside class="hero-card reveal" data-delay="120">
        <h3>What We Protect</h3>
        <p>One partner for manpower and technology &mdash; across every kind of premises.</p>
        <ul class="hero-card-list">
          <li><span class="ico">{I["flame"]}</span><span><b>Fire Alarm Systems</b><span>Cutting-edge detection and alarm solutions.</span></span></li>
          <li><span class="ico">{I["alarm"]}</span><span><b>Intrusion Systems</b><span>Detect and prevent unauthorized access.</span></span></li>
          <li><span class="ico">{I["users"]}</span><span><b>Security Manpower</b><span>Trained personnel for premises, assets and people.</span></span></li>
        </ul>
      </aside>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Our Services</p>
      <h2>Complete Security Solutions</h2>
      <p>From manned guarding to fully integrated electronic security, AZSCO delivers protection that is tailored, certified and monitored around the clock.</p>
    </div>
    <div class="grid grid-3">
{service_cards()}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split">
      <div class="split-visual reveal">
        <div class="visual-frame">{HERO_SVG}</div>
        <div class="visual-badge">
          <b>24/7</b><span>Always On Duty</span>
        </div>
      </div>
      <div class="reveal" data-delay="120">
        <p class="eyebrow">About AZSCO</p>
        <h2>A Leading Provider of Security Services in Kuwait</h2>
        <p class="lead">AZSCO is a leading provider of security services in Kuwait with a strong reputation for quality and reliability. Our team of highly trained and experienced security professionals is equipped with the latest technology and equipment to ensure the safety of your property and assets.</p>
        <ul class="check-list">
          <li><span class="ico">{I["check"]}</span><span><b>Customized solutions</b><span>We understand that every client has unique security needs, and tailor our solutions to the specific requirements of each site.</span></span></li>
          <li><span class="ico">{I["check"]}</span><span><b>Cost-effective and efficient</b><span>Our goal is to provide the highest level of security and peace of mind, while keeping our services efficient and affordable.</span></span></li>
          <li><span class="ico">{I["check"]}</span><span><b>Available around the clock</b><span>Our team of dedicated professionals is available 24 hours a day, 7 days a week.</span></span></li>
        </ul>
        <div class="btn-row">
          <a class="btn btn-dark" href="about.html">More About Us {I["arrow"]}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight stats">
  <div class="wrap">
    <div class="grid grid-4">
      <div class="stat reveal"><span class="num"><span data-count="24">0</span>/<span data-count="7">0</span></span><span class="label">Monitoring &amp; Support</span></div>
      <div class="stat reveal" data-delay="80"><span class="num"><span data-count="500">0</span>+</span><span class="label">Systems Installed</span></div>
      <div class="stat reveal" data-delay="160"><span class="num"><span data-count="300">0</span>+</span><span class="label">Security Personnel</span></div>
      <div class="stat reveal" data-delay="240"><span class="num"><span data-count="100">0</span>%</span><span class="label">Client Commitment</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Our Divisions</p>
      <h2>Two Divisions, One Standard</h2>
      <p>AZSCO brings together professional security manpower and certified systems engineering under a single accountable partner.</p>
    </div>
    <div class="division">
      <article class="div-card reveal">
        <span class="tag">Division 01</span>
        <h3>AZSCO Security</h3>
        <p>A comprehensive range of security services, including guarding, patrol services, event security and security consulting &mdash; delivered by professionals equipped with the latest technology and equipment.</p>
        <ul class="div-list">
          <li>{I["check"]} Manned guarding &amp; static posts</li>
          <li>{I["check"]} Mobile patrol services</li>
          <li>{I["check"]} Event &amp; VIP security</li>
          <li>{I["check"]} Security consulting &amp; risk assessment</li>
        </ul>
        <a class="btn btn-primary" href="security.html">Explore AZSCO Security {I["arrow"]}</a>
      </article>

      <article class="div-card reveal" data-delay="120">
        <span class="tag">Division 02</span>
        <h3>AZSCO Systems</h3>
        <p>Design, supply, installation and maintenance of electronic security &mdash; fire alarm, intrusion detection, CCTV, access control and smart home integration, engineered to international standards.</p>
        <ul class="div-list">
          <li>{I["check"]} Fire detection &amp; alarm systems</li>
          <li>{I["check"]} Intrusion &amp; perimeter protection</li>
          <li>{I["check"]} CCTV, access control &amp; integration</li>
          <li>{I["check"]} Smart home &amp; building automation</li>
        </ul>
        <a class="btn btn-primary" href="systems.html">Explore AZSCO Systems {I["arrow"]}</a>
      </article>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Why AZSCO</p>
      <h2>Why Clients Choose Us</h2>
      <p>A strong reputation for quality and reliability, built on people, technology and accountability.</p>
    </div>
    <div class="grid grid-3">
      <div class="tile reveal"><span class="ico">{I["award"]}</span><div><h4>Proven Reputation</h4><p>A leading provider of security services in Kuwait, trusted for quality and reliability across commercial, industrial and residential sites.</p></div></div>
      <div class="tile reveal" data-delay="80"><span class="ico">{I["users"]}</span><div><h4>Trained Professionals</h4><p>Highly trained and experienced security personnel, screened, licensed and supervised to a consistent operating standard.</p></div></div>
      <div class="tile reveal" data-delay="160"><span class="ico">{I["cog"]}</span><div><h4>Latest Technology</h4><p>Our teams are equipped with the latest technology and equipment to ensure the safety of your property and assets.</p></div></div>
      <div class="tile reveal" data-delay="0"><span class="ico">{I["target"]}</span><div><h4>Tailored to You</h4><p>Every client has unique security needs. We design customized solutions around your risk profile, site and operating hours.</p></div></div>
      <div class="tile reveal" data-delay="80"><span class="ico">{I["wallet"]}</span><div><h4>Cost-Effective</h4><p>The highest level of security and peace of mind, delivered in a way that stays efficient and commercially sensible.</p></div></div>
      <div class="tile reveal" data-delay="160"><span class="ico">{I["headset"]}</span><div><h4>24/7 Availability</h4><p>Our dedicated professionals are available 24 hours a day, 7 days a week &mdash; for monitoring, response and support.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">How We Work</p>
      <h2>Our Process</h2>
      <p>A straightforward path from first conversation to a protected, maintained site.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><span class="n">01</span><h4>Consultation</h4><p>We listen to your requirements, operating hours and concerns to understand what actually needs protecting.</p></div>
      <div class="step reveal" data-delay="80"><span class="n">02</span><h4>Site Survey</h4><p>Our specialists assess the premises, identify vulnerabilities and map coverage, access points and risk.</p></div>
      <div class="step reveal" data-delay="160"><span class="n">03</span><h4>Tailored Proposal</h4><p>You receive a clear solution and quotation &mdash; manpower, systems or both &mdash; scoped to your budget.</p></div>
      <div class="step reveal" data-delay="240"><span class="n">04</span><h4>Deploy &amp; Support</h4><p>We install, commission and deploy, then maintain and monitor with 24/7 support behind you.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Our Partners</p>
      <h2>Strategic Partnerships</h2>
      <p>AZSCO has established strategic partnerships with leading industry players to enhance the range and quality of our security solutions.</p>
    </div>
    <div class="partners">
{partner_grid()}
    </div>
    <div class="center" style="margin-top:44px">
      <a class="btn btn-dark" href="partners.html">About Our Partnerships {I["arrow"]}</a>
    </div>
  </div>
</section>

{cta()}
'''

page("index.html",
     "AZSCO Security | Professional Security Services for Kuwait",
     "AZSCO Security is a leading security company in Kuwait offering security manpower, fire alarm systems, intrusion detection, CCTV installation, access control and 24/7 professional security services.",
     body)

# ================================================================= ABOUT
ABOUT_SVG = '''<svg viewBox="0 0 320 300" role="img" aria-label="Illustration of AZSCO security operations">
<defs><linearGradient id="ag" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#9a9a9a"/></linearGradient></defs>
<rect x="46" y="96" width="70" height="130" rx="6" fill="rgba(255,255,255,.16)" stroke="url(#ag)" stroke-width="2"/>
<rect x="126" y="56" width="70" height="170" rx="6" fill="rgba(255,255,255,.24)" stroke="url(#ag)" stroke-width="2"/>
<rect x="206" y="120" width="70" height="106" rx="6" fill="rgba(255,255,255,.09)" stroke="url(#ag)" stroke-width="2"/>
<g fill="rgba(255,255,255,.35)">
<rect x="58" y="112" width="16" height="14" rx="2"/><rect x="86" y="112" width="16" height="14" rx="2"/>
<rect x="58" y="140" width="16" height="14" rx="2"/><rect x="86" y="140" width="16" height="14" rx="2"/>
<rect x="138" y="76" width="16" height="14" rx="2"/><rect x="166" y="76" width="16" height="14" rx="2"/>
<rect x="138" y="104" width="16" height="14" rx="2"/><rect x="166" y="104" width="16" height="14" rx="2"/>
<rect x="218" y="140" width="16" height="14" rx="2"/><rect x="246" y="140" width="16" height="14" rx="2"/>
</g>
<path d="M161 150l30 11v21c0 19-13 33-30 40-17-7-30-21-30-40v-21z" fill="#0d0d0d" stroke="url(#ag)" stroke-width="3"/>
<path d="m150 182 8 8 17-17" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M30 236h260" stroke="rgba(255,255,255,.25)" stroke-width="3" stroke-linecap="round"/>
</svg>'''

body = banner("About AZSCO",
  "A leading provider of security services in Kuwait, with a strong reputation for quality and reliability.",
  "About") + f'''
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split-visual reveal">
        <div class="visual-frame">{ABOUT_SVG}</div>
        <div class="visual-badge"><b>KWT</b><span>Serving Kuwait</span></div>
      </div>
      <div class="reveal" data-delay="120">
        <p class="eyebrow">Who We Are</p>
        <h2>Security You Can Build On</h2>
        <p class="lead">AZSCO is committed to providing unparalleled security services that ensure the safety and peace of mind of our clients. We are a leading provider of security services in Kuwait with a strong reputation for quality and reliability.</p>
        <p>We offer a comprehensive range of security services, including guarding, patrol services, event security and security consulting. Our team of highly trained and experienced security professionals is equipped with the latest technology and equipment to ensure the safety of your property and assets.</p>
        <p>Alongside our manpower services, AZSCO designs and installs advanced fire alarm systems, intrusion detection, CCTV and access control &mdash; so a single accountable partner covers both the people and the technology protecting your site.</p>
        <div class="btn-row">
          <a class="btn btn-dark" href="contact.html">Talk to Our Team {I["arrow"]}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="grid grid-3">
      <article class="card reveal">
        <span class="ico">{I["target"]}</span>
        <h3>Our Mission</h3>
        <p>To provide the highest level of security and peace of mind for every client, while ensuring that our services remain cost-effective and efficient.</p>
      </article>
      <article class="card reveal" data-delay="80">
        <span class="ico">{I["eye"]}</span>
        <h3>Our Vision</h3>
        <p>To be Kuwait&rsquo;s most trusted security partner &mdash; recognised for quality, reliability and the strength of the people and technology we put on the ground.</p>
      </article>
      <article class="card reveal" data-delay="160">
        <span class="ico">{I["shield-check"]}</span>
        <h3>Our Values</h3>
        <p>Integrity, vigilance and accountability. We understand that every client has unique security needs, and we tailor our solutions to meet them exactly.</p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">What Sets Us Apart</p>
      <h2>Our Commitment</h2>
      <p>Everything we do is measured against one standard: does it make our client safer?</p>
    </div>
    <div class="grid grid-2">
      <div class="tile reveal"><span class="ico">{I["users"]}</span><div><h4>Highly Trained Personnel</h4><p>Our security professionals are screened, licensed, trained and supervised &mdash; and equipped with the technology they need to do the job properly.</p></div></div>
      <div class="tile reveal" data-delay="80"><span class="ico">{I["cog"]}</span><div><h4>Certified Systems Engineering</h4><p>Fire, intrusion, CCTV and access control systems designed and commissioned to international standards, and maintained for the life of the installation.</p></div></div>
      <div class="tile reveal"><span class="ico">{I["target"]}</span><div><h4>Customized Solutions</h4><p>Every client has unique security needs. We survey, assess and design around your site rather than selling a fixed package.</p></div></div>
      <div class="tile reveal" data-delay="80"><span class="ico">{I["clock"]}</span><div><h4>Available 24/7</h4><p>Our team of dedicated professionals is available 24 hours a day, 7 days a week to provide the highest level of security and peace of mind.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--tight stats">
  <div class="wrap">
    <div class="grid grid-4">
      <div class="stat reveal"><span class="num"><span data-count="24">0</span>/<span data-count="7">0</span></span><span class="label">Operations Coverage</span></div>
      <div class="stat reveal" data-delay="80"><span class="num"><span data-count="500">0</span>+</span><span class="label">Systems Installed</span></div>
      <div class="stat reveal" data-delay="160"><span class="num"><span data-count="300">0</span>+</span><span class="label">Security Personnel</span></div>
      <div class="stat reveal" data-delay="240"><span class="num"><span data-count="12">0</span>+</span><span class="label">Technology Partners</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Questions</p>
      <h2>Frequently Asked</h2>
    </div>
    <div style="max-width:840px;margin:0 auto">
      <div class="acc is-open reveal">
        <button class="acc-btn" type="button">What areas does AZSCO cover?<span class="pm">{I["plus"]}</span></button>
        <div class="acc-panel"><div class="inner">AZSCO provides security manpower and security systems across Kuwait, from our office at {ADDRESS_1L}. Call {PHONE} to discuss coverage for your site.</div></div>
      </div>
      <div class="acc reveal">
        <button class="acc-btn" type="button">Do you provide both guards and security systems?<span class="pm">{I["plus"]}</span></button>
        <div class="acc-panel"><div class="inner">Yes. AZSCO Security supplies trained security personnel &mdash; guarding, patrols, event security and consulting &mdash; while AZSCO Systems designs and installs fire alarm, intrusion, CCTV, access control and smart home solutions. Most clients use both under one contract.</div></div>
      </div>
      <div class="acc reveal">
        <button class="acc-btn" type="button">How quickly can a system be installed?<span class="pm">{I["plus"]}</span></button>
        <div class="acc-panel"><div class="inner">Timelines depend on the size and complexity of the site. After a free site survey we issue a proposal with a clear schedule for supply, installation, commissioning and handover &mdash; along with the maintenance plan that follows it.</div></div>
      </div>
      <div class="acc reveal">
        <button class="acc-btn" type="button">Is support available outside working hours?<span class="pm">{I["plus"]}</span></button>
        <div class="acc-panel"><div class="inner">Our office hours are Sunday to Thursday, 8:00 to 17:00, but our team of dedicated professionals is available 24 hours a day, 7 days a week for monitoring, emergency response and technical support.</div></div>
      </div>
    </div>
  </div>
</section>

{cta()}
'''

page("about.html",
     "About Us | AZSCO Security Kuwait",
     "AZSCO is a leading provider of security services in Kuwait with a strong reputation for quality and reliability — offering guarding, patrols, event security, consulting and advanced security systems.",
     body)

# ================================================================= SERVICES
SERVICE_DETAIL = [
 ("manpower","users","Security Manpower",
  "Highly trained and professional security personnel to safeguard your premises, assets and people. Our security manpower services are tailored to meet the specific requirements of each client.",
  ["Static guarding for offices, towers, compounds and industrial sites",
   "Reception, concierge and front-of-house security",
   "Mobile patrols and lock-and-unlock services",
   "Event, exhibition and VIP protection details",
   "Supervisors, shift rotation and documented reporting"]),
 ("fire","flame","Fire Alarm Systems",
  "Advanced fire alarm systems to protect lives and property. AZSCO provides cutting-edge fire detection and alarm solutions tailored to meet the unique needs of various establishments.",
  ["Addressable and conventional fire alarm panels",
   "Smoke, heat, multi-sensor and beam detection",
   "Sounders, strobes, voice evacuation and interfaces",
   "Design, supply, installation, testing and commissioning",
   "Scheduled inspection and preventive maintenance"]),
 ("intrusion","alarm","Intrusion Detection",
  "Intrusion systems designed to detect and prevent unauthorized access to your property. We utilise state-of-the-art technology to deliver robust intrusion detection solutions.",
  ["Wired and wireless intrusion alarm panels",
   "Motion, glass-break, vibration and door contacts",
   "Perimeter protection and external beam detection",
   "Panic and hold-up devices for high-risk areas",
   "Mobile alerts with 24/7 monitored response"]),
 ("cctv","camera","CCTV &amp; Surveillance",
  "CCTV installation, configuration and maintenance — with high-definition coverage, intelligent recording and secure remote viewing from any device, anywhere.",
  ["IP and HD camera systems for indoor and outdoor use",
   "NVR / DVR storage sized to your retention policy",
   "Video analytics, motion search and line-crossing alerts",
   "Remote viewing via mobile and desktop applications",
   "Health checks, cleaning and lens re-alignment"]),
 ("access","lock","Access Control",
  "Control exactly who goes where, and when. AZSCO delivers card, PIN and biometric access control that integrates cleanly with your intrusion, CCTV and fire alarm systems.",
  ["Proximity card, PIN and biometric readers",
   "Door controllers, maglocks, turnstiles and barriers",
   "Time and attendance reporting",
   "Visitor management and audit trails",
   "Fire alarm interfacing for safe egress"]),
 ("smart","home","Smart Home &amp; Automation",
  "Integration and management of smart home devices — lights, locks, thermostats and more — brought together in one secure, easy-to-use application.",
  ["Smart locks, video doorbells and indoor cameras",
   "Lighting, curtain and climate automation",
   "Scenes, schedules and away-mode simulation",
   "Single-app control for the whole property",
   "Integration with alarm and CCTV systems"]),
 ("consulting","file","Security Consulting",
  "Independent assessment of your risk profile, followed by a practical plan. We help you decide what to protect, how, and in what order.",
  ["Site surveys and vulnerability assessments",
   "Security policies, procedures and post orders",
   "Manpower deployment planning",
   "System specification and tender support",
   "Post-incident review and recommendations"]),
 ("monitoring","headset","24/7 Monitoring &amp; Support",
  "Our team of dedicated professionals is available 24 hours a day, 7 days a week — for alarm monitoring, fire monitoring, emergency response and technical support.",
  ["Alarm and fire signal monitoring",
   "Escalation to key holders and authorities",
   "Emergency call-out and response",
   "Preventive and corrective maintenance contracts",
   "Service-level reporting"]),
]

def service_sections():
    out = []
    for i, (anchor, icon, name, intro, points) in enumerate(SERVICE_DETAIL):
        alt = " section--alt" if i % 2 else ""
        lis = "\n".join(f'          <li><span class="ico">{I["check"]}</span><span>{p}</span></li>' for p in points)
        flip = " split--flip" if i % 2 else ""
        out.append(f'''
<section class="section{alt}" id="{anchor}">
  <div class="wrap">
    <div class="split{flip}">
      <div class="reveal">
        <p class="eyebrow">Service {i+1:02d}</p>
        <h2>{name}</h2>
        <p class="lead">{intro}</p>
        <ul class="check-list">
{lis}
        </ul>
        <div class="btn-row">
          <a class="btn btn-dark" href="contact.html">Request a Quote {I["arrow"]}</a>
        </div>
      </div>
      <div class="split-visual reveal" data-delay="120">
        <div class="visual-frame"><div style="color:#fff;width:160px;max-width:60%">{I[icon]}</div></div>
      </div>
    </div>
  </div>
</section>''')
    return "\n".join(out)

body = banner("Our Services",
  "A comprehensive range of security services — guarding, patrol services, event security and security consulting — backed by advanced fire, intrusion and surveillance systems.",
  "Services") + f'''
<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Overview</p>
      <h2>What AZSCO Delivers</h2>
      <p>Whether you need people on the ground, technology on the walls, or both, our services are tailored to the specific requirements of each client.</p>
    </div>
    <div class="grid grid-3">
{service_cards()}
    </div>
  </div>
</section>
{service_sections()}
{cta("Not sure which service you need?","Book a free site survey. We will assess your premises and recommend the right combination of manpower and systems.")}
'''

page("services.html",
     "Security Services in Kuwait | AZSCO Security",
     "AZSCO security services in Kuwait: security manpower, guarding, patrols, event security, consulting, fire alarm systems, intrusion detection, CCTV, access control and smart home automation.",
     body)

# ================================================================= AZSCO SECURITY
body = banner("AZSCO Security",
  "Guarding, patrol services, event security and security consulting — delivered by highly trained and experienced professionals.",
  "AZSCO Security") + f'''
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Division 01</p>
        <h2>Security Manpower You Can Rely On</h2>
        <p class="lead">AZSCO offers a comprehensive range of security services, including guarding, patrol services, event security and security consulting. Our team of highly trained and experienced security professionals is equipped with the latest technology and equipment to ensure the safety of your property and assets.</p>
        <p>We understand that every client has unique security needs and offer customized security solutions tailored to meet the specific requirements of each client. Our goal is to provide the highest level of security and peace of mind, while ensuring that our services are cost-effective and efficient.</p>
        <p>Our team of dedicated professionals is available 24 hours a day, 7 days a week.</p>
        <div class="btn-row">
          <a class="btn btn-dark" href="contact.html">Discuss Your Requirement {I["arrow"]}</a>
        </div>
      </div>
      <div class="split-visual reveal" data-delay="120">
        <div class="visual-frame"><div style="color:#fff;width:170px;max-width:60%">{I["users"]}</div></div>
        <div class="visual-badge"><b>24/7</b><span>On Duty</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Services</p>
      <h2>What This Division Covers</h2>
    </div>
    <div class="grid grid-4">
      <article class="card reveal"><span class="ico">{I["shield"]}</span><h3>Guarding</h3><p>Static security officers for towers, offices, compounds, retail and industrial premises &mdash; with supervision and documented reporting.</p></article>
      <article class="card reveal" data-delay="80"><span class="ico">{I["route"]}</span><h3>Patrol Services</h3><p>Scheduled and random mobile patrols, perimeter checks and lock-and-unlock services that keep an unpredictable, visible presence.</p></article>
      <article class="card reveal" data-delay="160"><span class="ico">{I["calendar"]}</span><h3>Event Security</h3><p>Crowd management, access screening, VIP details and stewarding for exhibitions, conferences and private events.</p></article>
      <article class="card reveal" data-delay="240"><span class="ico">{I["file"]}</span><h3>Security Consulting</h3><p>Risk assessments, security surveys, policies and deployment planning &mdash; so your spend goes where the risk actually is.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Our People</p>
      <h2>Trained, Vetted, Supervised</h2>
      <p>The strength of a manned security contract is the standard behind every shift.</p>
    </div>
    <div class="grid grid-3">
      <div class="tile reveal"><span class="ico">{I["shield-check"]}</span><div><h4>Screened &amp; Licensed</h4><p>Every officer is background checked and licensed before deployment, and briefed on site-specific post orders.</p></div></div>
      <div class="tile reveal" data-delay="80"><span class="ico">{I["award"]}</span><div><h4>Continuously Trained</h4><p>Ongoing training in access control, emergency procedures, fire response, customer service and incident reporting.</p></div></div>
      <div class="tile reveal" data-delay="160"><span class="ico">{I["headset"]}</span><div><h4>Actively Supervised</h4><p>Field supervisors, shift audits and a control room reachable 24 hours a day, 7 days a week.</p></div></div>
    </div>
  </div>
</section>

{cta("Need security personnel on site?","Tell us about your premises and shift pattern and we will propose a deployment plan and quotation.")}
'''

page("security.html",
     "AZSCO Security | Guarding, Patrols &amp; Event Security in Kuwait",
     "AZSCO Security offers guarding, patrol services, event security and security consulting in Kuwait, delivered by highly trained professionals available 24/7.",
     body)

# ================================================================= AZSCO SYSTEMS
body = banner("AZSCO Systems",
  "Fire alarm, intrusion detection, CCTV, access control and smart home integration — designed, installed and maintained to international standards.",
  "AZSCO Systems") + f'''
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split-visual reveal">
        <div class="visual-frame"><div style="color:#fff;width:170px;max-width:60%">{I["cog"]}</div></div>
        <div class="visual-badge"><b>ISO</b><span>Standards Led</span></div>
      </div>
      <div class="reveal" data-delay="120">
        <p class="eyebrow">Division 02</p>
        <h2>Electronic Security, Engineered Properly</h2>
        <p class="lead">AZSCO Systems provides advanced fire alarm systems to protect lives and property, and intrusion systems designed to detect and prevent unauthorized access to your property &mdash; using state-of-the-art technology throughout.</p>
        <p>We handle the full lifecycle: survey, design, supply, installation, commissioning, handover and maintenance. Systems are integrated so that fire, intrusion, CCTV and access control work as one, not as four disconnected products.</p>
        <p>Alongside commercial installations we integrate and manage smart home devices &mdash; lights, locks, thermostats and more &mdash; in a single secure application.</p>
        <div class="btn-row">
          <a class="btn btn-dark" href="contact.html">Book a Site Survey {I["arrow"]}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Systems</p>
      <h2>Solutions We Install</h2>
    </div>
    <div class="grid grid-3">
      <article class="card reveal"><span class="ico">{I["flame"]}</span><h3>Fire Alarm Systems</h3><p>Cutting-edge fire detection and alarm solutions tailored to meet the unique needs of various establishments &mdash; addressable panels, detection, evacuation and interfacing.</p><a class="more" href="services.html#fire">Learn more {I["arrow"]}</a></article>
      <article class="card reveal" data-delay="80"><span class="ico">{I["alarm"]}</span><h3>Intrusion Systems</h3><p>Robust intrusion detection using state-of-the-art technology &mdash; panels, motion and perimeter detection, panic devices and monitored response.</p><a class="more" href="services.html#intrusion">Learn more {I["arrow"]}</a></article>
      <article class="card reveal" data-delay="160"><span class="ico">{I["camera"]}</span><h3>CCTV &amp; Surveillance</h3><p>HD and IP camera systems with intelligent recording, analytics and secure remote viewing from any device, anywhere.</p><a class="more" href="services.html#cctv">Learn more {I["arrow"]}</a></article>
      <article class="card reveal"><span class="ico">{I["lock"]}</span><h3>Access Control</h3><p>Card, PIN and biometric access control with door hardware, turnstiles, visitor management and full audit trails.</p><a class="more" href="services.html#access">Learn more {I["arrow"]}</a></article>
      <article class="card reveal" data-delay="80"><span class="ico">{I["home"]}</span><h3>Smart Home</h3><p>Integration and management of smart home devices including lights, locks, thermostats and more &mdash; controlled from one application.</p><a class="more" href="services.html#smart">Learn more {I["arrow"]}</a></article>
      <article class="card reveal" data-delay="160"><span class="ico">{I["headset"]}</span><h3>Monitoring &amp; Maintenance</h3><p>Fire and alarm monitoring, emergency call-out and planned preventive maintenance contracts that keep systems certified and working.</p><a class="more" href="services.html#monitoring">Learn more {I["arrow"]}</a></article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">AZSCO App</p>
        <h2>Your Systems, In One Application</h2>
        <p class="lead">The AZSCO application brings your protected site into one place &mdash; arm and disarm your alarm, view cameras, check event history and control connected smart devices from your phone.</p>
        <ul class="div-list">
          <li>{I["check"]} Live camera viewing and playback</li>
          <li>{I["check"]} Arm, disarm and receive instant alerts</li>
          <li>{I["check"]} Smart lights, locks and thermostats</li>
          <li>{I["check"]} Multi-site and multi-user access</li>
        </ul>
        <div class="btn-row" style="margin-top:26px">
          <a class="btn btn-primary" href="contact.html">Ask About the App {I["arrow"]}</a>
        </div>
      </div>
      <div class="split-visual reveal" data-delay="120">
        <div class="visual-frame"><div style="color:#fff;width:130px;max-width:45%">{I["phone-app"]}</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Delivery</p>
      <h2>From Survey to Handover</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><span class="n">01</span><h4>Survey &amp; Design</h4><p>We assess the site, map risk and produce a compliant system design with a full bill of materials.</p></div>
      <div class="step reveal" data-delay="80"><span class="n">02</span><h4>Supply &amp; Install</h4><p>Equipment from our partner brands, installed by our own certified engineers to manufacturer specification.</p></div>
      <div class="step reveal" data-delay="160"><span class="n">03</span><h4>Test &amp; Commission</h4><p>Every device is tested, the system is commissioned, and your team is trained before handover.</p></div>
      <div class="step reveal" data-delay="240"><span class="n">04</span><h4>Maintain &amp; Monitor</h4><p>Planned preventive maintenance, 24/7 monitoring and rapid corrective response for the life of the system.</p></div>
    </div>
  </div>
</section>

{cta("Planning a new installation or upgrade?","Our engineers will survey your premises and specify a system that meets standards, budget and risk.")}
'''

page("systems.html",
     "AZSCO Systems | Fire Alarm, Intrusion, CCTV &amp; Access Control Kuwait",
     "AZSCO Systems designs, installs and maintains fire alarm systems, intrusion detection, CCTV, access control and smart home automation across Kuwait.",
     body)

# ================================================================= PARTNERS
body = banner("Our Partners",
  "AZSCO has established strategic partnerships with leading industry players to enhance the range and quality of our security solutions.",
  "Partners") + f'''
<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Strategic Partnerships</p>
      <h2>Backed by the Industry&rsquo;s Best</h2>
      <p>We work with established manufacturers so that the equipment we install is supported, certified and available for years &mdash; not orphaned after the first fault.</p>
    </div>
    <div class="partners">
{partner_grid()}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">Why It Matters</p>
      <h2>What Our Partnerships Give You</h2>
    </div>
    <div class="grid grid-3">
      <div class="tile reveal"><span class="ico">{I["award"]}</span><div><h4>Certified Engineers</h4><p>Manufacturer training and certification means our engineers commission systems the way they were designed to be commissioned.</p></div></div>
      <div class="tile reveal" data-delay="80"><span class="ico">{I["cog"]}</span><div><h4>Genuine Equipment</h4><p>Authorised supply channels, full warranty cover and spare-part availability for the life of the installation.</p></div></div>
      <div class="tile reveal" data-delay="160"><span class="ico">{I["link"]}</span><div><h4>Integrated Solutions</h4><p>Proven interoperability between fire, intrusion, CCTV and access control platforms &mdash; one system, not four silos.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Work With Us</p>
        <h2>Become an AZSCO Partner</h2>
        <p class="lead">We are always interested in working with manufacturers, distributors, consultants and contractors who share our standard of delivery.</p>
        <p>If your products or services would strengthen what we offer clients in Kuwait, we would like to hear from you. Send an outline of your proposal to <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE}.</p>
        <div class="btn-row">
          <a class="btn btn-dark" href="contact.html">Start a Conversation {I["arrow"]}</a>
        </div>
      </div>
      <div class="split-visual reveal" data-delay="120">
        <div class="visual-frame"><div style="color:#fff;width:160px;max-width:55%">{I["link"]}</div></div>
      </div>
    </div>
  </div>
</section>

{cta()}
'''

page("partners.html",
     "Our Partners | AZSCO Security Kuwait",
     "AZSCO has established strategic partnerships with leading industry players to enhance the range and quality of our security solutions in Kuwait.",
     body)

# ================================================================= CONTACT
body = banner("Contact Us",
  "Talk to AZSCO about guarding, systems or a free site survey. Our team is available 24 hours a day, 7 days a week.",
  "Contact") + f'''
<section class="section">
  <div class="wrap">
    <div class="grid grid-3" style="margin-bottom:64px">
      <div class="info-card reveal">
        <span class="ico">{I["pin"]}</span>
        <div><h4>Visit Our Office</h4><p>{ADDRESS}</p></div>
      </div>
      <div class="info-card reveal" data-delay="80">
        <span class="ico">{I["phone"]}</span>
        <div><h4>Call Us</h4><a href="tel:{PHONE_HREF}">{PHONE}</a><p style="color:var(--muted);font-size:.86rem">24/7 emergency response</p></div>
      </div>
      <div class="info-card reveal" data-delay="160">
        <span class="ico">{I["mail"]}</span>
        <div><h4>Email Us</h4><a href="mailto:{EMAIL}">{EMAIL}</a><p style="color:var(--muted);font-size:.86rem">We reply within one business day</p></div>
      </div>
    </div>

    <div class="contact-grid">
      <div class="reveal">
        <p class="eyebrow">Get In Touch</p>
        <h2>Request a Free Site Survey</h2>
        <p>Tell us a little about your premises and what you need protected. One of our security consultants will contact you to arrange a survey and prepare a tailored proposal.</p>

        <div class="map-embed" style="margin-top:32px">
          <div class="pin">
            {I["pin"]}
            <h4>AZSCO Security Services Company</h4>
            <p>{ADDRESS_1L}</p>
          </div>
        </div>

        <ul class="check-list" style="margin-top:32px">
          <li><span class="ico">{I["check"]}</span><span><b>Office hours</b><span>Sunday &ndash; Thursday, 8:00 &ndash; 17:00</span></span></li>
          <li><span class="ico">{I["check"]}</span><span><b>Emergency response</b><span>Available 24 hours a day, 7 days a week</span></span></li>
        </ul>
      </div>

      <div class="form-card reveal" data-delay="120">
        <form data-contact-form novalidate>
          <div class="form-status" role="status" aria-live="polite"></div>

          <div class="grid grid-2" style="gap:0 20px">
            <div class="field">
              <label for="name">Full Name <span class="req">*</span></label>
              <input type="text" id="name" name="name" placeholder="Your name" required>
              <span class="err">This field is required.</span>
            </div>
            <div class="field">
              <label for="company">Company</label>
              <input type="text" id="company" name="company" placeholder="Company name">
              <span class="err"></span>
            </div>
            <div class="field">
              <label for="email">Email <span class="req">*</span></label>
              <input type="email" id="email" name="email" placeholder="you@example.com" required>
              <span class="err">Please enter a valid email address.</span>
            </div>
            <div class="field">
              <label for="phone">Phone <span class="req">*</span></label>
              <input type="tel" id="phone" name="phone" placeholder="+965 0000 0000" required>
              <span class="err">Please enter a valid phone number.</span>
            </div>
          </div>

          <div class="field">
            <label for="service">Service Required <span class="req">*</span></label>
            <select id="service" name="service" required>
              <option value="">Please select&hellip;</option>
              <option>Security Manpower / Guarding</option>
              <option>Patrol Services</option>
              <option>Event Security</option>
              <option>Security Consulting</option>
              <option>Fire Alarm Systems</option>
              <option>Intrusion Detection</option>
              <option>CCTV &amp; Surveillance</option>
              <option>Access Control</option>
              <option>Smart Home &amp; Automation</option>
              <option>Maintenance &amp; Monitoring</option>
              <option>Other enquiry</option>
            </select>
            <span class="err">Please choose a service.</span>
          </div>

          <div class="field">
            <label for="message">How Can We Help? <span class="req">*</span></label>
            <textarea id="message" name="message" placeholder="Tell us about your site, the number of entrances, operating hours, and what you need protected." required></textarea>
            <span class="err">This field is required.</span>
          </div>

          <button class="btn btn-primary" type="submit" style="width:100%">Send Enquiry {I["arrow"]}</button>
          <p class="form-note">By submitting this form you agree to our <a href="privacy-policy.html">Privacy Policy</a>. For urgent matters please call {PHONE}.</p>
        </form>
      </div>
    </div>
  </div>
</section>

{cta("Prefer to speak to someone now?","Our team is available 24 hours a day, 7 days a week for urgent security matters.")}
'''

page("contact.html",
     "Contact AZSCO Security | Kuwait",
     f"Contact AZSCO Security in Kuwait. Office: {ADDRESS_1L}. Tel {PHONE}. Email {EMAIL}. Request a free site survey.",
     body)

# ================================================================= PRIVACY
body = banner("Privacy Policy",
  "How AZSCO collects, uses and protects the personal information you share with us.",
  "Privacy Policy") + f'''
<section class="section">
  <div class="wrap">
    <div class="rich reveal">
      <span class="updated">Last updated: January 2026</span>

      <p class="lead">AZSCO Security Services Company (&ldquo;AZSCO&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;) respects your privacy. This policy explains what personal information we collect through this website and our services, how we use it, and the choices available to you.</p>

      <h2>Information We Collect</h2>
      <p>We collect information that you provide directly to us, and a limited amount of technical information collected automatically when you visit this website.</p>
      <ul>
        <li><b>Information you provide:</b> your name, company, email address, telephone number, the service you are enquiring about, and any details you include in an enquiry or quotation request.</li>
        <li><b>Technical information:</b> browser type, device type, approximate location, referring page and pages viewed, collected through server logs and cookies.</li>
        <li><b>Service information:</b> where you become a client, records relating to site surveys, installed systems, maintenance visits and monitoring events.</li>
      </ul>

      <h2>How We Use Your Information</h2>
      <ul>
        <li>To respond to your enquiry and prepare quotations or proposals.</li>
        <li>To arrange and carry out site surveys, installations, maintenance and monitoring.</li>
        <li>To provide customer support and manage our contractual relationship with you.</li>
        <li>To improve this website, our services and our communications.</li>
        <li>To comply with legal, regulatory and licensing obligations in the State of Kuwait.</li>
      </ul>

      <h2>Cookies</h2>
      <p>This website uses cookies and similar technologies to keep the site working correctly and to understand how visitors use it. You can control or delete cookies through your browser settings. Disabling cookies may affect parts of the site&rsquo;s functionality.</p>

      <h2>Sharing Your Information</h2>
      <p>We do not sell your personal information. We may share it with:</p>
      <ul>
        <li>Service providers who support our operations, such as hosting and IT providers, under confidentiality obligations.</li>
        <li>Technology partners and manufacturers where necessary to fulfil warranty, support or commissioning obligations.</li>
        <li>Competent authorities where disclosure is required by law or to protect life and property.</li>
      </ul>

      <h2>Data Security</h2>
      <p>We apply appropriate technical and organisational measures to protect personal information against unauthorised access, loss or misuse. No method of transmission or storage is completely secure, but we work to protect your information and to review our safeguards regularly.</p>

      <h2>Data Retention</h2>
      <p>We keep personal information only for as long as necessary for the purposes described in this policy, or for as long as required by applicable law, contract or licensing requirements.</p>

      <h2>Your Rights</h2>
      <p>You may request access to the personal information we hold about you, ask us to correct inaccurate information, or ask us to delete information where we are not required to retain it. To make a request, contact us using the details below.</p>

      <h2>CCTV and Monitoring</h2>
      <p>Where AZSCO operates or maintains CCTV, access control or alarm monitoring systems on behalf of a client, the client is responsible for how that system is used at their premises. AZSCO processes such data only as instructed by the client and as permitted by applicable law.</p>

      <h2>Third-Party Links</h2>
      <p>This website may link to third-party sites. We are not responsible for the privacy practices or content of those sites, and we encourage you to read their privacy policies.</p>

      <h2>Changes to This Policy</h2>
      <p>We may update this policy from time to time. The revised version will be posted on this page with an updated date.</p>

      <h2>Contact Us</h2>
      <p>If you have questions about this Privacy Policy or how we handle your information, please contact us:</p>
      <ul>
        <li><b>AZSCO Security Services Company</b></li>
        <li>{ADDRESS_1L}</li>
        <li>Telephone: <a href="tel:{PHONE_HREF}">{PHONE}</a></li>
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
  </div>
</section>
'''

page("privacy-policy.html",
     "Privacy Policy | AZSCO Security",
     "AZSCO Security privacy policy — how we collect, use, share and protect the personal information you provide through our website and services.",
     body)

# ================================================================= 404
body = f'''
<section class="section" style="padding:120px 0">
  <div class="wrap center">
    <p class="eyebrow" style="justify-content:center">Error 404</p>
    <h1 style="margin-bottom:18px">Page Not Found</h1>
    <p class="lead" style="max-width:560px;margin:0 auto 32px">The page you are looking for may have been moved or no longer exists. Let us get you back to safety.</p>
    <div class="btn-row center">
      <a class="btn btn-primary" href="index.html">Back to Home {I["arrow"]}</a>
      <a class="btn btn-dark" href="contact.html">Contact Us</a>
    </div>
  </div>
</section>
'''
page("404.html", "Page Not Found | AZSCO Security",
     "The page you requested could not be found on the AZSCO Security website.", body)

# ---------------------------------------------------------------- write
if __name__ == "__main__":
    for fname, html in PAGES.items():
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as fh:
            fh.write(html)
        print("wrote", fname, len(html), "bytes")
