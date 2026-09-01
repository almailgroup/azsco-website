#!/usr/bin/env python3
"""Static builder for the AZSCO Security site (English + Arabic)."""
import os
import datetime

# Output to the repository root (this script lives in <repo>/tools).
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

LANGS = ("en", "ar")

PHONE = "(+965) 1808606"
PHONE_HREF = "+9651808606"
EMAIL = "info@azsco.com"          # general enquiries
EMAIL_SALES = "sales@azsco.com"   # sales and quotations
MAPS_URL = "https://maps.app.goo.gl/BN2Byxt6BCJ62XV26"

# ---------------------------------------------------------------- assistant
# CHAT_MODE selects how the browser reaches Mistral:
#   "direct" — the browser calls api.mistral.ai itself using CHAT_API_KEY below.
#              The key is compiled into assets/js/chat-config.js and is therefore
#              readable by anyone who views the site. Set a spend limit on the
#              Mistral account, and rotate the key if it is ever misused.
#   "proxy"  — the browser calls CHAT_ENDPOINT, and a server-side function holds
#              the key (see api/chat.js and api/README.md). Nothing is exposed.
CHAT_MODE = "direct"
CHAT_ENDPOINT = "/api/chat"
CHAT_API_KEY = "nqiT2l7oBl5499RBMVgBQLFBoKwaiCi8"
CHAT_MODEL = "mistral-small-latest"

# The facts the assistant may rely on. This is the single source of truth: the
# proxy in api/chat.js carries its own copy for when CHAT_MODE is "proxy".
CHAT_FACTS = """
COMPANY
- AZSCO for Facility Guard Services (AZSCO), established 2008, headquartered in
  Qibla, Kuwait. Part of Almail Group.
- Office: Floor 27, Kuwait Building Tower, Fahad Al Salem St., Qibla, Kuwait.
- Telephone: (+965) 1808606.
- Email: info@azsco.com for general enquiries, sales@azsco.com for sales
  and quotations.
- Office hours: Sunday to Thursday, 8:00-17:00. Emergency response 24/7.

WHAT AZSCO DOES
AZSCO provides security manpower only. It does NOT sell, install or maintain
security systems (no fire alarm, intrusion, CCTV, access control or smart home
installation). Services:
- Manned Guarding: static security officers for apartments, malls, banks,
  stores, offices, compounds and industrial sites.
- Mobile Patrols: scheduled and random patrols, perimeter checks,
  lock-and-unlock, key holding, alarm response.
- Event & VIP Security: crowd management, access screening, stewarding,
  close protection.
- Reception & Concierge: front-of-house officers, visitor management,
  contractor and delivery control.
- Security Consulting: site surveys, risk assessments, post orders,
  deployment planning.
- Supervision & Reporting: field supervisors, shift audits, incident reporting.

OTHER FACTS
- Officers are screened, licensed, uniformed, trained and supervised.
- Technology partners: Ajax, Hikvision, Rasilient.
- Clients include Xcite, Millennium Hotels and Resorts, and Alnasser.
- A free site survey is the normal first step for a new enquiry.
"""

CHAT_RULES = """
RULES
- Answer ONLY questions about AZSCO, its security manpower services, and how to
  get in touch. For anything else, politely say it is outside what you can help
  with and offer to put the visitor in touch with the team.
- Use ONLY the facts above. If you do not know something - pricing, guard
  numbers, availability, contract terms, staff names - say so plainly and point
  the visitor to (+965) 1808606 or info@azsco.com. Never guess or invent.
- AZSCO does not install or maintain security systems. If asked for CCTV, alarm
  or access control installation, say AZSCO provides security personnel and
  suggest contacting the team to discuss what they need.
- Never quote a price, promise a response time, or commit AZSCO to anything.
- Be brief: two or three short paragraphs at most. Plain text, no markdown
  headings or bullet lists.
- If a visitor appears to have an urgent security incident, tell them to call
  (+965) 1808606 immediately rather than continuing to chat.
"""

def chat_system_prompt(lang):
    reply_in = ("Reply in Arabic (Modern Standard Arabic), in a professional tone."
                if lang == "ar" else
                "Reply in English, in a professional tone.")
    return ("You are the AZSCO Assistant, the virtual assistant on the website of "
            "AZSCO, a security manpower company in Kuwait.\n"
            + CHAT_FACTS + CHAT_RULES + "- " + reply_in)
FOUNDED = 2008
YEARS = datetime.date.today().year - FOUNDED

# Every visible string is a pair: (English, Arabic).
def t(pair, lang):
    return pair[0] if lang == "en" else pair[1]

def lang_attrs(lang):
    return 'lang="ar" dir="rtl"' if lang == "ar" else 'lang="en" dir="ltr"'

def asset(lang, path):
    """Arabic pages live in /ar/, so shared assets need one level up."""
    return ("../" + path) if lang == "ar" else path

def page_url(lang, fname):
    """Link between pages within the same language."""
    return fname

def other_lang_url(lang, fname):
    """The same page in the other language."""
    return ("../" + fname) if lang == "ar" else ("ar/" + fname)

def canonical(lang, fname):
    base = "https://www.azsco.com/"
    path = "" if fname == "index.html" else fname
    return base + ("ar/" if lang == "ar" else "") + path
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

I["chat"] = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-3.3-.6L3 21l1.8-5a8.3 8.3 0 0 1-.8-3.6'
             'A8.4 8.4 0 0 1 12.5 3 8.4 8.4 0 0 1 21 11.5z"/></svg>')

I["expand"] = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
               'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-7 7"/><path d="M3 21l7-7"/></svg>')

I["send"] = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M22 2 11 13"/><path d="M22 2l-7 20-4-9-9-4z"/></svg>')

I["globe"] = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
              'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
              '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
              '<path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18z"/></svg>')
def logo(variant="dark"):
    """Brand lockup. `dark` is the black artwork for light backgrounds;
    `light` is the white artwork used on dark backgrounds (the footer)."""
    src = "AZSCO_Logo_white.png" if variant == "light" else "AZSCO_Logo.png"
    return ('<img class="brand-logo" src="assets/img/%s" '
            'alt="AZSCO Security" width="1730" height="798">' % src)


# ============================================================ shared strings
COMPANY   = ("AZSCO for Facility Guard Services", "شركة أزسكو لخدمات حراسة المنشآت")
SITE_NAME = ("AZSCO Security", "أزسكو للأمن")
TAGLINE   = ("Security &amp; Guarding", "الأمن والحراسة")
ADDRESS_1L = ("Floor 27, Kuwait Building Tower, Fahad Al Salem St., Qibla, Kuwait",
              "الدور 27، برج مبنى الكويت، شارع فهد السالم، القبلة، الكويت")
ADDRESS_BR = ("Floor 27, Kuwait Building Tower,<br>Fahad Al Salem St., Qibla, Kuwait",
              "الدور 27، برج مبنى الكويت،<br>شارع فهد السالم، القبلة، الكويت")
HOURS      = ("Sunday &ndash; Thursday, 8:00 &ndash; 17:00", "الأحد &ndash; الخميس، 8:00 &ndash; 17:00")
HOURS_FOOT = ("Sunday &ndash; Thursday, 8:00 &ndash; 17:00<br>Emergency response 24/7",
              "الأحد &ndash; الخميس، 8:00 &ndash; 17:00<br>استجابة الطوارئ على مدار الساعة")
RESPONSE_24 = ("24/7 Response", "استجابة على مدار الساعة")
LANG_SWITCH = ("العربية", "English")
LANG_SWITCH_SHORT = ("ع", "EN")
LANG_SWITCH_LABEL = ("Switch to Arabic", "التبديل إلى الإنجليزية")

UI = {
    "quote":      ("Get a Quote", "اطلب عرض سعر"),
    "consult":    ("Request a Consultation", "اطلب استشارة"),
    "consult_m":  ("Request a Consultation", "اطلب استشارة"),
    "learn":      ("Learn more", "اعرف المزيد"),
    "more_about": ("More About Us", "المزيد عنّا"),
    "explore":    ("Explore Our Services", "تصفّح خدماتنا"),
    "talk":       ("Talk to Our Team", "تحدّث مع فريقنا"),
    "req_quote":  ("Request a Quote", "اطلب عرض سعر"),
    "home":       ("Home", "الرئيسية"),
    "menu_open":  ("Open menu", "فتح القائمة"),
    "menu_close": ("Close menu", "إغلاق القائمة"),
    "to_top":     ("Back to top", "العودة إلى الأعلى"),
    "skip":       ("Skip to content", "تخطّي إلى المحتوى"),
    "call_now":   ("Call Now", "اتصل الآن"),
    "get_quote":  ("Get a Quote", "عرض سعر"),
    "call_us":    ("Call us anytime", "اتصل بنا في أي وقت"),
    "social":     ("AZSCO on social media", "أزسكو على وسائل التواصل"),
    "map_label":  ("AZSCO office location on Google Maps (opens in a new tab)",
                   "موقع مكتب أزسكو على خرائط جوجل (يفتح في تبويب جديد)"),
    "home_label": ("AZSCO Security — home", "أزسكو للأمن — الصفحة الرئيسية"),
    "main_nav":   ("Main navigation", "التنقل الرئيسي"),
    "mob_nav":    ("Mobile navigation", "قائمة التنقل للجوال"),
}

CHAT = {
  "launcher": ("AZSCO Assistant", "مساعد أزسكو"),
  "title": ("AZSCO Assistant", "مساعد أزسكو"),
  "sub": ("Ask about our security services", "اسأل عن خدماتنا الأمنية"),
  "greeting": ("Hello. I am the AZSCO Assistant. What can I help you with today? You can ask about our guarding services, the areas we cover, or how to request a quote.",
               "مرحباً. أنا مساعد أزسكو. كيف يمكنني مساعدتك اليوم؟ يمكنك السؤال عن خدمات الحراسة لدينا، أو المناطق التي نغطيها، أو كيفية طلب عرض سعر."),
  "placeholder": ("Type your question&hellip;", "اكتب سؤالك&hellip;"),
  "send": ("Send message", "إرسال الرسالة"),
  "close": ("Close assistant", "إغلاق المساعد"),
  "expand": ("Expand assistant", "توسيع المساعد"),
  "collapse": ("Collapse assistant", "تصغير المساعد"),
  "open": ("Open the AZSCO Assistant", "فتح مساعد أزسكو"),
  "suggest": [
    ("What services do you offer?", "ما الخدمات التي تقدّمونها؟"),
    ("How do I request a quote?", "كيف أطلب عرض سعر؟"),
    ("What areas do you cover?", "ما المناطق التي تغطونها؟"),
  ],
  "error": ("Sorry, I could not reach the assistant just now. Please try again, or contact our team directly on (+965) 1808606 or info@azsco.com.",
            "عذراً، تعذّر الوصول إلى المساعد في الوقت الحالي. يُرجى المحاولة مرة أخرى، أو التواصل مع فريقنا مباشرة على (+965) 1808606 أو info@azsco.com."),
  "offline": ("The assistant is not connected yet. Please contact our team on (+965) 1808606 or info@azsco.com and we will be glad to help.",
              "لم يتم تفعيل المساعد بعد. يُرجى التواصل مع فريقنا على (+965) 1808606 أو info@azsco.com وسيسعدنا مساعدتك."),
  "foot": ("AI assistant — may be inaccurate. For anything binding, contact our team.",
           "مساعد ذكاء اصطناعي — قد تكون إجاباته غير دقيقة. لأي أمر مُلزم يُرجى التواصل مع فريقنا."),
}

# No "Home" item: the logo links to the home page in both the header and the
# mobile drawer, so a separate entry would be a second route to the same place.
NAV = [
    (("About", "من نحن"), "about.html", []),
    (("Services", "خدماتنا"), "services.html", [
        (("All Services", "جميع الخدمات"), "services.html"),
        (("Manned Guarding", "الحراسة الأمنية"), "services.html#guarding"),
        (("Mobile Patrols", "الدوريات المتنقلة"), "services.html#patrols"),
        (("Event &amp; VIP Security", "أمن الفعاليات وكبار الشخصيات"), "services.html#events"),
        (("Reception &amp; Concierge", "الاستقبال والكونسيرج"), "services.html#reception"),
        (("Security Consulting", "الاستشارات الأمنية"), "services.html#consulting"),
        (("Supervision &amp; Reporting", "الإشراف والتقارير"), "services.html#supervision"),
    ]),
    (("Partners", "شركاؤنا"), "partners.html", []),
    (("Contact", "اتصل بنا"), "contact.html", []),
]

FOOTER = {
    "blurb": ("AZSCO for facility guard services has been protecting premises, assets and people across Kuwait since 2008, with professionally trained, licensed and closely supervised security personnel.",
              "تعمل شركة أزسكو لخدمات حراسة المنشآت على حماية المنشآت والممتلكات والأشخاص في جميع أنحاء الكويت منذ عام 2008، بكوادر أمنية مدرّبة ومرخّصة وتخضع لإشراف دقيق."),
    "company": ("Company", "الشركة"),
    "services": ("Services", "الخدمات"),
    "touch": ("Get In Touch", "تواصل معنا"),
  "email_general": ("General enquiries", "الاستفسارات العامة"),
  "email_sales": ("Sales &amp; quotations", "المبيعات وعروض الأسعار"),
    "links": [
        (("Home", "الرئيسية"), "index.html"),
        (("About AZSCO", "عن أزسكو"), "about.html"),
        (("Our Services", "خدماتنا"), "services.html"),
        (("Our Partners", "شركاؤنا"), "partners.html"),
        (("Contact Us", "اتصل بنا"), "contact.html"),
    ],
    "rights": ("All rights reserved.", "جميع الحقوق محفوظة."),
    "privacy": ("Privacy Policy", "سياسة الخصوصية"),
    "contact": ("Contact", "اتصل بنا"),
}

CTA_DEFAULT = (
    ("Ready to secure what matters most?", "هل أنت مستعد لحماية ما يهمّك؟"),
    ("Talk to an AZSCO security consultant about a site survey and a tailored proposal for your premises.",
     "تحدّث مع مستشار أمني من أزسكو حول معاينة الموقع وإعداد عرض مخصّص لمنشأتك."),
)

# ============================================================ services
SERVICES = [
  {"anchor": "guarding", "icon": "shield",
   "name": ("Manned Guarding", "الحراسة الأمنية"),
   "card": ("Highly trained and professional security officers safeguarding your premises, assets and people &mdash; security guards for apartments, malls, banks, stores and much more.",
            "أفراد أمن محترفون وعلى درجة عالية من التدريب لحماية منشآتك وممتلكاتك والعاملين فيها &mdash; حراس أمن للشقق والمجمّعات التجارية والبنوك والمتاجر وغيرها الكثير."),
   "intro": ("Highly trained and professional security personnel to safeguard your premises, assets and people. AZSCO is distinguished in offering security guards for apartments, malls, banks, stores and much more, with deployments tailored to each client.",
             "كوادر أمنية مدرّبة ومحترفة لحماية منشآتك وممتلكاتك والعاملين فيها. تتميّز أزسكو بتوفير حراس الأمن للشقق والمجمّعات التجارية والبنوك والمتاجر وغيرها الكثير، مع خطط انتشار مصمّمة لكل عميل."),
   "points": [
     ("Static officers for towers, compounds, retail and industrial sites", "أفراد أمن ثابتون للأبراج والمجمّعات والمنشآت التجارية والصناعية"),
     ("Screened, licensed and uniformed personnel", "كوادر مدقّقة أمنياً ومرخّصة وبزي رسمي"),
     ("Site-specific post orders and access procedures", "تعليمات مواقع وإجراءات دخول خاصة بكل منشأة"),
     ("Day, night and rotating shift patterns", "ورديات صباحية وليلية ودوّارة"),
     ("Daily occurrence books and incident reporting", "سجلات يومية وتقارير عن الحوادث"),
   ]},
  {"anchor": "patrols", "icon": "route",
   "name": ("Mobile Patrols", "الدوريات المتنقلة"),
   "card": ("Scheduled and random patrols, perimeter checks and lock-and-unlock services that keep a visible, unpredictable security presence across your site.",
            "دوريات مجدولة وعشوائية، وفحص للأسوار الخارجية، وخدمات الفتح والإغلاق، للحفاظ على حضور أمني ظاهر ويصعب التنبؤ به في موقعك."),
   "intro": ("A visible, unpredictable security presence for sites that do not need a permanent post &mdash; or an added layer of assurance for those that do.",
             "حضور أمني ظاهر ويصعب التنبؤ به للمواقع التي لا تحتاج إلى نقطة حراسة دائمة &mdash; أو طبقة حماية إضافية للمواقع التي تحتاجها."),
   "points": [
     ("Scheduled and random patrol visits", "زيارات دوريات مجدولة وعشوائية"),
     ("Perimeter, car park and stairwell checks", "فحص الأسوار ومواقف السيارات والسلالم"),
     ("Lock-and-unlock and key-holding services", "خدمات الفتح والإغلاق وحفظ المفاتيح"),
     ("Alarm response and escalation to key holders", "الاستجابة للإنذارات وإبلاغ حاملي المفاتيح"),
     ("Time-stamped patrol reports for every visit", "تقارير دوريات موثّقة بالوقت لكل زيارة"),
   ]},
  {"anchor": "events", "icon": "calendar",
   "name": ("Event &amp; VIP Security", "أمن الفعاليات وكبار الشخصيات"),
   "card": ("Crowd management, access screening, stewarding and close protection for exhibitions, conferences, private functions and VIP visits.",
            "إدارة الحشود، وتفتيش الدخول، والتنظيم، والحماية الشخصية للمعارض والمؤتمرات والمناسبات الخاصة وزيارات كبار الشخصيات."),
   "intro": ("Officers who keep an event running smoothly and safely, from access screening at the door to close protection for principals.",
             "أفراد أمن يضمنون سير الفعالية بسلاسة وأمان، من تفتيش الدخول عند الباب إلى الحماية الشخصية للشخصيات المهمة."),
   "points": [
     ("Crowd management and queue control", "إدارة الحشود وتنظيم الصفوف"),
     ("Access screening, accreditation and door supervision", "تفتيش الدخول والتصاريح والإشراف على الأبواب"),
     ("Exhibition, conference and private function stewarding", "تنظيم المعارض والمؤتمرات والمناسبات الخاصة"),
     ("VIP and close protection details", "فرق حماية كبار الشخصيات والحماية الشخصية"),
     ("Pre-event risk assessment and deployment plan", "تقييم المخاطر وخطة الانتشار قبل الفعالية"),
   ]},
  {"anchor": "reception", "icon": "users",
   "name": ("Reception &amp; Concierge", "الاستقبال والكونسيرج"),
   "card": ("Front-of-house officers who combine entry control and visitor management with the courtesy your staff, residents and guests expect.",
            "أفراد استقبال يجمعون بين ضبط الدخول وإدارة الزوار وحسن التعامل الذي يتوقعه موظفوك وسكانك وضيوفك."),
   "intro": ("Front-of-house security that protects the building without making visitors feel policed &mdash; the first impression as well as the first line of defence.",
             "أمن الواجهة الأمامية الذي يحمي المبنى دون أن يشعر الزائر بالمراقبة &mdash; الانطباع الأول وخط الدفاع الأول في آنٍ واحد."),
   "points": [
     ("Reception, lobby and concierge posts", "نقاط الاستقبال والبهو والكونسيرج"),
     ("Visitor registration, badging and escorting", "تسجيل الزوار وإصدار البطاقات ومرافقتهم"),
     ("Contractor and delivery control", "ضبط دخول المقاولين وعمليات التوصيل"),
     ("Entry control and key management", "ضبط الدخول وإدارة المفاتيح"),
     ("Customer-service training alongside security training", "تدريب على خدمة العملاء إلى جانب التدريب الأمني"),
   ]},
  {"anchor": "consulting", "icon": "file",
   "name": ("Security Consulting", "الاستشارات الأمنية"),
   "card": ("Site surveys, risk assessments, post orders and deployment planning, so your security spend goes where the risk actually is.",
            "معاينات للمواقع، وتقييم للمخاطر، وتعليمات للمواقع، وتخطيط للانتشار، ليذهب إنفاقك الأمني إلى حيث تكمن المخاطر فعلاً."),
   "intro": ("Independent assessment of your risk, followed by a practical plan. We help you decide what to protect, how, and in what order.",
             "تقييم مستقل للمخاطر يتبعه خطة عملية. نساعدك على تحديد ما يجب حمايته، وكيف، وبأي ترتيب."),
   "points": [
     ("Site surveys and vulnerability assessments", "معاينات المواقع وتقييم نقاط الضعف"),
     ("Security policies, procedures and post orders", "السياسات والإجراءات الأمنية وتعليمات المواقع"),
     ("Manpower deployment and shift planning", "تخطيط انتشار الكوادر وجدولة الورديات"),
     ("Tender and contract specification support", "دعم إعداد مواصفات المناقصات والعقود"),
     ("Post-incident review and recommendations", "مراجعة ما بعد الحوادث وتقديم التوصيات"),
   ]},
  {"anchor": "supervision", "icon": "headset",
   "name": ("Supervision &amp; Reporting", "الإشراف والتقارير"),
   "card": ("Field supervisors, shift audits and documented incident reporting, with a team available 24 hours a day, 7 days a week.",
            "مشرفون ميدانيون، وتدقيق للورديات، وتقارير موثّقة للحوادث، مع فريق متاح على مدار 24 ساعة طوال أيام الأسبوع."),
   "intro": ("The difference between a guard on site and a managed security contract: supervision, auditing and a record you can rely on.",
             "الفرق بين وجود حارس في الموقع وعقد أمني مُدار: الإشراف والتدقيق وسجل يمكن الاعتماد عليه."),
   "points": [
     ("Field supervisors and unannounced shift audits", "مشرفون ميدانيون وتدقيق مفاجئ للورديات"),
     ("24/7 operations contact for escalations", "تواصل تشغيلي على مدار الساعة للحالات الطارئة"),
     ("Documented incident and occurrence reporting", "تقارير موثّقة للحوادث والوقائع"),
     ("Attendance monitoring and shift cover", "متابعة الحضور وتغطية الورديات"),
     ("Regular service reviews with the client", "مراجعات دورية للخدمة مع العميل"),
   ]},
]

SECTORS = [
    ("home",     ("Apartments &amp; Compounds", "الشقق والمجمّعات السكنية")),
    ("grid",     ("Malls &amp; Retail", "المجمّعات التجارية والمتاجر")),
    ("wallet",   ("Banks &amp; Financial", "البنوك والمؤسسات المالية")),
    ("file",     ("Offices &amp; Corporate", "المكاتب والشركات")),
    ("cog",      ("Industrial &amp; Logistics", "المنشآت الصناعية واللوجستية")),
    ("calendar", ("Events &amp; Exhibitions", "الفعاليات والمعارض")),
]

PARTNERS = ["Ajax", "Hikvision", "Rasilient"]
CLIENTS = [("Xcite", "إكسايت"), ("Millennium Hotels and Resorts", "ميلينيوم للفنادق والمنتجعات"), ("Alnasser", "النصر")]
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

# ============================================================ home
HOME = {
  "title": ("AZSCO Security | Professional Security Services for Kuwait",
            "أزسكو للأمن | خدمات أمنية احترافية في الكويت"),
  "desc": ("AZSCO for facility guard services provides professional security manpower in Kuwait since 2008 — manned guarding, mobile patrols, event and VIP security, reception and concierge, security consulting and 24/7 supervision.",
           "تقدّم شركة أزسكو لخدمات حراسة المنشآت كوادر أمنية احترافية في الكويت منذ عام 2008 — حراسة أمنية، ودوريات متنقلة، وأمن الفعاليات وكبار الشخصيات، والاستقبال والكونسيرج، والاستشارات الأمنية، وإشراف على مدار الساعة."),
  "badge": ("Licensed Security Provider &mdash; Kuwait", "مزوّد خدمات أمنية مرخّص &mdash; الكويت"),
  "h1a": ("Professional Security", "خدمات أمنية"),
  "h1b": ("Services for Kuwait", "احترافية في الكويت"),
  "lead": ("AZSCO is committed to providing unparalleled security services that ensure the safety and peace of mind of our clients &mdash; delivered by highly trained, licensed and closely supervised security personnel.",
           "تلتزم أزسكو بتقديم خدمات أمنية لا تُضاهى تضمن سلامة عملائنا وراحة بالهم &mdash; عبر كوادر أمنية مدرّبة تدريباً عالياً ومرخّصة وتخضع لإشراف دقيق."),
  "points": [("Guarding Kuwait since 2008", "نحرس الكويت منذ عام 2008"),
             ("Licensed &amp; vetted personnel", "كوادر مرخّصة ومدقّقة أمنياً"),
             ("24/7 supervision &amp; response", "إشراف واستجابة على مدار الساعة")],
  "card_h": ("What We Guard", "ما الذي نحرسه"),
  "card_p": ("Security officers for every kind of premises across Kuwait.",
             "أفراد أمن لجميع أنواع المنشآت في جميع أنحاء الكويت."),
  "card_items": [
    ("shield", ("Manned Guarding", "الحراسة الأمنية"),
     ("Static officers for apartments, malls, banks and stores.", "أفراد أمن ثابتون للشقق والمجمّعات التجارية والبنوك والمتاجر.")),
    ("route", ("Mobile Patrols", "الدوريات المتنقلة"),
     ("Scheduled and random patrols, day and night.", "دوريات مجدولة وعشوائية، نهاراً وليلاً.")),
    ("calendar", ("Event &amp; VIP Security", "أمن الفعاليات وكبار الشخصيات"),
     ("Crowd management, screening and close protection.", "إدارة الحشود والتفتيش والحماية الشخصية.")),
  ],
  "svc_eyebrow": ("Our Services", "خدماتنا"),
  "svc_h2": ("Our Security Services", "خدماتنا الأمنية"),
  "svc_lead": ("From manned guarding to mobile patrols and event security, every deployment is tailored to the specific requirements of each client.",
               "من الحراسة الأمنية إلى الدوريات المتنقلة وأمن الفعاليات، تُصمَّم كل خطة انتشار وفق متطلبات كل عميل على حدة."),
  "about_eyebrow": ("About AZSCO", "عن أزسكو"),
  "about_h2": ("A Leading Provider of Security Services in Kuwait", "مزوّد رائد للخدمات الأمنية في الكويت"),
  "about_lead": ("AZSCO for facility guard services was established in 2008 and is headquartered in Qibla, Kuwait. Our team of highly trained and experienced security professionals is equipped with the latest technology and equipment to ensure the safety of your property and assets.",
                 "تأسّست شركة أزسكو لخدمات حراسة المنشآت عام 2008 ويقع مقرّها في القبلة بالكويت. ويضمّ فريقنا كوادر أمنية مدرّبة وذات خبرة، مجهّزة بأحدث التقنيات والمعدات لضمان سلامة ممتلكاتك وأصولك."),
  "about_checks": [
    (("Customized solutions", "حلول مخصّصة"),
     ("We understand that every client has unique security needs, and tailor our solutions to the specific requirements of each site.",
      "ندرك أن لكل عميل احتياجات أمنية فريدة، ولذلك نصمّم حلولنا وفق متطلبات كل موقع.")),
    (("Cost-effective and efficient", "فعّالة من حيث التكلفة والكفاءة"),
     ("Our goal is to provide the highest level of security and peace of mind, while keeping our services efficient and affordable.",
      "هدفنا تقديم أعلى مستوى من الأمن وراحة البال، مع الحفاظ على كفاءة خدماتنا وتكلفتها المعقولة.")),
    (("Available around the clock", "متاحون على مدار الساعة"),
     ("Our team of dedicated professionals is available 24 hours a day, 7 days a week.",
      "فريقنا من المتخصصين المتفانين متاح على مدار 24 ساعة طوال أيام الأسبوع.")),
  ],
  "sec_eyebrow": ("Where We Guard", "أين نحرس"),
  "sec_h2": ("Sectors We Protect", "القطاعات التي نحميها"),
  "sec_lead": ("AZSCO is distinguished in offering security services such as security guards for apartments, malls, banks, stores and much more.",
               "تتميّز أزسكو بتقديم خدمات أمنية مثل حراس الأمن للشقق والمجمّعات التجارية والبنوك والمتاجر وغيرها الكثير."),
  "why_eyebrow": ("Why AZSCO", "لماذا أزسكو"),
  "why_h2": ("Why Clients Choose Us", "لماذا يختارنا العملاء"),
  "why_lead": ("A strong reputation for quality and reliability, built on people, technology and accountability.",
               "سمعة قوية في الجودة والموثوقية، مبنية على الكوادر والتقنية والمساءلة."),
  "why_tiles": [
    ("award", ("Proven Reputation", "سمعة راسخة"),
     ("A leading provider of security services in Kuwait, trusted for quality and reliability across commercial, industrial and residential sites.",
      "مزوّد رائد للخدمات الأمنية في الكويت، موثوق به في الجودة والموثوقية عبر المواقع التجارية والصناعية والسكنية.")),
    ("users", ("Trained Professionals", "كوادر مدرّبة"),
     ("Highly trained and experienced security personnel, screened, licensed and supervised to a consistent operating standard.",
      "كوادر أمنية مدرّبة وذات خبرة، مدقّقة أمنياً ومرخّصة وتخضع لإشراف وفق معيار تشغيلي ثابت.")),
    ("award2", ("Established 2008", "تأسّست عام 2008"),
     ("Guarding Kuwait for over {YEARS} years, with continuous growth that testifies to our commitment to excellence.",
      "نحرس الكويت منذ أكثر من {YEARS} عاماً، بنموّ متواصل يشهد على التزامنا بالتميّز.")),
    ("target", ("Tailored to You", "مصمّمة لك"),
     ("Every client has unique security needs. We design customized solutions around your risk profile, site and operating hours.",
      "لكل عميل احتياجات أمنية فريدة. نصمّم حلولاً مخصّصة وفق مستوى المخاطر لديك وموقعك وساعات عملك.")),
    ("wallet", ("Cost-Effective", "فعّالة من حيث التكلفة"),
     ("The highest level of security and peace of mind, delivered in a way that stays efficient and commercially sensible.",
      "أعلى مستوى من الأمن وراحة البال، مقدَّم بأسلوب يحافظ على الكفاءة والجدوى التجارية.")),
    ("headset", ("24/7 Availability", "متاحون على مدار الساعة"),
     ("Our dedicated professionals are available 24 hours a day, 7 days a week &mdash; for supervision, response and support.",
      "متخصصونا المتفانون متاحون على مدار 24 ساعة طوال أيام الأسبوع &mdash; للإشراف والاستجابة والدعم.")),
  ],
  "proc_eyebrow": ("How We Work", "كيف نعمل"),
  "proc_h2": ("Our Process", "آلية عملنا"),
  "proc_lead": ("A straightforward path from first conversation to a protected, maintained site.",
                "مسار واضح من أول حديث حتى موقع محمي ومُدار."),
  "steps": [
    (("Consultation", "الاستشارة"), ("We listen to your requirements, operating hours and concerns to understand what actually needs protecting.",
      "نستمع إلى متطلباتك وساعات عملك ومخاوفك لنفهم ما يحتاج فعلاً إلى الحماية.")),
    (("Site Survey", "معاينة الموقع"), ("Our specialists assess the premises, identify vulnerabilities and map patrol routes, access points and risk.",
      "يقيّم مختصّونا المنشأة ويحدّدون نقاط الضعف ويرسمون مسارات الدوريات ونقاط الدخول والمخاطر.")),
    (("Tailored Proposal", "عرض مخصّص"), ("You receive a clear deployment plan and quotation &mdash; posts, shifts and cover &mdash; scoped to your budget.",
      "تحصل على خطة انتشار وعرض سعر واضحين &mdash; النقاط والورديات والتغطية &mdash; ضمن ميزانيتك.")),
    (("Deploy &amp; Supervise", "الانتشار والإشراف"), ("Officers are briefed and deployed, then supervised and audited with 24/7 support behind them.",
      "يتم إحاطة الأفراد ونشرهم، ثم الإشراف عليهم وتدقيق عملهم بدعم متواصل على مدار الساعة.")),
  ],
  "part_eyebrow": ("Our Partners", "شركاؤنا"),
  "part_h2": ("Strategic Partnerships", "شراكات استراتيجية"),
  "part_lead": ("AZSCO has established strategic partnerships with leading industry players to enhance the range and quality of our security solutions.",
                "أقامت أزسكو شراكات استراتيجية مع كبرى الشركات في القطاع لتعزيز نطاق وجودة حلولنا الأمنية."),
  "part_btn": ("About Our Partnerships", "عن شراكاتنا"),
}

STATS = [
    ("founded", ("Established in Kuwait", "تأسّست في الكويت")),
    ("years",   ("Years of Experience", "عاماً من الخبرة")),
    ("247",     ("Monitoring &amp; Response", "المتابعة والاستجابة")),
    ("partners",("Technology Partners", "شركاء التقنية")),
]

# ============================================================ about
ABOUT = {
  "title": ("About Us | AZSCO Security Kuwait", "من نحن | أزسكو للأمن الكويت"),
  "desc": ("AZSCO for facility guard services was established in 2008 in Qibla, Kuwait, offering security guards for apartments, malls, banks, stores and much more.",
           "تأسّست شركة أزسكو لخدمات حراسة المنشآت عام 2008 في القبلة بالكويت، وتقدّم حراس أمن للشقق والمجمّعات التجارية والبنوك والمتاجر وغيرها الكثير."),
  "banner_h": ("About AZSCO", "عن أزسكو"),
  "banner_p": ("A leading provider of security services in Kuwait, with a strong reputation for quality and reliability.",
               "مزوّد رائد للخدمات الأمنية في الكويت، بسمعة قوية في الجودة والموثوقية."),
  "crumb": ("About", "من نحن"),
  "story_eyebrow": ("Our Story", "قصّتنا"),
  "story_h2": ("Protecting Kuwait Since 2008", "نحمي الكويت منذ عام 2008"),
  "story": [
    ("AZSCO for facility guard services was established in 2008 and is headquartered in Qibla, Kuwait. Since its inception, AZSCO has been committed to providing its customers with state of the art security and prosperity bringing peace to places that are vulnerable. Additionally, AZSCO&rsquo;s team works on improving the security solutions that is offered to our beloved customers.",
     "تأسّست شركة أزسكو لخدمات حراسة المنشآت عام 2008 ويقع مقرّها في القبلة بالكويت. ومنذ انطلاقتها، التزمت أزسكو بتزويد عملائها بأحدث حلول الأمن والازدهار، لتبعث الطمأنينة في الأماكن المعرّضة للخطر. كما يعمل فريق أزسكو باستمرار على تطوير الحلول الأمنية المقدَّمة لعملائنا الكرام."),
    ("AZSCO is distinguished in offering security services such as security guards for apartments, malls, banks, stores and much more. AZSCO has partnerships with many global brands to provide unique products and solutions for projects.",
     "تتميّز أزسكو بتقديم خدمات أمنية مثل حراس الأمن للشقق والمجمّعات التجارية والبنوك والمتاجر وغيرها الكثير. ولدى أزسكو شراكات مع العديد من العلامات التجارية العالمية لتوفير منتجات وحلول مميّزة للمشاريع."),
    ("AZSCO is committed to building long-term relationships with its clients in both the public and private sectors, based on trust, cooperation, and development, with a focus on executing its projects with efficiency and high quality. Its success and continuous growth testify to its commitment to excellence and innovation in providing solutions and products to its clients.",
     "تلتزم أزسكو ببناء علاقات طويلة الأمد مع عملائها في القطاعين العام والخاص، قائمة على الثقة والتعاون والتطوير، مع التركيز على تنفيذ مشاريعها بكفاءة وجودة عالية. ويشهد نجاحها ونموّها المستمر على التزامها بالتميّز والابتكار في تقديم الحلول والمنتجات لعملائها."),
  ],
  "badge": (("2008", "2008"), ("Established", "سنة التأسيس")),
  "mvv": [
    ("target", ("Our Mission", "رسالتنا"),
     ("To provide the highest level of security and peace of mind for every client, while ensuring that our services remain cost-effective and efficient.",
      "تقديم أعلى مستوى من الأمن وراحة البال لكل عميل، مع ضمان بقاء خدماتنا فعّالة من حيث التكلفة والكفاءة.")),
    ("eye", ("Our Vision", "رؤيتنا"),
     ("To be Kuwait&rsquo;s most trusted security partner &mdash; recognised for quality, reliability and the strength of the people we put on the ground.",
      "أن نكون الشريك الأمني الأكثر ثقة في الكويت &mdash; معروفين بالجودة والموثوقية وكفاءة الكوادر التي ننشرها في الميدان.")),
    ("shield-check", ("Our Values", "قيمنا"),
     ("Integrity, vigilance and accountability. We understand that every client has unique security needs, and we tailor our solutions to meet them exactly.",
      "النزاهة واليقظة والمساءلة. ندرك أن لكل عميل احتياجات أمنية فريدة، ونصمّم حلولنا لتلبيتها بدقة.")),
  ],
  "commit_eyebrow": ("What Sets Us Apart", "ما يميّزنا"),
  "commit_h2": ("Our Commitment", "التزامنا"),
  "commit_lead": ("Everything we do is measured against one standard: does it make our client safer?",
                  "كل ما نقوم به يُقاس بمعيار واحد: هل يجعل عميلنا أكثر أماناً؟"),
  "commit_tiles": [
    ("users", ("Highly Trained Personnel", "كوادر عالية التدريب"),
     ("Our security professionals are screened, licensed, trained and supervised &mdash; and equipped with what they need to do the job properly.",
      "كوادرنا الأمنية مدقّقة أمنياً ومرخّصة ومدرّبة وتخضع للإشراف &mdash; ومجهّزة بما تحتاجه لأداء العمل على أكمل وجه.")),
    ("route", ("Managed, Not Just Staffed", "إدارة لا مجرّد توفير أفراد"),
     ("Field supervisors, unannounced shift audits and documented reporting, so a contract is actively managed rather than simply filled.",
      "مشرفون ميدانيون وتدقيق مفاجئ للورديات وتقارير موثّقة، ليكون العقد مُداراً فعلياً لا مجرّد عقد مُنفَّذ.")),
    ("target", ("Customized Solutions", "حلول مخصّصة"),
     ("Every client has unique security needs. We survey, assess and plan deployments around your site rather than selling a fixed package.",
      "لكل عميل احتياجات أمنية فريدة. نعاين ونقيّم ونخطّط الانتشار وفق موقعك بدلاً من بيع باقة جاهزة.")),
    ("clock", ("Available 24/7", "متاحون على مدار الساعة"),
     ("Our team of dedicated professionals is available 24 hours a day, 7 days a week to provide the highest level of security and peace of mind.",
      "فريقنا من المتخصصين المتفانين متاح على مدار 24 ساعة طوال أيام الأسبوع لتقديم أعلى مستوى من الأمن وراحة البال.")),
  ],
  "ceo_eyebrow": ("A Word From Our Leadership", "كلمة من إدارتنا"),
  "ceo_h2": ("CEO&rsquo;s Message", "كلمة الرئيس التنفيذي"),
  "ceo": [
    ("Our commitment goes beyond merely achieving success and profitability at Almail Group. We believe in the importance of upholding our principles and values towards our employees, customers, and the community. Therefore, the owners of Almail Group prioritize the well-being and comfort of our employees and the development of our products and services.",
     "التزامنا يتجاوز مجرّد تحقيق النجاح والربحية في مجموعة الميّل. فنحن نؤمن بأهمية التمسّك بمبادئنا وقيمنا تجاه موظفينا وعملائنا والمجتمع. ولذلك يضع ملّاك مجموعة الميّل رفاهية موظفينا وراحتهم وتطوير منتجاتنا وخدماتنا في مقدمة أولوياتهم."),
    ("The employees of Almail Group are partners in our success and a fundamental part of achieving it. We always strive to provide a comfortable work environment without focusing on cost. We also work on continuous development and adopting modern technologies despite their high cost, as they enhance work efficiency and quality and contribute to delivering distinguished products and solutions to serve the community, thereby building strong and sustainable relationships with our customers.",
     "موظفو مجموعة الميّل شركاء في نجاحنا وجزء أساسي من تحقيقه. ونسعى دائماً إلى توفير بيئة عمل مريحة دون التركيز على التكلفة. كما نعمل على التطوير المستمر وتبنّي التقنيات الحديثة رغم ارتفاع كلفتها، لأنها تعزّز كفاءة العمل وجودته وتسهم في تقديم منتجات وحلول متميّزة تخدم المجتمع، وبذلك نبني علاقات قوية ومستدامة مع عملائنا."),
  ],
  "ceo_line": ("(Our Employees &mdash; Our Customers)", "(موظفونا &mdash; عملاؤنا)"),
  "ceo_thanks": ("Thank you for your trust in us, we thrive because of you.",
                 "شكراً لثقتكم بنا، فبكم نزدهر."),
  "ceo_by": ("CEO, Almail Group", "الرئيس التنفيذي، مجموعة الميّل"),
  "clients_eyebrow": ("Our Clients", "عملاؤنا"),
  "clients_h2": ("Trusted Across Kuwait", "موثوقون في جميع أنحاء الكويت"),
  "clients_lead": ("AZSCO is committed to building long-term relationships with its clients in both the public and private sectors.",
                   "تلتزم أزسكو ببناء علاقات طويلة الأمد مع عملائها في القطاعين العام والخاص."),
  "faq_eyebrow": ("Questions", "أسئلة"),
  "faq_h2": ("Frequently Asked", "الأسئلة الشائعة"),
  "faq": [
    (("What areas does AZSCO cover?", "ما المناطق التي تغطيها أزسكو؟"),
     ("AZSCO provides security manpower across Kuwait, from our office at {ADDR}. Call {PHONE} to discuss coverage for your site.",
      "توفّر أزسكو كوادر أمنية في جميع أنحاء الكويت، انطلاقاً من مكتبنا في {ADDR}. اتصل على {PHONE} لمناقشة تغطية موقعك.")),
    (("What kinds of premises do you guard?", "ما أنواع المنشآت التي تحرسونها؟"),
     ("AZSCO is distinguished in offering security services such as security guards for apartments, malls, banks, stores and much more, along with offices, compounds, industrial sites and events. Every deployment is planned around the specific requirements of the client.",
      "تتميّز أزسكو بتقديم خدمات أمنية مثل حراس الأمن للشقق والمجمّعات التجارية والبنوك والمتاجر وغيرها الكثير، إضافة إلى المكاتب والمجمّعات والمواقع الصناعية والفعاليات. وتُخطَّط كل عملية انتشار وفق متطلبات العميل تحديداً.")),
    (("How quickly can officers be deployed?", "ما السرعة التي يمكن بها نشر الأفراد؟"),
     ("Timelines depend on the number of posts, the shift pattern and any vetting the site requires. After a free site survey we issue a proposal with a clear deployment schedule, the officers assigned and the supervision arrangements that come with them.",
      "تعتمد المدة على عدد النقاط ونمط الورديات وأي تدقيق أمني يتطلبه الموقع. وبعد معاينة مجانية للموقع نصدر عرضاً يتضمّن جدولاً واضحاً للانتشار والأفراد المكلّفين وترتيبات الإشراف المرافقة لهم.")),
    (("Is support available outside working hours?", "هل الدعم متاح خارج ساعات العمل؟"),
     ("Our office hours are Sunday to Thursday, 8:00 to 17:00, but our team of dedicated professionals is available 24 hours a day, 7 days a week for supervision, emergency response and escalations.",
      "ساعات عمل مكتبنا من الأحد إلى الخميس، من 8:00 إلى 17:00، لكن فريقنا من المتخصصين متاح على مدار 24 ساعة طوال أيام الأسبوع للإشراف والاستجابة للطوارئ والحالات العاجلة.")),
  ],
}

# ============================================================ services page
SERVICES_PAGE = {
  "title": ("Security Manpower Services in Kuwait | AZSCO Security",
            "خدمات الكوادر الأمنية في الكويت | أزسكو للأمن"),
  "desc": ("AZSCO security manpower services in Kuwait: manned guarding, mobile patrols, event and VIP security, reception and concierge, security consulting, supervision and reporting.",
           "خدمات الكوادر الأمنية من أزسكو في الكويت: الحراسة الأمنية، والدوريات المتنقلة، وأمن الفعاليات وكبار الشخصيات، والاستقبال والكونسيرج، والاستشارات الأمنية، والإشراف والتقارير."),
  "banner_h": ("Our Services", "خدماتنا"),
  "banner_p": ("A comprehensive range of security manpower services — guarding, patrol services, event security and security consulting — tailored to each client.",
               "مجموعة شاملة من خدمات الكوادر الأمنية — الحراسة، وخدمات الدوريات، وأمن الفعاليات، والاستشارات الأمنية — مصمّمة لكل عميل."),
  "crumb": ("Services", "خدماتنا"),
  "over_eyebrow": ("Overview", "نظرة عامة"),
  "over_h2": ("What AZSCO Delivers", "ما تقدّمه أزسكو"),
  "over_lead": ("Every post, patrol and detail is planned around your premises, your operating hours and your risk &mdash; never a fixed package.",
                "تُخطَّط كل نقطة حراسة ودورية ومهمة وفق منشأتك وساعات عملك ومستوى المخاطر لديك &mdash; وليس وفق باقة جاهزة."),
  "service_label": ("Service", "الخدمة"),
  "people_eyebrow": ("Our People", "كوادرنا"),
  "people_h2": ("Trained, Vetted, Supervised", "مدرّبون، مدقّقون، تحت الإشراف"),
  "people_lead": ("The strength of a manned security contract is the standard behind every shift.",
                  "قوة عقد الحراسة الأمنية تكمن في المعيار الذي يقف خلف كل وردية."),
  "people_tiles": [
    ("shield-check", ("Screened &amp; Licensed", "مدقّقون ومرخّصون"),
     ("Every officer is background checked and licensed before deployment, and briefed on site-specific post orders.",
      "يخضع كل فرد للتدقيق الأمني والترخيص قبل نشره، ويُحاط بتعليمات الموقع الخاصة.")),
    ("award", ("Continuously Trained", "تدريب مستمر"),
     ("Ongoing training in entry control, emergency procedures, fire response, customer service and incident reporting.",
      "تدريب متواصل على ضبط الدخول وإجراءات الطوارئ والاستجابة للحرائق وخدمة العملاء وكتابة تقارير الحوادث.")),
    ("headset", ("Actively Supervised", "إشراف فعّال"),
     ("Field supervisors, shift audits and an operations team reachable 24 hours a day, 7 days a week.",
      "مشرفون ميدانيون وتدقيق للورديات وفريق عمليات يمكن الوصول إليه على مدار 24 ساعة طوال أيام الأسبوع.")),
  ],
  "cta": (("Not sure which service you need?", "لست متأكداً من الخدمة التي تحتاجها؟"),
          ("Book a free site survey. We will assess your premises and recommend the right deployment of officers, patrols and supervision.",
           "احجز معاينة مجانية للموقع. سنقيّم منشأتك ونوصي بالانتشار المناسب من الأفراد والدوريات والإشراف.")),
}

# ============================================================ partners page
PARTNERS_PAGE = {
  "title": ("Our Partners | AZSCO Security Kuwait", "شركاؤنا | أزسكو للأمن الكويت"),
  "desc": ("AZSCO has established strategic partnerships with leading industry players to enhance the range and quality of our security solutions in Kuwait.",
           "أقامت أزسكو شراكات استراتيجية مع كبرى الشركات في القطاع لتعزيز نطاق وجودة حلولنا الأمنية في الكويت."),
  "banner_h": ("Our Partners", "شركاؤنا"),
  "banner_p": ("AZSCO has established strategic partnerships with leading industry players to enhance the range and quality of our security solutions.",
               "أقامت أزسكو شراكات استراتيجية مع كبرى الشركات في القطاع لتعزيز نطاق وجودة حلولنا الأمنية."),
  "crumb": ("Partners", "شركاؤنا"),
  "eyebrow": ("Strategic Partnerships", "شراكات استراتيجية"),
  "h2": ("Backed by the Industry&rsquo;s Best", "بدعم من الأفضل في القطاع"),
  "lead": ("AZSCO has partnerships with many global brands to provide unique products and solutions for projects, supporting the sites our officers protect.",
           "لدى أزسكو شراكات مع العديد من العلامات التجارية العالمية لتوفير منتجات وحلول مميّزة للمشاريع، بما يدعم المواقع التي يحميها أفرادنا."),
  "why_eyebrow": ("Why It Matters", "لماذا يهمّ ذلك"),
  "why_h2": ("What Our Partnerships Give You", "ما الذي تمنحك إياه شراكاتنا"),
  "tiles": [
    ("award", ("Established Brands", "علامات تجارية راسخة"),
     ("We work with recognised global manufacturers, so the products specified on a project are supported and available for years.",
      "نتعامل مع مصنّعين عالميين معروفين، لتبقى المنتجات المعتمدة في المشروع مدعومة ومتوفّرة لسنوات.")),
    ("target", ("The Right Fit", "الخيار الأنسب"),
     ("Partnerships give us options, so each project gets the product that suits the site rather than the one we happen to stock.",
      "توفّر لنا الشراكات خيارات متعددة، ليحصل كل مشروع على المنتج الذي يناسب الموقع لا المنتج المتوفّر لدينا صدفة.")),
    ("users", ("Backing Our Officers", "دعم لأفرادنا"),
     ("Reliable equipment on site supports the officers guarding it, from the entry system at the door to the cameras they watch.",
      "المعدات الموثوقة في الموقع تدعم الأفراد الذين يحرسونه، من نظام الدخول عند الباب إلى الكاميرات التي يتابعونها.")),
  ],
  "join_eyebrow": ("Work With Us", "اعمل معنا"),
  "join_h2": ("Become an AZSCO Partner", "كن شريكاً لأزسكو"),
  "join_lead": ("We are always interested in working with manufacturers, distributors, consultants and contractors who share our standard of delivery.",
                "يسعدنا دائماً التعاون مع المصنّعين والموزّعين والاستشاريين والمقاولين الذين يشاركوننا معايير التنفيذ."),
  "join_p": ("If your products or services would strengthen what we offer clients in Kuwait, we would like to hear from you. Send an outline of your proposal to {EMAIL} or call {PHONE}.",
             "إذا كانت منتجاتك أو خدماتك تعزّز ما نقدّمه لعملائنا في الكويت، يسرّنا أن نسمع منك. أرسل ملخّصاً لعرضك إلى {EMAIL} أو اتصل على {PHONE}."),
  "join_btn": ("Start a Conversation", "ابدأ الحوار"),
}

# ============================================================ contact page
CONTACT = {
  "title": ("Contact AZSCO Security | Kuwait", "اتصل بأزسكو للأمن | الكويت"),
  "desc": ("Contact AZSCO Security in Kuwait. Office: Floor 27, Kuwait Building Tower, Fahad Al Salem St., Qibla, Kuwait. Tel (+965) 1808606. Email info@azsco.com. Request a free site survey.",
           "تواصل مع أزسكو للأمن في الكويت. المكتب: الدور 27، برج مبنى الكويت، شارع فهد السالم، القبلة، الكويت. هاتف (+965) 1808606. بريد إلكتروني info@azsco.com. اطلب معاينة مجانية للموقع."),
  "banner_h": ("Contact Us", "اتصل بنا"),
  "banner_p": ("Talk to AZSCO about guarding or a free site survey. Our team is available 24 hours a day, 7 days a week.",
               "تحدّث مع أزسكو حول خدمات الحراسة أو معاينة مجانية للموقع. فريقنا متاح على مدار 24 ساعة طوال أيام الأسبوع."),
  "crumb": ("Contact", "اتصل بنا"),
  "cards": [
    ("pin",  ("Visit Our Office", "زُر مكتبنا"), None),
    ("phone",("Call Us", "اتصل بنا"), ("24/7 emergency response", "استجابة للطوارئ على مدار الساعة")),
    ("mail", ("Email Us", "راسلنا"), None),
  ],
  "form_eyebrow": ("Get In Touch", "تواصل معنا"),
  "form_h2": ("Request a Free Site Survey", "اطلب معاينة مجانية للموقع"),
  "form_lead": ("Tell us a little about your premises and what you need protected. One of our security consultants will contact you to arrange a survey and prepare a tailored proposal.",
                "أخبرنا قليلاً عن منشأتك وما تحتاج إلى حمايته. سيتواصل معك أحد مستشارينا الأمنيين لترتيب المعاينة وإعداد عرض مخصّص."),
  "fields": {
    "name":    ("Full Name", "الاسم الكامل"),
    "name_ph": ("Your name", "اسمك"),
    "company": ("Company", "الشركة"),
    "company_ph": ("Company name", "اسم الشركة"),
    "email":   ("Email", "البريد الإلكتروني"),
    "phone":   ("Phone", "الهاتف"),
    "service": ("Service Required", "الخدمة المطلوبة"),
    "select":  ("Please select&hellip;", "اختر&hellip;"),
    "message": ("How Can We Help?", "كيف يمكننا مساعدتك؟"),
    "message_ph": ("Tell us about your site, the number of officers or posts you need, operating hours, and what you need protected.",
                   "أخبرنا عن موقعك، وعدد الأفراد أو النقاط التي تحتاجها، وساعات العمل، وما تريد حمايته."),
    "submit":  ("Send Enquiry", "إرسال الطلب"),
    "note":    ("By submitting this form you agree to our {PRIVACY}. For urgent matters please call {PHONE}.",
                "بإرسال هذا النموذج فإنك توافق على {PRIVACY}. وللأمور العاجلة يُرجى الاتصال على {PHONE}."),
    "req":     ("This field is required.", "هذا الحقل مطلوب."),
    "bad_email": ("Please enter a valid email address.", "يُرجى إدخال بريد إلكتروني صحيح."),
    "bad_phone": ("Please enter a valid phone number.", "يُرجى إدخال رقم هاتف صحيح."),
    "choose":  ("Please choose a service.", "يُرجى اختيار خدمة."),
  },
  "options": [
    ("Manned Guarding", "الحراسة الأمنية"),
    ("Mobile Patrols", "الدوريات المتنقلة"),
    ("Event &amp; VIP Security", "أمن الفعاليات وكبار الشخصيات"),
    ("Reception &amp; Concierge", "الاستقبال والكونسيرج"),
    ("Security Consulting", "الاستشارات الأمنية"),
    ("Supervision &amp; Reporting", "الإشراف والتقارير"),
    ("Other enquiry", "استفسار آخر"),
  ],
  "office_hours": ("Office hours", "ساعات العمل"),
  "emergency": ("Emergency response", "الاستجابة للطوارئ"),
  "emergency_v": ("Available 24 hours a day, 7 days a week", "متاحة على مدار 24 ساعة طوال أيام الأسبوع"),
  "cta": (("Prefer to speak to someone now?", "تفضّل التحدّث مع أحدهم الآن؟"),
          ("Our team is available 24 hours a day, 7 days a week for urgent security matters.",
           "فريقنا متاح على مدار 24 ساعة طوال أيام الأسبوع للأمور الأمنية العاجلة.")),
  "sent": ("Thank you for contacting AZSCO. Your request has been recorded — a member of our team will respond shortly. For urgent matters call (+965) 1808606.",
           "شكراً لتواصلك مع أزسكو. تم تسجيل طلبك وسيتواصل معك أحد أعضاء فريقنا قريباً. وللأمور العاجلة اتصل على (+965) 1808606."),
}

# ============================================================ 404
NOTFOUND = {
  "title": ("Page Not Found | AZSCO Security", "الصفحة غير موجودة | أزسكو للأمن"),
  "desc": ("The page you requested could not be found on the AZSCO Security website.",
           "الصفحة التي طلبتها غير موجودة على موقع أزسكو للأمن."),
  "eyebrow": ("Error 404", "خطأ 404"),
  "h1": ("Page Not Found", "الصفحة غير موجودة"),
  "lead": ("The page you are looking for may have been moved or no longer exists. Let us get you back to safety.",
           "ربما تم نقل الصفحة التي تبحث عنها أو لم تعد موجودة. دعنا نعيدك إلى برّ الأمان."),
  "back": ("Back to Home", "العودة إلى الرئيسية"),
  "contact": ("Contact Us", "اتصل بنا"),
}

# ============================================================ privacy policy
PRIVACY = {
  "title": ("Privacy Policy | AZSCO Security", "سياسة الخصوصية | أزسكو للأمن"),
  "desc": ("AZSCO Security privacy policy — how we collect, use, share and protect the personal information you provide through our website and services.",
           "سياسة الخصوصية لدى أزسكو للأمن — كيف نجمع المعلومات الشخصية التي تقدّمها عبر موقعنا وخدماتنا ونستخدمها ونشاركها ونحميها."),
  "banner_h": ("Privacy Policy", "سياسة الخصوصية"),
  "banner_p": ("How AZSCO collects, uses and protects the personal information you share with us.",
               "كيف تجمع أزسكو المعلومات الشخصية التي تشاركها معنا وتستخدمها وتحميها."),
  "crumb": ("Privacy Policy", "سياسة الخصوصية"),
  "updated": ("Last updated: January 2026", "آخر تحديث: يناير 2026"),
  "intro": ("{COMPANY} (&ldquo;AZSCO&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;) respects your privacy. This policy explains what personal information we collect through this website and our services, how we use it, and the choices available to you.",
            "تحترم {COMPANY} (&laquo;أزسكو&raquo;، &laquo;نحن&raquo;) خصوصيتك. توضّح هذه السياسة المعلومات الشخصية التي نجمعها عبر هذا الموقع وخدماتنا، وكيفية استخدامنا لها، والخيارات المتاحة أمامك."),
  "sections": [
    (("Information We Collect", "المعلومات التي نجمعها"),
     [("p", ("We collect information that you provide directly to us, and a limited amount of technical information collected automatically when you visit this website.",
             "نجمع المعلومات التي تقدّمها لنا مباشرة، وقدراً محدوداً من المعلومات التقنية التي تُجمع تلقائياً عند زيارتك لهذا الموقع.")),
      ("ul", [("<b>Information you provide:</b> your name, company, email address, telephone number, the service you are enquiring about, and any details you include in an enquiry or quotation request.",
               "<b>المعلومات التي تقدّمها:</b> اسمك، والشركة، والبريد الإلكتروني، ورقم الهاتف، والخدمة التي تستفسر عنها، وأي تفاصيل تدرجها في الاستفسار أو طلب عرض السعر."),
              ("<b>Technical information:</b> browser type, device type, approximate location, referring page and pages viewed, collected through server logs and cookies.",
               "<b>المعلومات التقنية:</b> نوع المتصفح، ونوع الجهاز، والموقع التقريبي، والصفحة المُحيلة والصفحات التي تمت زيارتها، وتُجمع عبر سجلات الخادم وملفات تعريف الارتباط."),
              ("<b>Service information:</b> where you become a client, records relating to site surveys, deployments, shift rosters, patrol visits and incident reports.",
               "<b>معلومات الخدمة:</b> عندما تصبح عميلاً، السجلات المتعلقة بمعاينات المواقع وخطط الانتشار وجداول الورديات وزيارات الدوريات وتقارير الحوادث.")])]),
    (("How We Use Your Information", "كيف نستخدم معلوماتك"),
     [("ul", [("To respond to your enquiry and prepare quotations or proposals.", "للردّ على استفسارك وإعداد عروض الأسعار أو المقترحات."),
              ("To arrange and carry out site surveys, deployments, patrols and supervision.", "لترتيب وتنفيذ معاينات المواقع وخطط الانتشار والدوريات والإشراف."),
              ("To provide customer support and manage our contractual relationship with you.", "لتقديم دعم العملاء وإدارة علاقتنا التعاقدية معك."),
              ("To improve this website, our services and our communications.", "لتحسين هذا الموقع وخدماتنا وتواصلنا."),
              ("To comply with legal, regulatory and licensing obligations in the State of Kuwait.", "للامتثال للالتزامات القانونية والتنظيمية والترخيصية في دولة الكويت.")])]),
    (("Cookies", "ملفات تعريف الارتباط"),
     [("p", ("This website uses cookies and similar technologies to keep the site working correctly and to understand how visitors use it. You can control or delete cookies through your browser settings. Disabling cookies may affect parts of the site&rsquo;s functionality.",
             "يستخدم هذا الموقع ملفات تعريف الارتباط وتقنيات مشابهة للحفاظ على عمل الموقع بشكل صحيح ولفهم كيفية استخدام الزوار له. ويمكنك التحكم بها أو حذفها من إعدادات متصفحك. وقد يؤثر تعطيلها على بعض وظائف الموقع."))]),
    (("Sharing Your Information", "مشاركة معلوماتك"),
     [("p", ("We do not sell your personal information. We may share it with:", "نحن لا نبيع معلوماتك الشخصية. وقد نشاركها مع:")),
      ("ul", [("Service providers who support our operations, such as hosting and IT providers, under confidentiality obligations.",
               "مزوّدي الخدمات الذين يدعمون عملياتنا، مثل مزوّدي الاستضافة وتقنية المعلومات، بموجب التزامات السرية."),
              ("Technology partners and manufacturers where necessary to fulfil warranty or support obligations on products supplied for a project.",
               "شركاء التقنية والمصنّعين عند الضرورة للوفاء بالتزامات الضمان أو الدعم للمنتجات المورَّدة لمشروع ما."),
              ("Competent authorities where disclosure is required by law or to protect life and property.",
               "الجهات المختصة عندما يكون الإفصاح مطلوباً بموجب القانون أو لحماية الأرواح والممتلكات.")])]),
    (("Data Security", "أمن البيانات"),
     [("p", ("We apply appropriate technical and organisational measures to protect personal information against unauthorised access, loss or misuse. No method of transmission or storage is completely secure, but we work to protect your information and to review our safeguards regularly.",
             "نطبّق تدابير تقنية وتنظيمية مناسبة لحماية المعلومات الشخصية من الوصول غير المصرّح به أو الفقدان أو سوء الاستخدام. ولا توجد وسيلة نقل أو تخزين آمنة تماماً، لكننا نعمل على حماية معلوماتك ومراجعة إجراءاتنا الوقائية بانتظام."))]),
    (("Data Retention", "الاحتفاظ بالبيانات"),
     [("p", ("We keep personal information only for as long as necessary for the purposes described in this policy, or for as long as required by applicable law, contract or licensing requirements.",
             "نحتفظ بالمعلومات الشخصية للمدة اللازمة للأغراض الموضّحة في هذه السياسة فقط، أو للمدة التي يقتضيها القانون المعمول به أو العقد أو متطلبات الترخيص."))]),
    (("Your Rights", "حقوقك"),
     [("p", ("You may request access to the personal information we hold about you, ask us to correct inaccurate information, or ask us to delete information where we are not required to retain it. To make a request, contact us using the details below.",
             "يمكنك طلب الاطّلاع على المعلومات الشخصية التي نحتفظ بها عنك، أو مطالبتنا بتصحيح المعلومات غير الدقيقة، أو حذف المعلومات التي لا يُلزمنا القانون بالاحتفاظ بها. ولتقديم طلب، تواصل معنا عبر البيانات أدناه."))]),
    (("Client Premises and Monitoring", "منشآت العملاء والمراقبة"),
     [("p", ("Where AZSCO officers work at a client&rsquo;s premises, any CCTV or entry system at that site remains the client&rsquo;s own, and the client is responsible for how it is used. AZSCO processes such data only as instructed by the client and as permitted by applicable law.",
             "عندما يعمل أفراد أزسكو في منشأة أحد العملاء، تبقى أي كاميرات مراقبة أو أنظمة دخول في ذلك الموقع ملكاً للعميل، ويتحمّل العميل مسؤولية كيفية استخدامها. ولا تعالج أزسكو هذه البيانات إلا وفق تعليمات العميل وبما يسمح به القانون المعمول به."))]),
    (("Third-Party Links", "روابط الجهات الخارجية"),
     [("p", ("This website may link to third-party sites. We are not responsible for the privacy practices or content of those sites, and we encourage you to read their privacy policies.",
             "قد يتضمّن هذا الموقع روابط لمواقع تابعة لجهات خارجية. ولسنا مسؤولين عن ممارسات الخصوصية أو المحتوى في تلك المواقع، وننصحك بقراءة سياسات الخصوصية الخاصة بها."))]),
    (("Changes to This Policy", "التعديلات على هذه السياسة"),
     [("p", ("We may update this policy from time to time. The revised version will be posted on this page with an updated date.",
             "قد نحدّث هذه السياسة من وقت لآخر. وستُنشر النسخة المعدّلة على هذه الصفحة مع تاريخ التحديث."))]),
  ],
  "contact_h": ("Contact Us", "اتصل بنا"),
  "contact_p": ("If you have questions about this Privacy Policy or how we handle your information, please contact us:",
                "إذا كانت لديك أسئلة حول سياسة الخصوصية هذه أو كيفية تعاملنا مع معلوماتك، يُرجى التواصل معنا:"),
  "tel_label": ("Telephone:", "الهاتف:"),
  "email_label": ("Email:", "البريد الإلكتروني:"),
}

# ============================================================ templates
FONTS_EN = ('<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700'
            '&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">')
FONTS_AR = ('<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700'
            '&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">')

def ltr(text):
    """Keep phone numbers and emails readable inside right-to-left text."""
    return f'<span dir="ltr">{text}</span>'

def head(lang, fname, title, desc):
    a = asset(lang, "")
    return f'''<!DOCTYPE html>
<html {lang_attrs(lang)}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d0d0d">
<link rel="canonical" href="{canonical(lang, fname)}">
<link rel="alternate" hreflang="en" href="{canonical("en", fname)}">
<link rel="alternate" hreflang="ar" href="{canonical("ar", fname)}">
<link rel="alternate" hreflang="x-default" href="{canonical("en", fname)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{t(SITE_NAME, lang)}">
<meta property="og:locale" content="{"ar_KW" if lang == "ar" else "en_US"}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical(lang, fname)}">
<meta property="og:image" content="https://www.azsco.com/assets/img/AZSCO_Logo.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{a}assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{a}assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="{a}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS_AR if lang == "ar" else FONTS_EN}
<link rel="stylesheet" href="{a}assets/css/style.css">
</head>
<body>
<a class="skip-link" href="#main">{t(UI["skip"], lang)}</a>
'''

def desktop_nav(lang):
    out = ['<ul class="nav">']
    for label, href, subs in NAV:
        if subs:
            out.append(f'<li><a href="{href}">{t(label, lang)} {I["caret"]}</a><ul class="subnav">')
            for s_label, s_href in subs:
                out.append(f'<li><a href="{s_href}">{t(s_label, lang)}</a></li>')
            out.append('</ul></li>')
        else:
            out.append(f'<li><a href="{href}">{t(label, lang)}</a></li>')
    out.append('</ul>')
    return "\n        ".join(out)

def mobile_nav(lang):
    out = ['<ul class="m-nav">']
    for n, (label, href, subs) in enumerate(NAV):
        if subs:
            out.append('<li class="m-group">')
            out.append(f'<button class="m-toggle" type="button" aria-expanded="false" '
                       f'aria-controls="m-sub-{n}">{t(label, lang)}{I["caret"]}</button>')
            out.append(f'<ul class="m-sub" id="m-sub-{n}">')
            for s_label, s_href in subs:
                out.append(f'<li><a href="{s_href}">{t(s_label, lang)}</a></li>')
            out.append('</ul></li>')
        else:
            out.append(f'<li><a href="{href}">{t(label, lang)}</a></li>')
    out.append('</ul>')
    return "\n      ".join(out)

def lang_link(lang, fname, cls="lang-switch"):
    other = "ar" if lang == "en" else "en"
    return (f'<a class="{cls}" href="{other_lang_url(lang, fname)}" lang="{other}" '
            f'dir="{"rtl" if other == "ar" else "ltr"}" '
            f'hreflang="{other}" aria-label="{t(UI["LANG_SWITCH_LABEL"], lang) if "LANG_SWITCH_LABEL" in UI else t(LANG_SWITCH_LABEL, lang)}">'
            f'{I["globe"]}<span class="lang-full">{t(LANG_SWITCH, lang)}</span>'
            f'<span class="lang-short">{t(LANG_SWITCH_SHORT, lang)}</span></a>')

def header(lang, fname):
    a = asset(lang, "")
    return f'''
<div class="topbar">
  <div class="wrap">
    <ul class="topbar-list">
      <li class="hide-sm">{I["pin"]}<a href="{MAPS_URL}" target="_blank" rel="noopener noreferrer" aria-label="{t(UI["map_label"], lang)}">{t(ADDRESS_1L, lang)}</a></li>
      <li>{I["phone"]}<a href="tel:{PHONE_HREF}" dir="ltr">{PHONE}</a></li>
      <li class="hide-md">{I["mail"]}<a href="mailto:{EMAIL}" dir="ltr">{EMAIL}</a></li>
      <li class="hide-md">{I["clock"]}<span>{t(RESPONSE_24, lang)}</span></li>
    </ul>
    <div class="topbar-end">
      <div class="topbar-social" aria-label="{t(UI["social"], lang)}">
        <a href="#" aria-label="AZSCO on Facebook">{I["facebook"]}</a>
        <a href="#" aria-label="AZSCO on X">{I["x"]}</a>
        <a href="#" aria-label="AZSCO on Instagram">{I["instagram"]}</a>
        <a href="#" aria-label="AZSCO on LinkedIn">{I["linkedin"]}</a>
      </div>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{t(UI["home_label"], lang)}">
      <img class="brand-logo" src="{a}assets/img/AZSCO_Logo.png" alt="{t(SITE_NAME, lang)}" width="1730" height="798">
    </a>

    <nav aria-label="{t(UI["main_nav"], lang)}">
        {desktop_nav(lang)}
    </nav>

    <div class="header-cta">
      {lang_link(lang, fname, "lang-switch lang-switch--head")}
      <a class="btn btn-primary" href="contact.html">{t(UI["quote"], lang)}</a>
      <button class="burger" type="button" aria-label="{t(UI["menu_open"], lang)}" aria-expanded="false" aria-controls="mobile-nav"><span></span></button>
    </div>
  </div>
</header>

<div class="backdrop"></div>
<nav class="mobile-nav" id="mobile-nav" aria-label="{t(UI["mob_nav"], lang)}">
  <div class="mobile-nav-head">
    <img class="brand-logo" src="{a}assets/img/AZSCO_Logo.png" alt="{t(SITE_NAME, lang)}" width="1730" height="798">
    <button class="close" type="button" aria-label="{t(UI["menu_close"], lang)}">{I["close"]}</button>
  </div>
      {mobile_nav(lang)}
  <div class="mobile-nav-foot">
    <a class="btn btn-primary" href="contact.html">{t(UI["consult"], lang)}</a>
    <a class="m-contact" href="tel:{PHONE_HREF}">{I["phone"]}<span dir="ltr">{PHONE}</span></a>
    <a class="m-contact" href="mailto:{EMAIL}">{I["mail"]}<span dir="ltr">{EMAIL}</span></a>
  </div>
</nav>
'''

def chat_widget(lang):
    C = CHAT
    chips = "\n      ".join(
        f'<button type="button">{t(sug, lang)}</button>' for sug in C["suggest"])
    return f'''
<div data-azsco-chat data-endpoint="{CHAT_ENDPOINT}" data-lang="{lang}"
     data-greeting="{t(C["greeting"], lang)}"
     data-error="{t(C["error"], lang)}"
     data-offline="{t(C["offline"], lang)}"
     data-label-expand="{t(C["expand"], lang)}"
     data-label-collapse="{t(C["collapse"], lang)}">
  <button class="chat-launcher" type="button" aria-expanded="false" aria-controls="azsco-chat-panel" aria-label="{t(C["open"], lang)}">
    {I["chat"]}<span class="chat-launcher-text">{t(C["launcher"], lang)}</span>
  </button>

  <div class="chat-panel" id="azsco-chat-panel" role="dialog" aria-label="{t(C["title"], lang)}" hidden>
    <div class="chat-head">
      <span class="avatar">{I["chat"]}</span>
      <span>
        <b>{t(C["title"], lang)}</b>
        <small>{t(C["sub"], lang)}</small>
      </span>
      <span class="spacer"></span>
      <button class="chat-btn" type="button" data-chat-expand aria-pressed="false" aria-label="{t(C["expand"], lang)}">{I["expand"]}</button>
      <button class="chat-btn" type="button" data-chat-close aria-label="{t(C["close"], lang)}">{I["close"]}</button>
    </div>

    <div class="chat-log" role="log" aria-live="polite" aria-atomic="false"></div>

    <div class="chat-suggest">
      {chips}
    </div>

    <form class="chat-form">
      <label class="visually-hidden" for="azsco-chat-input">{t(C["placeholder"], lang)}</label>
      <textarea id="azsco-chat-input" rows="1" placeholder="{t(C["placeholder"], lang)}" maxlength="1000"></textarea>
      <button class="chat-send" type="submit" aria-label="{t(C["send"], lang)}">{I["send"]}</button>
    </form>
    <p class="chat-foot">{t(C["foot"], lang)}</p>
  </div>
</div>
'''

def footer(lang):
    a = asset(lang, "")
    links = "\n          ".join(
        f'<li><a href="{href}">{t(label, lang)}</a></li>' for label, href in FOOTER["links"])
    svc = "\n          ".join(
        f'<li><a href="services.html#{s["anchor"]}">{t(s["name"], lang)}</a></li>' for s in SERVICES)
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html" aria-label="{t(UI["home_label"], lang)}">
          <img class="brand-logo" src="{a}assets/img/AZSCO_Logo_white.png" alt="{t(SITE_NAME, lang)}" width="1730" height="798">
        </a>
        <p>{t(FOOTER["blurb"], lang)}</p>
        <div class="footer-social">
          <a href="#" aria-label="AZSCO on Facebook">{I["facebook"]}</a>
          <a href="#" aria-label="AZSCO on X">{I["x"]}</a>
          <a href="#" aria-label="AZSCO on Instagram">{I["instagram"]}</a>
          <a href="#" aria-label="AZSCO on LinkedIn">{I["linkedin"]}</a>
        </div>
      </div>

      <div>
        <h4>{t(FOOTER["company"], lang)}</h4>
        <ul class="footer-links">
          {links}
        </ul>
      </div>

      <div>
        <h4>{t(FOOTER["services"], lang)}</h4>
        <ul class="footer-links">
          {svc}
        </ul>
      </div>

      <div>
        <h4>{t(FOOTER["touch"], lang)}</h4>
        <ul class="footer-contact">
          <li>{I["pin"]}<span>{t(ADDRESS_BR, lang)}</span></li>
          <li>{I["phone"]}<a href="tel:{PHONE_HREF}" dir="ltr">{PHONE}</a></li>
          <li>{I["mail"]}<span><a href="mailto:{EMAIL}" dir="ltr">{EMAIL}</a><small>{t(FOOTER["email_general"], lang)}</small></span></li>
          <li>{I["mail"]}<span><a href="mailto:{EMAIL_SALES}" dir="ltr">{EMAIL_SALES}</a><small>{t(FOOTER["email_sales"], lang)}</small></span></li>
          <li>{I["clock"]}<span>{t(HOURS_FOOT, lang)}</span></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; <span data-year>2026</span> {t(COMPANY, lang)}. {t(FOOTER["rights"], lang)}</p>
      <ul>
        <li><a href="privacy-policy.html">{t(FOOTER["privacy"], lang)}</a></li>
        <li><a href="contact.html">{t(FOOTER["contact"], lang)}</a></li>
      </ul>
    </div>
  </div>
</footer>

<button class="to-top" type="button" aria-label="{t(UI["to_top"], lang)}">{I["up"]}</button>

<div class="mobile-bar">
  <a class="mobile-bar-call" href="tel:{PHONE_HREF}">{I["phone"]}<span>{t(UI["call_now"], lang)}</span></a>
  <a class="mobile-bar-quote" href="contact.html">{I["mail"]}<span>{t(UI["get_quote"], lang)}</span></a>
</div>
{chat_widget(lang)}
<script src="{a}assets/js/main.js"></script>
<script src="{a}assets/js/chat-config.js"></script>
<script src="{a}assets/js/chat.js" defer></script>
</body>
</html>
'''

def banner(lang, title, sub, crumb):
    return f'''
<section class="page-banner">
  <div class="wrap">
    <p class="eyebrow">{t(SITE_NAME, lang)}</p>
    <h1>{title}</h1>
    <p>{sub}</p>
    <ul class="crumbs">
      <li><a href="index.html">{t(UI["home"], lang)}</a></li>
      <li aria-current="page">{crumb}</li>
    </ul>
  </div>
</section>
'''

def cta(lang, pair=None):
    title, text = pair or CTA_DEFAULT
    return f'''
<section class="cta">
  <div class="wrap">
    <div>
      <h2>{t(title, lang)}</h2>
      <p>{t(text, lang)}</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-primary" href="contact.html">{t(UI["consult"], lang)} {I["arrow"]}</a>
      <a class="btn btn-outline" href="tel:{PHONE_HREF}" dir="ltr">{PHONE}</a>
    </div>
  </div>
</section>
'''

def stats_block(lang):
    cells = []
    for i, (kind, label) in enumerate(STATS):
        if kind == "founded":
            num = f'<span data-count="{FOUNDED}" data-plain>0</span>'
        elif kind == "years":
            num = f'<span data-years-since="{FOUNDED}" data-count="{YEARS}">0</span>+'
        elif kind == "247":
            num = '<span data-count="24">0</span>/<span data-count="7">0</span>'
        else:
            num = f'<span data-count="{len(PARTNERS)}">0</span>'
        cells.append(f'      <div class="stat reveal" data-delay="{i*80}">'
                     f'<span class="num" dir="ltr">{num}</span>'
                     f'<span class="label">{t(label, lang)}</span></div>')
    return ('<section class="section section--tight stats">\n  <div class="wrap">\n'
            '    <div class="grid grid-4">\n' + "\n".join(cells) +
            '\n    </div>\n  </div>\n</section>')

PAGES = {}

def page(lang, fname, title, desc, body):
    PAGES[(lang, fname)] = (head(lang, fname, title, desc) + header(lang, fname)
                            + f'<main id="main">\n{body}\n</main>' + footer(lang))

# ============================================================ shared blocks
def service_cards(lang):
    return "\n".join(
        f'''      <article class="card reveal" data-delay="{n*80}">
        <span class="ico">{I[s["icon"]]}</span>
        <h3>{t(s["name"], lang)}</h3>
        <p>{t(s["card"], lang)}</p>
        <a class="more" href="services.html#{s["anchor"]}">{t(UI["learn"], lang)} {I["arrow"]}</a>
      </article>''' for n, s in enumerate(SERVICES))

def partner_grid():
    return "\n".join(
        f'      <div class="partner reveal" data-delay="{i*80}">'
        f'<span class="partner-name">{name}</span></div>'
        for i, name in enumerate(PARTNERS))

def client_grid(lang):
    return "\n".join(
        f'      <div class="client reveal" data-delay="{i*80}">'
        f'<span class="client-name">{t(name, lang)}</span></div>'
        for i, name in enumerate(CLIENTS))

def sector_grid(lang):
    return "\n".join(
        f'      <div class="sector reveal" data-delay="{i*60}">'
        f'<span class="ico">{I[icon]}</span><span>{t(label, lang)}</span></div>'
        for i, (icon, label) in enumerate(SECTORS))

def tiles(lang, items, cols=3):
    return "\n".join(
        f'      <div class="tile reveal" data-delay="{(i%cols)*80}"><span class="ico">'
        f'{I["award"] if icon == "award2" else I[icon]}</span><div><h4>{t(title, lang)}</h4>'
        f'<p>{t(text, lang).replace("{YEARS}", str(YEARS))}</p></div></div>'
        for i, (icon, title, text) in enumerate(items))

# ============================================================ pages
def build_home(lang):
    H = HOME
    cards = "\n".join(
        f'          <li><span class="ico">{I[icon]}</span><span><b>{t(title, lang)}</b>'
        f'<span>{t(desc, lang)}</span></span></li>' for icon, title, desc in H["card_items"])
    points = "\n".join(f'          <li>{I["check"]} {t(p, lang)}</li>' for p in H["points"])
    checks = "\n".join(
        f'          <li><span class="ico">{I["check"]}</span><span><b>{t(a, lang)}</b>'
        f'<span>{t(b, lang)}</span></span></li>' for a, b in H["about_checks"])
    steps = "\n".join(
        f'      <div class="step reveal" data-delay="{i*80}"><span class="n">{i+1:02d}</span>'
        f'<h4>{t(a, lang)}</h4><p>{t(b, lang)}</p></div>'
        for i, (a, b) in enumerate(H["steps"]))

    body = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="hero-badge">{I["shield-check"]} {t(H["badge"], lang)}</span>
        <h1>{t(H["h1a"], lang)}<em>{t(H["h1b"], lang)}</em></h1>
        <p class="lead">{t(H["lead"], lang)}</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="contact.html">{t(UI["consult"], lang)} {I["arrow"]}</a>
          <a class="btn btn-outline" href="services.html">{t(UI["explore"], lang)}</a>
        </div>
        <ul class="hero-points">
{points}
        </ul>
      </div>

      <aside class="hero-card reveal" data-delay="120">
        <h3>{t(H["card_h"], lang)}</h3>
        <p>{t(H["card_p"], lang)}</p>
        <ul class="hero-card-list">
{cards}
        </ul>
      </aside>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(H["svc_eyebrow"], lang)}</p>
      <h2>{t(H["svc_h2"], lang)}</h2>
      <p>{t(H["svc_lead"], lang)}</p>
    </div>
    <div class="grid grid-3">
{service_cards(lang)}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split">
      <div class="split-visual reveal">
        <div class="visual-frame">{HERO_SVG}</div>
        <div class="visual-badge"><b dir="ltr">24/7</b><span>{t(("Always On Duty", "على أهبة الاستعداد"), lang)}</span></div>
      </div>
      <div class="reveal" data-delay="120">
        <p class="eyebrow">{t(H["about_eyebrow"], lang)}</p>
        <h2>{t(H["about_h2"], lang)}</h2>
        <p class="lead">{t(H["about_lead"], lang)}</p>
        <ul class="check-list">
{checks}
        </ul>
        <div class="btn-row">
          <a class="btn btn-dark" href="about.html">{t(UI["more_about"], lang)} {I["arrow"]}</a>
        </div>
      </div>
    </div>
  </div>
</section>

{stats_block(lang)}

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(H["sec_eyebrow"], lang)}</p>
      <h2>{t(H["sec_h2"], lang)}</h2>
      <p>{t(H["sec_lead"], lang)}</p>
    </div>
    <div class="sectors">
{sector_grid(lang)}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(H["why_eyebrow"], lang)}</p>
      <h2>{t(H["why_h2"], lang)}</h2>
      <p>{t(H["why_lead"], lang)}</p>
    </div>
    <div class="grid grid-3">
{tiles(lang, H["why_tiles"])}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(H["proc_eyebrow"], lang)}</p>
      <h2>{t(H["proc_h2"], lang)}</h2>
      <p>{t(H["proc_lead"], lang)}</p>
    </div>
    <div class="steps">
{steps}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(H["part_eyebrow"], lang)}</p>
      <h2>{t(H["part_h2"], lang)}</h2>
      <p>{t(H["part_lead"], lang)}</p>
    </div>
    <div class="partners">
{partner_grid()}
    </div>
    <div class="center" style="margin-top:44px">
      <a class="btn btn-dark" href="partners.html">{t(H["part_btn"], lang)} {I["arrow"]}</a>
    </div>
  </div>
</section>

{cta(lang)}
'''
    page(lang, "index.html", t(H["title"], lang), t(H["desc"], lang), body)

def build_about(lang):
    A = ABOUT
    story = "\n        ".join(
        ('<p class="lead">' if i == 0 else '<p>') + t(p, lang) + '</p>'
        for i, p in enumerate(A["story"]))
    mvv = "\n".join(
        f'      <article class="card reveal" data-delay="{i*80}"><span class="ico">{I[icon]}</span>'
        f'<h3>{t(title, lang)}</h3><p>{t(text, lang)}</p></article>'
        for i, (icon, title, text) in enumerate(A["mvv"]))
    ceo = "\n      ".join(f'<p>{t(p, lang)}</p>' for p in A["ceo"])
    faqs = []
    for i, (q, a) in enumerate(A["faq"]):
        ans = t(a, lang).replace("{ADDR}", t(ADDRESS_1L, lang)).replace("{PHONE}", PHONE)
        faqs.append(f'''      <div class="acc{" is-open" if i == 0 else ""} reveal">
        <button class="acc-btn" type="button">{t(q, lang)}<span class="pm">{I["plus"]}</span></button>
        <div class="acc-panel"><div class="inner">{ans}</div></div>
      </div>''')

    FAQ_HTML = "\n".join(faqs)
    body = banner(lang, t(A["banner_h"], lang), t(A["banner_p"], lang), t(A["crumb"], lang)) + f'''
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split-visual reveal">
        <div class="visual-frame">{ABOUT_SVG}</div>
        <div class="visual-badge"><b dir="ltr">{t(A["badge"][0], lang)}</b><span>{t(A["badge"][1], lang)}</span></div>
      </div>
      <div class="reveal" data-delay="120">
        <p class="eyebrow">{t(A["story_eyebrow"], lang)}</p>
        <h2>{t(A["story_h2"], lang)}</h2>
        {story}
        <div class="btn-row" style="margin-top:26px">
          <a class="btn btn-dark" href="contact.html">{t(UI["talk"], lang)} {I["arrow"]}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="grid grid-3">
{mvv}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(A["commit_eyebrow"], lang)}</p>
      <h2>{t(A["commit_h2"], lang)}</h2>
      <p>{t(A["commit_lead"], lang)}</p>
    </div>
    <div class="grid grid-2">
{tiles(lang, A["commit_tiles"], cols=2)}
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(A["ceo_eyebrow"], lang)}</p>
      <h2>{t(A["ceo_h2"], lang)}</h2>
    </div>
    <blockquote class="quote reveal">
      {ceo}
      <p class="quote-line">{t(A["ceo_line"], lang)}</p>
      <p>{t(A["ceo_thanks"], lang)}</p>
      <footer class="quote-by">{t(A["ceo_by"], lang)}</footer>
    </blockquote>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(A["clients_eyebrow"], lang)}</p>
      <h2>{t(A["clients_h2"], lang)}</h2>
      <p>{t(A["clients_lead"], lang)}</p>
    </div>
    <div class="clients">
{client_grid(lang)}
    </div>
  </div>
</section>

{stats_block(lang)}

<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(A["faq_eyebrow"], lang)}</p>
      <h2>{t(A["faq_h2"], lang)}</h2>
    </div>
    <div style="max-width:840px;margin:0 auto">
{FAQ_HTML}
    </div>
  </div>
</section>

{cta(lang)}
'''
    page(lang, "about.html", t(A["title"], lang), t(A["desc"], lang), body)

def build_services(lang):
    S = SERVICES_PAGE
    sections = []
    for i, s in enumerate(SERVICES):
        alt = " section--alt" if i % 2 else ""
        flip = " split--flip" if i % 2 else ""
        pts = "\n".join(
            f'          <li><span class="ico">{I["check"]}</span><span>{t(p, lang)}</span></li>'
            for p in s["points"])
        sections.append(f'''
<section class="section{alt}" id="{s["anchor"]}">
  <div class="wrap">
    <div class="split{flip}">
      <div class="reveal">
        <p class="eyebrow">{t(S["service_label"], lang)} {i+1:02d}</p>
        <h2>{t(s["name"], lang)}</h2>
        <p class="lead">{t(s["intro"], lang)}</p>
        <ul class="check-list">
{pts}
        </ul>
        <div class="btn-row">
          <a class="btn btn-dark" href="contact.html">{t(UI["req_quote"], lang)} {I["arrow"]}</a>
        </div>
      </div>
      <div class="split-visual reveal" data-delay="120">
        <div class="visual-frame"><div style="color:#fff;width:160px;max-width:60%">{I[s["icon"]]}</div></div>
      </div>
    </div>
  </div>
</section>''')

    body = banner(lang, t(S["banner_h"], lang), t(S["banner_p"], lang), t(S["crumb"], lang)) + f'''
<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(S["over_eyebrow"], lang)}</p>
      <h2>{t(S["over_h2"], lang)}</h2>
      <p>{t(S["over_lead"], lang)}</p>
    </div>
    <div class="grid grid-3">
{service_cards(lang)}
    </div>
  </div>
</section>
{"".join(sections)}

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(S["people_eyebrow"], lang)}</p>
      <h2>{t(S["people_h2"], lang)}</h2>
      <p>{t(S["people_lead"], lang)}</p>
    </div>
    <div class="grid grid-3">
{tiles(lang, S["people_tiles"])}
    </div>
  </div>
</section>

{cta(lang, S["cta"])}
'''
    page(lang, "services.html", t(S["title"], lang), t(S["desc"], lang), body)

def build_partners(lang):
    P = PARTNERS_PAGE
    join_p = (t(P["join_p"], lang)
              .replace("{EMAIL}", f'<a href="mailto:{EMAIL}" dir="ltr">{EMAIL}</a>')
              .replace("{PHONE}", f'<span dir="ltr">{PHONE}</span>'))
    body = banner(lang, t(P["banner_h"], lang), t(P["banner_p"], lang), t(P["crumb"], lang)) + f'''
<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(P["eyebrow"], lang)}</p>
      <h2>{t(P["h2"], lang)}</h2>
      <p>{t(P["lead"], lang)}</p>
    </div>
    <div class="partners">
{partner_grid()}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{t(P["why_eyebrow"], lang)}</p>
      <h2>{t(P["why_h2"], lang)}</h2>
    </div>
    <div class="grid grid-3">
{tiles(lang, P["tiles"])}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">{t(P["join_eyebrow"], lang)}</p>
        <h2>{t(P["join_h2"], lang)}</h2>
        <p class="lead">{t(P["join_lead"], lang)}</p>
        <p>{join_p}</p>
        <div class="btn-row">
          <a class="btn btn-dark" href="contact.html">{t(P["join_btn"], lang)} {I["arrow"]}</a>
        </div>
      </div>
      <div class="split-visual reveal" data-delay="120">
        <div class="visual-frame"><div style="color:#fff;width:160px;max-width:55%">{I["link"]}</div></div>
      </div>
    </div>
  </div>
</section>

{cta(lang)}
'''
    page(lang, "partners.html", t(P["title"], lang), t(P["desc"], lang), body)

def build_contact(lang):
    C = CONTACT
    F = C["fields"]
    card_values = [
        f'<p>{t(ADDRESS_BR, lang)}</p>',
        f'<a href="tel:{PHONE_HREF}" dir="ltr">{PHONE}</a>',
        (f'<a href="mailto:{EMAIL}" dir="ltr">{EMAIL}</a>'
         f'<small class="info-note">{t(FOOTER["email_general"], lang)}</small>'
         f'<a href="mailto:{EMAIL_SALES}" dir="ltr">{EMAIL_SALES}</a>'
         f'<small class="info-note">{t(FOOTER["email_sales"], lang)}</small>'),
    ]
    cards = []
    for i, ((icon, title, sub), value) in enumerate(zip(C["cards"], card_values)):
        extra = (f'<p style="color:var(--muted);font-size:.86rem">{t(sub, lang)}</p>') if sub else ""
        cards.append(f'''      <div class="info-card reveal" data-delay="{i*80}">
        <span class="ico">{I[icon]}</span>
        <div><h4>{t(title, lang)}</h4>{value}{extra}</div>
      </div>''')
    options = "\n".join(f'              <option>{t(o, lang)}</option>' for o in C["options"])
    note = (t(F["note"], lang)
            .replace("{PRIVACY}", f'<a href="privacy-policy.html">{t(FOOTER["privacy"], lang)}</a>')
            .replace("{PHONE}", f'<span dir="ltr">{PHONE}</span>'))

    body = banner(lang, t(C["banner_h"], lang), t(C["banner_p"], lang), t(C["crumb"], lang)) + f'''
<section class="section">
  <div class="wrap">
    <div class="grid grid-3" style="margin-bottom:64px">
{chr(10).join(cards)}
    </div>

    <div class="contact-grid">
      <div class="reveal">
        <p class="eyebrow">{t(C["form_eyebrow"], lang)}</p>
        <h2>{t(C["form_h2"], lang)}</h2>
        <p>{t(C["form_lead"], lang)}</p>

        <div class="map-embed" style="margin-top:32px">
          <a class="pin" href="{MAPS_URL}" target="_blank" rel="noopener noreferrer" aria-label="{t(UI["map_label"], lang)}">
            {I["pin"]}
            <h4>{t(COMPANY, lang)}</h4>
            <p>{t(ADDRESS_1L, lang)}</p>
          </a>
        </div>

        <ul class="check-list" style="margin-top:32px">
          <li><span class="ico">{I["check"]}</span><span><b>{t(C["office_hours"], lang)}</b><span>{t(HOURS, lang)}</span></span></li>
          <li><span class="ico">{I["check"]}</span><span><b>{t(C["emergency"], lang)}</b><span>{t(C["emergency_v"], lang)}</span></span></li>
        </ul>
      </div>

      <div class="form-card reveal" data-delay="120">
        <form data-contact-form novalidate data-sent-message="{t(C["sent"], lang)}">
          <div class="form-status" role="status" aria-live="polite"></div>

          <div class="grid grid-2" style="gap:0 20px">
            <div class="field">
              <label for="name">{t(F["name"], lang)} <span class="req">*</span></label>
              <input type="text" id="name" name="name" placeholder="{t(F["name_ph"], lang)}" required>
              <span class="err">{t(F["req"], lang)}</span>
            </div>
            <div class="field">
              <label for="company">{t(F["company"], lang)}</label>
              <input type="text" id="company" name="company" placeholder="{t(F["company_ph"], lang)}">
              <span class="err"></span>
            </div>
            <div class="field">
              <label for="email">{t(F["email"], lang)} <span class="req">*</span></label>
              <input type="email" id="email" name="email" placeholder="you@example.com" dir="ltr" required>
              <span class="err">{t(F["bad_email"], lang)}</span>
            </div>
            <div class="field">
              <label for="phone">{t(F["phone"], lang)} <span class="req">*</span></label>
              <input type="tel" id="phone" name="phone" placeholder="+965 0000 0000" dir="ltr" required>
              <span class="err">{t(F["bad_phone"], lang)}</span>
            </div>
          </div>

          <div class="field">
            <label for="service">{t(F["service"], lang)} <span class="req">*</span></label>
            <select id="service" name="service" required>
              <option value="">{t(F["select"], lang)}</option>
{options}
            </select>
            <span class="err">{t(F["choose"], lang)}</span>
          </div>

          <div class="field">
            <label for="message">{t(F["message"], lang)} <span class="req">*</span></label>
            <textarea id="message" name="message" placeholder="{t(F["message_ph"], lang)}" required></textarea>
            <span class="err">{t(F["req"], lang)}</span>
          </div>

          <button class="btn btn-primary" type="submit" style="width:100%">{t(F["submit"], lang)} {I["arrow"]}</button>
          <p class="form-note">{note}</p>
        </form>
      </div>
    </div>
  </div>
</section>

{cta(lang, C["cta"])}
'''
    page(lang, "contact.html", t(C["title"], lang), t(C["desc"], lang), body)

def build_privacy(lang):
    P = PRIVACY
    out = [f'<span class="updated">{t(P["updated"], lang)}</span>',
           f'<p class="lead">{t(P["intro"], lang).replace("{COMPANY}", t(COMPANY, lang))}</p>']
    for heading, blocks in P["sections"]:
        out.append(f'<h2>{t(heading, lang)}</h2>')
        for kind, payload in blocks:
            if kind == "p":
                out.append(f'<p>{t(payload, lang)}</p>')
            else:
                items = "\n        ".join(f'<li>{t(i, lang)}</li>' for i in payload)
                out.append(f'<ul>\n        {items}\n      </ul>')
    out.append(f'<h2>{t(P["contact_h"], lang)}</h2>')
    out.append(f'<p>{t(P["contact_p"], lang)}</p>')
    out.append('<ul>\n        '
               f'<li><b>{t(COMPANY, lang)}</b></li>\n        '
               f'<li>{t(ADDRESS_1L, lang)}</li>\n        '
               f'<li>{t(P["tel_label"], lang)} <a href="tel:{PHONE_HREF}" dir="ltr">{PHONE}</a></li>\n        '
               f'<li>{t(P["email_label"], lang)} <a href="mailto:{EMAIL}" dir="ltr">{EMAIL}</a></li>\n      </ul>')
    rich = "\n      ".join(out)

    body = banner(lang, t(P["banner_h"], lang), t(P["banner_p"], lang), t(P["crumb"], lang)) + f'''
<section class="section">
  <div class="wrap">
    <div class="rich reveal">
      {rich}
    </div>
  </div>
</section>
'''
    page(lang, "privacy-policy.html", t(P["title"], lang), t(P["desc"], lang), body)

def build_404(lang):
    N = NOTFOUND
    body = f'''
<section class="section" style="padding:120px 0">
  <div class="wrap center">
    <p class="eyebrow" style="justify-content:center">{t(N["eyebrow"], lang)}</p>
    <h1 style="margin-bottom:18px">{t(N["h1"], lang)}</h1>
    <p class="lead" style="max-width:560px;margin:0 auto 32px">{t(N["lead"], lang)}</p>
    <div class="btn-row center">
      <a class="btn btn-primary" href="index.html">{t(N["back"], lang)} {I["arrow"]}</a>
      <a class="btn btn-dark" href="contact.html">{t(N["contact"], lang)}</a>
    </div>
  </div>
</section>
'''
    page(lang, "404.html", t(N["title"], lang), t(N["desc"], lang), body)

# ============================================================ write
SITEMAP_PRIORITY = {
    "index.html": "1.0", "services.html": "0.9", "about.html": "0.8",
    "contact.html": "0.8", "partners.html": "0.6", "privacy-policy.html": "0.3",
}

def write_chat_config():
    """Writes assets/js/chat-config.js, read by the widget at runtime.

    In "direct" mode this file contains the Mistral key and is served to every
    visitor. That is a deliberate choice recorded in CHAT_MODE above; switching
    CHAT_MODE to "proxy" removes the key from the site entirely.
    """
    import json
    cfg = {
        "mode": CHAT_MODE,
        "endpoint": CHAT_ENDPOINT,
        "model": CHAT_MODEL,
        "apiUrl": "https://api.mistral.ai/v1/chat/completions",
        "apiKey": CHAT_API_KEY if CHAT_MODE == "direct" else "",
        "system": {lang: chat_system_prompt(lang) for lang in LANGS},
    }
    banner = ("/* Generated by tools/build.py - do not edit by hand.\n"
              "   Edit CHAT_* in tools/build.py and rebuild. */\n")
    body = "window.AZSCO_CHAT_CONFIG = " + json.dumps(cfg, ensure_ascii=False, indent=2) + ";\n"
    path = os.path.join(OUT, "assets", "js", "chat-config.js")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(banner + body)
    return cfg["mode"]

def write_sitemap():
    """Built from the pages that exist, with an alternate for each language."""
    today = datetime.date.today().isoformat()
    rows = []
    for fname, priority in SITEMAP_PRIORITY.items():
        for lang in LANGS:
            alts = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{canonical(l, fname)}"/>'
                for l in LANGS)
            rows.append(f'  <url>\n    <loc>{canonical(lang, fname)}</loc>{alts}\n'
                        f'    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)
    return len(rows)

if __name__ == "__main__":
    for lang in LANGS:
        build_home(lang)
        build_about(lang)
        build_services(lang)
        build_partners(lang)
        build_contact(lang)
        build_privacy(lang)
        build_404(lang)

    os.makedirs(os.path.join(OUT, "ar"), exist_ok=True)
    for (lang, fname), html in PAGES.items():
        path = os.path.join(OUT, "ar", fname) if lang == "ar" else os.path.join(OUT, fname)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        print("wrote", ("ar/" if lang == "ar" else "") + fname, len(html), "bytes")
    print("wrote sitemap.xml with", write_sitemap(), "urls")
    print("wrote assets/js/chat-config.js (mode:", write_chat_config() + ")")
