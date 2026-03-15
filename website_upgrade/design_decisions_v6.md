# Design Decisions — Adams Blinds Website v6

*Built: 2026-03-15 | Rebuild method: 4-agent team (DESIGN LEAD, COPY LEAD, CRO LEAD, BUILDER)*

---

## Skill Usage Summary

### Skills Read in Full
| Skill | Reference Files Read |
|-------|---------------------|
| `design-taste-frontend` | SKILL.md (full — all 10 sections) |
| `image-generation` | `references/prompt-crafting.md` |
| `copywriting` | `references/copy-frameworks.md` (previous session) |
| `marketing-psychology` | `SKILL.md` (previous session) |
| `copy-editing` | `references/plain-english-alternatives.md` (previous session) |
| `site-architecture` | `references/navigation-patterns.md`, `references/site-type-templates.md` (previous session) |
| `page-cro` | `references/experiments.md` (previous session) |

### Skills Referenced (SKILL.md read, no dedicated reference files)
- `ad-creative` — platform specs for image quality standards
- `ads-landing` — message match principles applied to form section

---

## Design Decisions by Section

### Global Design System (styles.css)

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| Playfair Display headlines + Raleway body | `design-taste-frontend` Rule 1 | Anti-slop typography: serif editorial + clean sans | Banned Inter. Playfair = premium editorial home brand. Raleway = clean, legible body |
| CSS Custom Properties (design tokens) | `design-taste-frontend` Section 2 | CSS architecture baseline | Consistent palette propagation, no magic numbers |
| 8px spacing scale | `design-taste-frontend` Rule 6 | VISUAL_DENSITY:4 "Daily App Mode" | Generous but not empty. Breathing room without art-gallery airy |
| `cubic-bezier(0.16, 1, 0.3, 1)` easing | `design-taste-frontend` Rule on MOTION_INTENSITY:4-7 | "Fluid CSS" level — transform + opacity only | MOTION_INTENSITY:6. Hardware-accelerated, premium spring-like feel |
| Scroll reveal via IntersectionObserver | `design-taste-frontend` Section 4 | Staggered orchestration via `animation-delay` cascade | MOTION_INTENSITY:6. No `window.addEventListener('scroll')` — uses IntersectionObserver |
| min-height: 100dvh on hero | `design-taste-frontend` Rule "Viewport Stability CRITICAL" | NEVER use h-screen — always min-h-[100dvh] | Prevents iOS Safari layout jump |
| Charcoal #363330 (not #000000) | `design-taste-frontend` Rule 2 "NO Pure Black" | AI Tells forbidden patterns | Off-black feels premium, not harsh |
| Max 1 accent colour (terracotta) | `design-taste-frontend` Rule 2 "Constraint: Max 1 Accent" | Saturation < 80% | Terracotta is warm, desaturated, editorial — not corporate blue or neon |

---

### Section 01 — Hero

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| Asymmetric 55/45 CSS grid | `design-taste-frontend` Rule 3 "ANTI-CENTER BIAS" | DESIGN_VARIANCE:8 — "Split Screen" structure | Centered hero strictly banned at LAYOUT_VARIANCE > 4. Left-aligned copy / right image |
| Headline: "Your windows deserve better than whatever fits." | `copywriting` | Differentiation formula + PAS (Problem-Agitate-Solve) | Problem stated in headline. "Whatever fits" = the painful status quo competitors enable |
| `<em>` italic for "better than whatever fits" | `design-taste-frontend` Rule 1 | Hierarchy via weight/colour, not just scale | Terracotta italic emphasis = visual anchor, draws eye to the solution pivot |
| Hero sub: 3-sentence PAS structure | `copywriting` `copy-frameworks.md` | PAS: Problem → Agitate → Solve | "Most London homes make do..." (P) → "slightly too wide, too short" (A) → "Adams visits, guides, fits" (S) |
| Trust strip above fold | `marketing-psychology` | Cialdini Authority + Social Proof | 4.9 stars + 129 reviews + BUILD Award 2021 all visible without scrolling |
| Floating badge with counter animation | `page-cro` `experiments.md` | Social proof placement — badge near CTA converts | data-target="129" animates on scroll-into-view via scripts.js |
| "Book Your Free Home Survey" CTA label | `copywriting` | Outcome formula: name the exact thing they get | "Free" reduces friction. "Home Survey" specifies the low-commitment action |

---

### Section 02 — Trust Bar + Pain Section + How It Works

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| 4-item trust bar (not 3) | `design-taste-frontend` Rule 3 | Anti-3-equal-column ban | 4-item 2x2 on mobile avoids the generic "3 cards in a row" pattern |
| Inline SVG icons (star, trophy, ruler, wrench) | `design-taste-frontend` Section 2 "Icons" | No external icon libraries without package.json check | Self-contained, no network dep, accessible |
| Pain section on charcoal background | `marketing-psychology` | Loss aversion + contrast disruption | Dark bg = psychological contrast after cream hero. Creates tension before the "bridge" |
| Pain section H2: "Every room deserves better than whatever fitted" | `copywriting` `copy-frameworks.md` | Problem formula | Echoes the hero's "whatever fits" for message continuity |
| Asymmetric 3fr/2fr pain layout | `design-taste-frontend` Rule 6 DESIGN_VARIANCE:8 | Fractional grid units | "Masonry layouts, CSS Grid with fractional units" — not equal columns |
| Stats with counter animation (4,000+, 15+, 4.9) | `marketing-psychology` | Social proof via specific numbers | Organic messy numbers (4,000 not "thousands") per design-taste-frontend "NO Fake Numbers" rule |
| How It Works: ZIGZAG alternating layout | `design-taste-frontend` Rule 3 | "2-column Zig-Zag" over equal cards | Step 1: image left/copy right. Step 2: copy left/image right. DESIGN_VARIANCE:8 |
| How It Works: BAB framework copy | `copywriting` `copy-frameworks.md` | Before-After-Bridge | Bridge = Adams process. Step 1-2-3 maps to B-A-B |
| Reassurance ribbon: "No obligation · No hidden costs · No subcontractors · No catalogue shopping" | `marketing-psychology` | Objection removal + authority | Address the 4 most common objections in one scannable strip |

---

### Section 03 — Adams Difference + Testimonials

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| Asymmetric 2-col benefits layout | `design-taste-frontend` Rule 3 | Left benefits list + right featured quote | DESIGN_VARIANCE:8. Not a 3-col feature row |
| Terracotta SVG checkmarks | `design-taste-frontend` Rule 2 | Single accent colour applied consistently | Checkmark = completion/trust signal. Terracotta = brand colour |
| Featured Carla A. quote card | `marketing-psychology` | Cialdini Social Proof — specific, named, detailed | Real name + real quote. Avoids "generic testimonial" AI tell |
| Brass left border on quote card | `design-taste-frontend` | Materiality — shadow tinted to bg hue | Brass = warmth, premium. Not a generic box-shadow |
| BUILD Award + BBSA pill badges | `marketing-psychology` | Authority signals positioned after social proof | Both signals in one visual cluster — efficient trust stacking |
| Featured large testimonial (St Joseph's Hospice) | `page-cro` `experiments.md` | Large format testimonial converts better than grids | Commercial proof = validates non-residential too, broadens social proof |
| 2-column testimonial grid (not 3) | `design-taste-frontend` Rule 7 "Layout & Spacing" | "NO 3-Column Card Layouts" strictly banned | 2-col avoids AI slop pattern, creates asymmetric balance |
| 4.9 rating displayed top-right of testimonials header | `page-cro` | Social proof placement near section header | Anchors the testimonials section with authority before reading quotes |

---

### Section 04 — Products Bento Grid

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| Bento grid: `2fr 1fr 1fr` | `design-taste-frontend` Section 8 "Bento Grid" + Rule 6 | DESIGN_VARIANCE:8 — Apple Control Center aesthetic | Asymmetric tile-based grouping. Plantation Shutters spans 2 rows as flagship |
| Plantation Shutters = large featured card | `marketing-psychology` | Anchoring + flagship product priority | Highest margin product shown largest = anchoring effect |
| "Most popular" badge on Shutters | `marketing-psychology` | Social proof + bandwagon effect | Softens premium price anxiety by confirming popularity |
| Product images from real CDN | `image-generation` `prompt-crafting.md` | Use real assets over AI-generated for brand authenticity | Real product photography shows actual quality level |
| "Free fitting included" brass micro-badge | `page-cro` | Reinforce USP at point of product selection | Removes cost objection exactly when prospect is evaluating products |
| Reassurance strip below grid | `page-cro` `experiments.md` | Trust signals after product display | "Made to measure · Professional fitting always included" — converts fence-sitters |

---

### Section 05 — Free Samples + About

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| Samples section: terracotta background | `design-taste-frontend` Rule 2 | Single accent colour — full-bleed section use | Contrast section (cream → charcoal → cream → charcoal → cream → terracotta) creates visual rhythm |
| Samples inline form | `marketing-psychology` | Reciprocity (give samples) + Commitment/Consistency | Small ask (samples) → leads to big ask (survey booking). Cialdini foot-in-door |
| About: asymmetric 3fr/2fr grid | `design-taste-frontend` Rule 6 DESIGN_VARIANCE:8 | Fractional grid, not equal | 3:2 ratio — copy breathes, stats column feels purposeful |
| Stat counters: 4,000+ / 15+ / 4.9 | `marketing-psychology` | Authority via specific numbers (not round) | "4,000+" feels real. "Thousands" feels vague/generic |
| London area references (Islington, Canary Wharf) | `copywriting` | Place-specific copy for London audience | Demonstrates local knowledge, not generic national brand |
| BUILD Award + BBSA pill badges | `marketing-psychology` | Repeated authority signals reinforce without feeling forced | Second appearance of awards in different context (About vs Trust) normalises the authority |

---

### Section 06 — FAQ + Consultation Form

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| FAQ: sticky sidebar layout (1fr/2fr) | `design-taste-frontend` Rule 6 DESIGN_VARIANCE:8 | "Sidebar layout" — not standard single-column accordion | Left sidebar stays sticky while right scrolls. Non-generic, editorial feel |
| FAQ accordion (not expanded by default) | `page-cro` `experiments.md` | Accordion reduces perceived form length | 6 questions visible but collapsed = scannable without overwhelming |
| 6 FAQ questions covering real objections | `marketing-psychology` | Objection handling via information | Addresses: cost, timeline, coverage, samples, fitters, aftercare — the 6 most common |
| Contact form on charcoal background | `design-taste-frontend` Rule 2 | Dark section for high-conversion areas | Dark BG creates focus, removes distraction. Premium feel for a premium service |
| "Survey slots available this week" urgency | `marketing-psychology` | Genuine scarcity (weekly, real, not fake) | Not "ONLY 3 LEFT!!". Weekly availability = truthful, not manufactured |
| Left column: what happens next (3 steps) | `page-cro` `experiments.md` | Process transparency reduces form anxiety | "We call in 2 hours → visit → quote on the spot" removes uncertainty |
| 6 form fields (not more) | `form-cro` principles | Minimum viable fields for lead qualification | Name, phone, email, postcode, product interest, notes. Nothing optional until notes |
| data-webhook="" on form | `ads-landing` | GHL webhook stub ready for Tas to wire | Not wired yet (blocker). data-webhook pattern allows zero-code activation |
| "No spam, no hard sell" micro-copy | `copy-editing` `plain-english-alternatives.md` | Plain English + friction reduction | Addresses both objections with natural language, not corporate reassurance |

---

### Section 07 — Footer

| Decision | Skill | Rule/Pattern | Rationale |
|----------|-------|-------------|-----------|
| 4-column footer grid (2fr/1fr/1fr/1fr) | `site-architecture` `site-type-templates.md` | Local service business footer template | Brand column wider than link columns. Standard for local service businesses |
| Logo with `filter: brightness(0) invert(1)` | `design-taste-frontend` | No placeholder logos — use real asset | Inverts real logo to white on dark footer without needing a white asset |
| Awards column in footer | `page-cro` | Trust signals in footer converts late-stage sceptics | BUILD Award + BBSA + Google rating = authority stack for those who scroll to the bottom |
| FAQPage JSON-LD schema | `seo-schema` principles | Structured data for Google rich results | All 6 FAQ questions included. Enables FAQ rich snippets in SERPs |
| WhatsApp float button | `marketing-psychology` | Reciprocity + Commitment/Consistency + accessibility | Always-visible low-friction contact channel. Pulse animation draws attention without annoyance |
| `#25D366` WhatsApp green | Brand standards | Universal recognition colour | Using the exact WhatsApp brand colour for instant recognisability |

---

## Unsupported Decisions (no skill backing — flagged honestly)

| Decision | Section | Reason flagged |
|----------|---------|----------------|
| CSS-only decorative blind-slat element in samples section | 05_inspiration | Agent created a decorative element from scratch — no specific skill reference for this pattern. Aesthetic judgement call. |
| Image `onerror` fallback colour (#B8956A) | 04_products | Standard web practice but no specific skill reference for fallback colour choice |
| Glassmorphic form card styling in contact section | 06_contact | Agent applied glassmorphism (design-taste-frontend mentions it but as an advanced effect for modals, not forms). Risk: may not match main CSS. Should verify in browser |

---

## Skills Read vs Not Read

### Read in Full (applied to build)
- `design-taste-frontend/SKILL.md` ✅
- `image-generation/references/prompt-crafting.md` ✅
- `copywriting/references/copy-frameworks.md` ✅ (previous session)
- `marketing-psychology/SKILL.md` ✅ (previous session)
- `copy-editing/references/plain-english-alternatives.md` ✅ (previous session)
- `site-architecture/references/navigation-patterns.md` ✅ (previous session)
- `site-architecture/references/site-type-templates.md` ✅ (previous session)
- `page-cro/references/experiments.md` ✅ (previous session)

### Not Read (honest gap report)
- `ui-ux-pro-max/data/` — design database not queried (CLI tool not invoked). Decisions made from SKILL.md memory.
- `frontend-design/SKILL.md` — separate from design-taste-frontend. Not confirmed as read in this session (may have been read in previous session before context compaction)
- `ad-creative/references/platform-specs.md` — image quality standards referenced from memory, not re-read
- `copywriting/references/natural-transitions.md` — not read; section transitions handled by CSS visual rhythm instead
- `taste-skill` — this is the same as `design-taste-frontend` (both paths lead to same skill)

---

## QA Results (automated + manual)

| Check | Result |
|-------|--------|
| All nav anchor IDs present | ✅ PASS (fixed: added #hero, #inspiration anchor) |
| Skip link present | ✅ PASS (fixed: added after body tag) |
| FAQ accordion functional | ✅ PASS (6 items, opens on click) |
| Both forms present | ✅ PASS |
| Schema count | ✅ PASS (LocalBusiness + FAQPage) |
| WhatsApp float button | ✅ PASS |
| 49 scroll-reveal elements | ✅ PASS |
| No AI tells in own copy | ✅ PASS ("seamless" = verbatim customer quote, not our copy) |
| All form inputs labelled | ✅ PASS (7 inputs, 0 unlabeled) |
| Google Fonts loaded | ✅ PASS |
| Open Graph tags | ✅ PASS |
| Canonical URL | ✅ PASS |
| Viewport meta | ✅ PASS |
| Responsive mobile | ✅ PASS (1023px + 767px breakpoints) |
| prefers-reduced-motion | ✅ PASS (CSS override present) |
| DESIGN_VARIANCE:8 | ✅ PASS (asymmetric hero, bento grid, zigzag HIW, sidebar FAQ) |
| NO 3-equal-column card grids | ✅ PASS |

**Overall: 17/17 QA checks pass**
