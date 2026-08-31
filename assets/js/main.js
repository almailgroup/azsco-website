/* AZSCO Security — site behaviour */
(function () {
  'use strict';

  var doc = document;
  var on = function (el, ev, fn) { if (el) el.addEventListener(ev, fn); };
  var all = function (sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); };

  /* ---------- mark the active nav item ---------- */
  function markActive() {
    var here = location.pathname.split('/').pop() || 'index.html';
    all('.nav a, .mobile-nav a').forEach(function (a) {
      var href = (a.getAttribute('href') || '').split('/').pop().split('#')[0];
      if (!href || href !== here) return;
      var item = a.closest('li');
      if (!item) return;
      item.classList.add('is-active');
      var sub = a.closest('.subnav');
      if (sub) sub.closest('li').classList.add('is-active');
    });
  }

  /* ---------- sticky header shadow ---------- */
  function stickyHeader() {
    var header = doc.querySelector('.site-header');
    if (!header) return;
    var toggle = function () { header.classList.toggle('is-stuck', window.scrollY > 10); };
    toggle();
    on(window, 'scroll', toggle, { passive: true });
  }

  /* ---------- mobile drawer ---------- */
  function mobileNav() {
    var burger = doc.querySelector('.burger');
    var drawer = doc.querySelector('.mobile-nav');
    var backdrop = doc.querySelector('.backdrop');
    var closeBtn = doc.querySelector('.mobile-nav .close');
    if (!burger || !drawer || !backdrop) return;

    function setState(open) {
      drawer.classList.toggle('is-open', open);
      backdrop.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      doc.body.style.overflow = open ? 'hidden' : '';
      if (open) { var f = drawer.querySelector('a, button'); if (f) f.focus(); }
    }

    on(burger, 'click', function () { setState(!drawer.classList.contains('is-open')); });
    on(backdrop, 'click', function () { setState(false); });
    on(closeBtn, 'click', function () { setState(false); burger.focus(); });
    all('.mobile-nav a').forEach(function (a) { on(a, 'click', function () { setState(false); }); });
    on(doc, 'keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) { setState(false); burger.focus(); }
    });
    on(window, 'resize', function () {
      if (window.innerWidth > 1100 && drawer.classList.contains('is-open')) setState(false);
    });
  }

  /* ---------- collapsible groups inside the mobile drawer ---------- */
  function mobileGroups() {
    var groups = all('.m-group');
    if (!groups.length) return;

    function setOpen(group, open) {
      var btn = group.querySelector('.m-toggle');
      group.classList.toggle('is-open', open);
      if (btn) btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    groups.forEach(function (group) {
      var btn = group.querySelector('.m-toggle');
      // start expanded when the group contains the page being viewed
      if (group.querySelector('.is-active, [aria-current]')) setOpen(group, true);
      on(btn, 'click', function () {
        var open = !group.classList.contains('is-open');
        // one open group at a time keeps the drawer short
        if (open) groups.forEach(function (g) { if (g !== group) setOpen(g, false); });
        setOpen(group, open);
      });
    });
  }

  /* ---------- reveal on scroll ---------- */
  function reveal() {
    var items = all('.reveal');
    if (!items.length) return;
    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseInt(el.getAttribute('data-delay') || '0', 10);
        setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------- animated counters ---------- */
  function counters() {
    var nums = all('[data-count]');
    if (!nums.length) return;

    function run(el) {
      var target = parseFloat(el.getAttribute('data-count'));
      // years and other bare numbers must not get a thousands separator
      var plain = el.hasAttribute('data-plain');
      var dur = 1600;
      var start = null;
      function frame(ts) {
        if (start === null) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        var v = Math.round(target * eased);
        el.textContent = plain ? String(v) : v.toLocaleString('en-US');  // Latin digits in both languages
        if (p < 1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }

    if (!('IntersectionObserver' in window)) { nums.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        run(entry.target);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    nums.forEach(function (el) { io.observe(el); });
  }

  /* ---------- accordions ---------- */
  function accordions() {
    all('.acc').forEach(function (acc) {
      var btn = acc.querySelector('.acc-btn');
      var panel = acc.querySelector('.acc-panel');
      if (!btn || !panel) return;

      if (acc.classList.contains('is-open')) {
        btn.setAttribute('aria-expanded', 'true');
        panel.style.maxHeight = panel.scrollHeight + 'px';
      } else {
        btn.setAttribute('aria-expanded', 'false');
      }

      on(btn, 'click', function () {
        var open = acc.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        panel.style.maxHeight = open ? panel.scrollHeight + 'px' : 0;
      });
    });

    on(window, 'resize', function () {
      all('.acc.is-open .acc-panel').forEach(function (p) { p.style.maxHeight = p.scrollHeight + 'px'; });
    });
  }

  /* ---------- back to top ---------- */
  function backToTop() {
    var btn = doc.querySelector('.to-top');
    if (!btn) return;
    on(window, 'scroll', function () {
      btn.classList.toggle('is-visible', window.scrollY > 500);
    }, { passive: true });
    on(btn, 'click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }

  /* ---------- contact form validation ---------- */
  function contactForm() {
    var form = doc.querySelector('[data-contact-form]');
    if (!form) return;
    var status = form.querySelector('.form-status');

    function fail(field, msg) {
      var wrap = field.closest('.field');
      wrap.classList.add('has-error');
      var err = wrap.querySelector('.err');
      if (err && msg) err.textContent = msg;
      return false;
    }

    function check(field) {
      var wrap = field.closest('.field');
      wrap.classList.remove('has-error');
      var val = (field.value || '').trim();

      if (field.hasAttribute('required') && !val) {
        return fail(field, 'This field is required.');
      }
      if (field.type === 'email' && val && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(val)) {
        return fail(field, 'Please enter a valid email address.');
      }
      if (field.type === 'tel' && val && !/^[0-9+()\-\s]{6,}$/.test(val)) {
        return fail(field, 'Please enter a valid phone number.');
      }
      return true;
    }

    all('input, select, textarea', form).forEach(function (f) {
      on(f, 'blur', function () { check(f); });
      on(f, 'input', function () {
        if (f.closest('.field').classList.contains('has-error')) check(f);
      });
    });

    on(form, 'submit', function (e) {
      e.preventDefault();
      var ok = true;
      all('input, select, textarea', form).forEach(function (f) { if (!check(f)) ok = false; });

      if (!ok) {
        var first = form.querySelector('.has-error input, .has-error select, .has-error textarea');
        if (first) first.focus();
        return;
      }

      if (status) {
        // the message is authored per language on the form element itself
        status.textContent = form.getAttribute('data-sent-message') || '';
        status.classList.add('is-visible');
        status.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      form.reset();
    });
  }

  /* ---------- keep "years of experience" current without a rebuild ---------- */
  function yearsSince() {
    all('[data-years-since]').forEach(function (el) {
      var from = parseInt(el.getAttribute('data-years-since'), 10);
      if (!from) return;
      var n = new Date().getFullYear() - from;
      if (n < 0) return;
      // the counter animation reads data-count, so update that too
      el.setAttribute('data-count', String(n));
      el.textContent = String(n);
    });
  }

  /* ---------- current year in footer ---------- */
  function year() {
    all('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  function init() {
    markActive();
    stickyHeader();
    mobileNav();
    mobileGroups();
    reveal();
    yearsSince();   // must run before counters() so it animates to the right figure
    counters();
    accordions();
    backToTop();
    contactForm();
    year();
  }

  if (doc.readyState === 'loading') on(doc, 'DOMContentLoaded', init);
  else init();
})();
