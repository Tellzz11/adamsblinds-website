filepath = r"C:\Users\user\OneDrive\Documents\AdamsBlinds\londonblinds_website_v1.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)
changes = []

# ============================================================
# TASK 1 — EMBED SHUTTER ANIMATION VIDEO IN HERO
# ============================================================

old_hero_img = '    <img src="images/hero-london-shutters.jpg" alt="London Victorian living room with white plantation shutters, golden morning light on herringbone oak floor" loading="eager" fetchpriority="high">'
new_hero_video = '''    <video class="hero-video" autoplay muted loop playsinline poster="images/hero-london-shutters.jpg" aria-label="Plantation shutters opening to reveal golden morning light in a London Victorian living room">
      <source src="images/shutter-animation.mp4" type="video/mp4">
      <img src="images/hero-london-shutters.jpg" alt="London Victorian living room with white plantation shutters, golden morning light on herringbone oak floor" loading="eager" fetchpriority="high">
    </video>'''

if old_hero_img in content:
    content = content.replace(old_hero_img, new_hero_video, 1)
    changes.append("Task 1: Hero video embedded")
else:
    changes.append("MISS Task 1: Hero img not found")

# Add .hero-video CSS after .hero-bg img block
old_hero_css = '''    .hero-bg img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 30%;
    }'''
new_hero_css = '''    .hero-bg img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 30%;
    }
    .hero-video {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 30%;
      display: block;
    }
    @media (max-width: 768px) {
      .hero-video { display: none; }
    }'''

if old_hero_css in content:
    content = content.replace(old_hero_css, new_hero_css, 1)
    changes.append("Task 1: hero-video CSS added")
else:
    changes.append("MISS Task 1: hero-bg img CSS not found")

# ============================================================
# TASK 4 — FIX SCROLL ANIMATIONS
# ============================================================

# 4a. Add .reveal-scale CSS + change .vis → .visible in animation CSS
old_reveal_css = '''    .reveal,
    .reveal-left,
    .reveal-right {
      opacity: 0;
      transition: opacity 0.8s var(--ease-out-expo), transform 0.8s var(--ease-out-expo);
    }
    .reveal { transform: translateY(40px); }
    .reveal-left { transform: translateX(-50px); }
    .reveal-right { transform: translateX(50px); }
    .reveal.vis,
    .reveal-left.vis,
    .reveal-right.vis {
      opacity: 1;
      transform: translate(0);
    }'''

new_reveal_css = '''    .reveal,
    .reveal-left,
    .reveal-right,
    .reveal-scale {
      opacity: 0;
      transition: opacity 0.8s var(--ease-out-expo), transform 0.8s var(--ease-out-expo);
    }
    .reveal { transform: translateY(40px); }
    .reveal-left { transform: translateX(-50px); }
    .reveal-right { transform: translateX(50px); }
    .reveal-scale { transform: scale(0.95); }
    .reveal.visible,
    .reveal-left.visible,
    .reveal-right.visible,
    .reveal-scale.visible {
      opacity: 1;
      transform: translate(0) scale(1);
    }'''

if old_reveal_css in content:
    content = content.replace(old_reveal_css, new_reveal_css, 1)
    changes.append("Task 4a: reveal CSS updated (.vis → .visible, reveal-scale added)")
else:
    changes.append("MISS Task 4a: reveal CSS block not found")

# 4b. Update IntersectionObserver JS — use .visible, include .reveal-scale
old_observer_js = '''  // 6. INTERSECTION OBSERVER — REVEAL ANIMATIONS
  (function() {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const els = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
    if (reduced) {
      els.forEach(el => el.classList.add('vis'));
      return;
    }
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('vis');
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(el => obs.observe(el));
  })();'''

new_observer_js = '''  // 6. INTERSECTION OBSERVER — REVEAL ANIMATIONS
  (function() {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const els = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    if (reduced) {
      els.forEach(el => el.classList.add('visible'));
      return;
    }
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(el => obs.observe(el));
  })();'''

if old_observer_js in content:
    content = content.replace(old_observer_js, new_observer_js, 1)
    changes.append("Task 4b: IntersectionObserver updated (.vis → .visible, reveal-scale included)")
else:
    changes.append("MISS Task 4b: observer JS block not found")

# 4c. Add .counter class to stat-num elements
for old_stat, new_stat in [
    ('<span class="stat-num" data-target="129">0</span>', '<span class="stat-num counter" data-target="129">0</span>'),
    ('<span class="stat-num" data-target="15">0</span>', '<span class="stat-num counter" data-target="15">0</span>'),
    ('<span class="stat-num" data-target="100">0</span>', '<span class="stat-num counter" data-target="100">0</span>'),
]:
    if old_stat in content:
        content = content.replace(old_stat, new_stat, 1)
        changes.append(f"Task 4c: counter class added to stat-num data-target={old_stat.split('data-target=')[1].split('>')[0]}")
    else:
        changes.append(f"MISS Task 4c: {old_stat[:60]}")

# ============================================================
# WRITE OUTPUT
# ============================================================

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nOriginal length: {original_len} chars")
print(f"New length:      {len(content)} chars")
print(f"\nChanges applied ({len(changes)}):")
for c in changes:
    print(f"  {'✓' if not c.startswith('MISS') else '✗'} {c}")

# Quick verification
print(f"\nVerification:")
print(f"  hero-video in HTML: {content.count('hero-video')}")
print(f"  shutter-animation.mp4: {content.count('shutter-animation.mp4')}")
print(f"  .reveal-scale defined: {content.count('reveal-scale')}")
print(f"  .visible used (CSS): {'visible' in content}")
print(f"  .vis used (old): {content.count('.vis,')}")
print(f"  counter class on stat-nums: {content.count('stat-num counter')}")
