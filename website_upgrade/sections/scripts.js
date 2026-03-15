/* Adams Blinds v6 — scripts.js */

(function () {
  'use strict';

  /* ─── Announcement Bar ─────────────────────────────────────────── */
  const announcementDismiss = document.querySelector('.announcement-close');
  if (announcementDismiss) {
    announcementDismiss.addEventListener('click', function () {
      const bar = document.querySelector('.announcement-bar');
      if (bar) {
        bar.style.maxHeight = bar.scrollHeight + 'px';
        requestAnimationFrame(function () {
          bar.style.transition = 'max-height 0.3s ease, opacity 0.3s ease';
          bar.style.maxHeight = '0';
          bar.style.opacity = '0';
          bar.style.overflow = 'hidden';
        });
        setTimeout(function () { bar.remove(); }, 350);
      }
    });
  }

  /* ─── Sticky Nav ────────────────────────────────────────────────── */
  const nav = document.querySelector('.nav-wrapper');
  if (nav) {
    let lastScroll = 0;
    window.addEventListener('scroll', function () {
      const currentScroll = window.pageYOffset;
      if (currentScroll > 80) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
      lastScroll = currentScroll;
    }, { passive: true });
  }

  /* ─── Mobile Nav ────────────────────────────────────────────────── */
  const hamburger = document.querySelector('.nav-hamburger');
  const drawer = document.querySelector('.nav-mobile');
  const drawerClose = document.querySelector('.nav-drawer-close');
  const drawerOverlay = document.querySelector('.nav-drawer-overlay');

  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add('open');
    document.body.classList.add('nav-open');
    if (drawerOverlay) drawerOverlay.classList.add('visible');
    hamburger && hamburger.setAttribute('aria-expanded', 'true');
  }

  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove('open');
    document.body.classList.remove('nav-open');
    if (drawerOverlay) drawerOverlay.classList.remove('visible');
    hamburger && hamburger.setAttribute('aria-expanded', 'false');
  }

  if (hamburger) hamburger.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if (drawerOverlay) drawerOverlay.addEventListener('click', closeDrawer);

  // Close drawer on nav link click
  document.querySelectorAll('.nav-mobile a').forEach(function (link) {
    link.addEventListener('click', closeDrawer);
  });

  // Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeDrawer();
  });

  /* ─── Scroll Reveal (IntersectionObserver) ──────────────────────── */
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  if (revealEls.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    // Fallback: show all immediately
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* ─── FAQ Accordion ─────────────────────────────────────────────── */
  document.querySelectorAll('.faq-item').forEach(function (item) {
    const trigger = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    if (!trigger || !answer) return;

    trigger.addEventListener('click', function () {
      const isOpen = item.classList.contains('open');

      // Close all others
      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        openItem.classList.remove('open');
        const a = openItem.querySelector('.faq-answer');
        if (a) { a.style.maxHeight = '0'; }
        const q = openItem.querySelector('.faq-question');
        if (q) q.setAttribute('aria-expanded', 'false');
      });

      if (!isOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
        trigger.setAttribute('aria-expanded', 'true');
      }
    });

    // Init
    answer.style.maxHeight = '0';
    trigger.setAttribute('aria-expanded', 'false');
  });

  /* ─── Active Nav Link (scroll spy) ─────────────────────────────── */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a[href^="#"], .nav-drawer a[href^="#"]');

  if (sections.length && navLinks.length && 'IntersectionObserver' in window) {
    const spyObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach(function (link) {
            link.classList.toggle('active', link.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });

    sections.forEach(function (s) { spyObserver.observe(s); });
  }

  /* ─── Consultation Form ─────────────────────────────────────────── */
  const consultForm = document.getElementById('consultation-form');
  if (consultForm) {
    consultForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const btn = consultForm.querySelector('button[type="submit"]');
      const originalText = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

      const formData = new FormData(consultForm);
      const data = {};
      formData.forEach(function (v, k) { data[k] = v; });

      // GHL webhook — replace URL when Tas provides it
      const WEBHOOK_URL = consultForm.dataset.webhook || '';

      if (!WEBHOOK_URL) {
        // Dev mode: show success immediately
        showFormSuccess(consultForm);
        return;
      }

      fetch(WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
        .then(function (res) {
          if (res.ok) {
            showFormSuccess(consultForm);
          } else {
            showFormError(consultForm, btn, originalText);
          }
        })
        .catch(function () {
          showFormError(consultForm, btn, originalText);
        });
    });
  }

  function showFormSuccess(form) {
    const wrapper = form.closest('.form-wrapper') || form.parentElement;
    wrapper.innerHTML = [
      '<div class="form-success">',
      '<div class="form-success-icon">✓</div>',
      '<h3>We\'ll be in touch within 2 hours</h3>',
      '<p>One of our London consultants will call you back to arrange your free measuring visit.</p>',
      '<p class="form-success-note">While you wait, feel free to browse our inspiration gallery or order free samples.</p>',
      '</div>',
    ].join('');
  }

  function showFormError(form, btn, originalText) {
    if (btn) { btn.disabled = false; btn.textContent = originalText; }
    let errEl = form.querySelector('.form-error-msg');
    if (!errEl) {
      errEl = document.createElement('p');
      errEl.className = 'form-error-msg';
      errEl.style.cssText = 'color:#c0392b;margin-top:12px;font-size:0.9rem;';
      form.appendChild(errEl);
    }
    errEl.textContent = 'Something went wrong — please call us on 020 3745 6525 or WhatsApp below.';
  }

  /* ─── Samples Form ──────────────────────────────────────────────── */
  const samplesForm = document.getElementById('samples-form');
  if (samplesForm) {
    samplesForm.addEventListener('submit', function (e) {
      e.preventDefault();
      showFormSuccess(samplesForm);
    });
  }

  /* ─── Smooth Scroll (anchors) ───────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      const offset = nav ? nav.offsetHeight + 16 : 80;
      const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
      window.scrollTo({ top: top, behavior: 'smooth' });
    });
  });

  /* ─── Gallery Lightbox ──────────────────────────────────────────── */
  const galleryItems = document.querySelectorAll('.gallery-item img');
  if (galleryItems.length) {
    // Create lightbox
    const lb = document.createElement('div');
    lb.id = 'lightbox';
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Image viewer');
    lb.innerHTML = [
      '<div class="lightbox-backdrop"></div>',
      '<div class="lightbox-content">',
      '<button class="lightbox-close" aria-label="Close">&times;</button>',
      '<img class="lightbox-img" src="" alt="">',
      '<p class="lightbox-caption"></p>',
      '</div>',
    ].join('');
    document.body.appendChild(lb);

    const lbImg = lb.querySelector('.lightbox-img');
    const lbCaption = lb.querySelector('.lightbox-caption');

    function openLightbox(src, alt) {
      lbImg.src = src;
      lbImg.alt = alt || '';
      lbCaption.textContent = alt || '';
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
      lb.classList.remove('open');
      document.body.style.overflow = '';
    }

    galleryItems.forEach(function (img) {
      img.style.cursor = 'zoom-in';
      img.setAttribute('tabindex', '0');
      img.addEventListener('click', function () { openLightbox(img.src, img.alt); });
      img.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') openLightbox(img.src, img.alt);
      });
    });

    lb.querySelector('.lightbox-close').addEventListener('click', closeLightbox);
    lb.querySelector('.lightbox-backdrop').addEventListener('click', closeLightbox);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeLightbox();
    });
  }

  /* ─── Lightbox CSS (injected) ───────────────────────────────────── */
  const lbStyle = document.createElement('style');
  lbStyle.textContent = [
    '.lightbox{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:opacity 0.25s ease,visibility 0.25s ease;}',
    '.lightbox.open{opacity:1;visibility:visible;}',
    '.lightbox-backdrop{position:absolute;inset:0;background:rgba(0,0,0,0.88);}',
    '.lightbox-content{position:relative;max-width:min(90vw,960px);max-height:90vh;display:flex;flex-direction:column;align-items:center;gap:12px;}',
    '.lightbox-img{max-width:100%;max-height:80vh;object-fit:contain;border-radius:4px;}',
    '.lightbox-caption{color:rgba(255,255,255,0.7);font-size:0.875rem;text-align:center;}',
    '.lightbox-close{position:absolute;top:-40px;right:0;background:none;border:none;color:#fff;font-size:2rem;cursor:pointer;line-height:1;padding:4px 8px;}',
    '.lightbox-close:hover{color:#B8956A;}',
  ].join('');
  document.head.appendChild(lbStyle);

  /* ─── Hero counter animation ────────────────────────────────────── */
  function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    if (isNaN(target)) return;
    const duration = 1200;
    const start = performance.now();
    function step(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target) + (el.dataset.suffix || '');
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  const counterEls = document.querySelectorAll('[data-target]');
  if (counterEls.length && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counterEls.forEach(function (el) { counterObserver.observe(el); });
  }

  /* ─── Skip link focus fix ───────────────────────────────────────── */
  const skipLink = document.querySelector('.skip-link');
  if (skipLink) {
    skipLink.addEventListener('click', function () {
      const main = document.getElementById('main-content');
      if (main) { main.tabIndex = -1; main.focus(); }
    });
  }

})();
