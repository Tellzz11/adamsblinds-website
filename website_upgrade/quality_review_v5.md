# Quality Review — adamsblinds_website_v5.html
## Date: 2026-03-14
## Reviewer: Rise Advantage / Claude Agent

---

## Overall Score: 8.4/10

Significant upgrade over v4. The page is structurally excellent with strong CRO fundamentals, consistent brand compliance, and well-placed psychology triggers. Four critical issues need resolving before go-live — all are fixable in under an hour. The biggest concern is that both forms submit to nowhere (JavaScript demo mode only). Secondary concerns are two broken local image references and a minor warranty figure inconsistency.

---

## Critical Issues (Fix Before Going Live)

| # | Issue | Severity | Location |
|---|-------|----------|----------|
| 1 | **Forms not connected to backend** — both `#consultation-form` and `#samples-form` fire `e.preventDefault()` and show a toast, but submit no data anywhere. No leads will be captured. | BLOCKER | Lines 3536–3549 |
| 2 | **Broken image: `samples.png`** — the Free Samples section references `src="samples.png"` with no path prefix. This file does not exist in the repo root or `website_upgrade/`. The section will render a broken image above the form. | HIGH | Line 2786 |
| 3 | **Broken image: `team.png`** — the About section references `src="team.png"` with no path prefix. Same issue. Will show broken image next to the 4.9★ badge. | HIGH | Line 2877 |
| 4 | **Warranty inconsistency** — Trust Bar says "5-Year Guarantee on all products & fitting." FAQ answer says "5-year manufacturer's guarantee" + "fitting work guaranteed for 2 years." Client profile says "6-month warranty." These three figures contradict each other. Confirm the correct guarantee and standardise across all copy before launch. | MEDIUM | Trust bar (line 985), FAQ (line 2929), client profile |

---

## Section Scores

| Section | Score | Key Issues |
|---------|-------|------------|
| Hero | 9/10 | Excellent. Primary CTA visible, trust stats below fold but close. Minor: CTA button text says "FREE Home Survey" but sub-copy says "free home survey" — inconsistent capitalisation (cosmetic). |
| Trust Bar | 9/10 | Strong. 6 icons immediately after hero. "Which? Trusted Trader" in footer trust row — verify this accreditation is current/accurate. |
| Adams Difference | 8/10 | Good editorial section. Ghost CTA at bottom ("Book your free home consultation") is correct but low visual weight — consider upgrading to btn-secondary. |
| How It Works | 9/10 | Excellent 3-step visual with CTA after. Step images load from adamsblinds.co.uk — external dependency, will break if their server changes. |
| Before/After | 8/10 | Uses a single static image, not an actual before/after slider. Heading says "Before and after" but interaction doesn't deliver that. Consider renaming section or adding real slider. |
| Products Carousel | 8/10 | All 6 product images reference local `website_upgrade/product_images/prod_*.png` paths. Verify these files exist at deployment. |
| Shop Grid | 8/10 | Price anchoring is well done. Roller blind card (`prod_roller_new.png`) is in shop grid but not in carousel — minor inconsistency in product coverage. "Outdoor Blinds" is listed in footer but has no shop card. |
| Testimonials | 7/10 | 5 real reviews shown + link to Google. Reviews are short/thin — the two grid cards are single sentences. Featured quote is from a B2B MD for a residential-focused campaign. Should lead with a residential homeowner quote. No Google review widget embed (static text only — harder to trust). |
| Quote Calculator | 9/10 | Excellent conversion feature. After estimate, a booking prompt appears with "Book Your FREE Survey" — perfect. The calculator is client-side only (no data saved), but that is acceptable as it's purely lead-warming. |
| Gallery | 9/10 | Good masonry grid. All 5 images from adamsblinds.co.uk — external dependency. CTA at bottom is well placed. |
| Product Visualiser | 7/10 | Good concept but uses same product images as carousel/shop — not actual room-context visualisations. Branding says "Your home will be professionally photographed during the home visit" — this claim needs checking with client. |
| Free Samples | 6/10 | Form is not connected (Critical Issue #1). Image is broken (Critical Issue #2). The section is strategically excellent (Reciprocity principle) but non-functional. |
| About | 7/10 | Team image is broken (Critical Issue #3). The 4.9★ badge floating over the broken image will look poor. Copy is strong. |
| FAQ | 9/10 | 6 well-chosen questions covering price, fit, lead time, areas, guarantee and smart blinds. Accordion works. Dynamic FAQ schema injection is smart. Warranty figure inconsistency (Critical Issue #4). |
| Consultation Form | 7/10 | Form design is polished. Not connected (Critical Issue #1). No indication of what happens after submission (GHL? Email? WhatsApp?). Add a reassurance message below the submit button explaining the next step. |
| Footer | 8/10 | Comprehensive. "Which? Trusted Trader" badge appears — verify. Footer trust strip shows "129 Reviews" correctly. Privacy/Terms/Cookie links go to `#` (no pages exist). |

---

## Top 5 Quick Wins

1. **Connect both forms to GHL or a webhook** — this is the only blocker between the page and actual lead capture. Wire `#consultation-form` and `#samples-form` to GHL intake form or a Zapier/Make webhook that creates a contact + sends a notification to Tas. Estimated effort: 30 minutes.

2. **Replace `samples.png` and `team.png` with real images** — either upload the actual files to `website_upgrade/` or use existing live URLs from adamsblinds.co.uk. The broken images damage credibility most in the Free Samples and About sections.

3. **Move the featured testimonial to a residential customer** — "Joe E., Managing Director, A.C. Ltd" is a B2B commercial client. The Meta Ads campaign targets homeowners. Lead with Carla A., Adrian B. or another residential customer name.

4. **Add a post-submit confirmation message** — when the form submits, show an inline success state (not just a toast) that explains: "We'll call you on [number] within 2 hours." This reduces post-submission anxiety and increases perceived trust.

5. **Standardise the guarantee claim** — decide whether it is 5 years, 2 years fitting, or 6 months, and use one number everywhere. "5-year guarantee" is the strongest positioning and should be the standard if accurate.

---

## Psychology Score (Cialdini)

| Principle | Present? | Quality | Notes |
|-----------|----------|---------|-------|
| **Social Proof** | Yes | 8/10 | 4.9★ + 129 reviews in header, testimonials section, footer trust strip, hero counter. Review count is accurate (129 matches schema + display). Real reviewer names present. Weakness: reviews are short (1–2 sentences) and one is B2B. |
| **Authority** | Yes | 8/10 | BUILD Award 2021 prominent in announcement bar, trust bar, footer, hero stats. BBSA Accredited in footer. "Which? Trusted Trader" in footer — verify this is current. |
| **Scarcity / Urgency** | Weak | 4/10 | Announcement bar says "Book your free home survey" but no genuine urgency/scarcity language. "Most surveys completed within 48 hours" is reassurance, not urgency. Recommend: "Spring slots filling fast — book before [date]" or "Limited surveys available this month." |
| **Reciprocity** | Yes | 8/10 | Free Samples section is a strong reciprocity play. Free home survey itself is reciprocity. Calculator gives value before asking for anything. Section needs the form fixed to activate. |
| **Liking / Trust** | Yes | 9/10 | Brand voice is warm, personal, London-specific throughout. "Islington Victorian sashes to Canary Wharf apartments" is exactly right. "Est. 2009" family story in About. WhatsApp button reinforces personal access. |
| **Loss Aversion** | Weak | 4/10 | No loss aversion messaging detected. Suggest adding: "Without a professional measure, up to 1 in 5 DIY blind orders are returned or refitted at cost" or similar framing that makes inaction feel risky. |
| **Commitment / Consistency** | Good | 7/10 | The calculator creates micro-commitments before the booking form. Free samples create investment before the survey. The 3-step How It Works reduces perceived commitment of the first step. |

**Overall Cialdini Score: 7/10** — Strong on social proof, authority, reciprocity and liking. Urgency and loss aversion are the two missing levers that could meaningfully lift conversion rate.

---

## Mobile Readiness

| Check | Status | Notes |
|-------|--------|-------|
| Tap targets ≥48px | Pass | `.btn-primary` padding 1.1rem–1.2rem × 2.6rem renders well above 48px. Mobile hamburger is 22px icon with 0.4rem padding — technically passes but could be larger. |
| Body text ≥16px | Pass | Base is `font-size: 16px`. Global override `section p { font-size: max(1rem, 0.95em) }` enforces minimum. `.body-sm` at 0.9rem is an exception for decorative text. |
| Mobile sticky CTA bar | Pass | Appears at ≤768px with "Call", "WhatsApp", and "Free Consultation" — excellent. |
| WhatsApp float button | Pass | Repositions to `bottom: 5.5rem` on mobile to avoid overlap with sticky bar. |
| Hero on mobile | Pass | `height: 100svh` with `min-height: 500px`. Headline `clamp(2.2rem, 9vw, 3.2rem)` is readable. |
| Form fields on mobile | Pass | Both forms collapse to single column at ≤560px. |
| Product carousel on mobile | Pass | Scrolls horizontally, cards shrink to 270px. |
| Shop grid on mobile | Pass | 2-col at ≤900px, 1-col at ≤560px. |
| Navigation | Pass | Nav links hidden at ≤768px, hamburger shown. Mobile menu is full-screen overlay. |
| Announcement bar close | Pass | Close button has `padding: 0.3rem` — small but acceptable. |

**Mobile Readiness Score: 8.5/10** — Well-considered across the board. The sticky bar + WhatsApp float combination is a conversion asset on mobile that most competitors lack.

---

## Brand Compliance

| Check | Status | Notes |
|-------|--------|-------|
| Display font: Libre Bodoni | Pass | Loaded from Google Fonts. `--font-display: 'Libre Bodoni', Georgia, serif`. (Note: brief specifies "Bodoni Bold" — Libre Bodoni is the closest freely available equivalent. Accept.) |
| Body font: Candara | Pass | `--font-body: 'Candara', 'Candara Condensed', system-ui, sans-serif`. Candara is system-installed on Windows; system-ui fallback on other OS. |
| Primary CTA colour: Terracotta #C2704F | Pass | `--terracotta: #C2704F` defined and used consistently on all `.btn-primary`, `.nav-cta`, `.form-submit`, `.calc-submit`. |
| Accent colour: Aged Brass #B8956A | Pass | `--brass: #B8956A` used for accents, icons, section eyebrows. |
| Background: Cream #FAF8F5 | Pass | `--warm-white: #FAF8F5` used as body background. |
| Charcoal overlays #363330 | Pass | `--charcoal: #363330` used in hero overlay, footer, calculator. |
| Gold #D4AF64 — stars/awards | Partial | Brand spec says Gold #D4AF64 for stars/awards. The page uses `--brass: #B8956A` for star ratings (★★★★★). Suggest using #D4AF64 for star characters specifically to match brand spec. |
| No discount language | Pass | No "% off", "sale", "discount", "cheap" language found anywhere on page. |
| Brand voice: premium but approachable | Pass | Copy throughout is warm, personal, London-specific. "We come to you", "Our fitters leave your home cleaner than they found it", "Islington Victorian sashes" — all on-brand. |
| London-specific references | Pass | Kensington, Notting Hill, Chelsea, Islington, Canary Wharf, Clapham, Wimbledon, Richmond all mentioned. |
| No subcontractor positioning | Pass | "Our own fitters — not subcontractors" and "never subcontracted" appear explicitly. |
| Award-backed authority | Pass | BUILD 2021 in announcement bar, trust bar, footer — prominent. |

**Brand Compliance Score: 9/10** — Only notable gap is star rating colour (#B8956A brass vs #D4AF64 gold specified in brand guide).

---

## CRO / Conversion Rate Optimisation Score: 8/10

**What works well:**
- Primary CTA ("Book Your FREE Home Survey") is above the fold in the hero, in the nav, in How It Works, Before/After section, Shop grid, Gallery, Visualiser, and the final dark CTA section. Total of approximately 9 CTA placements — excellent coverage.
- Trust signals (4.9★, BUILD Award, 4,000 homes, 15 yrs) sit directly below the hero CTA — textbook CRO placement.
- The announcement bar leads with "BUILD Award Winners" before the CTA — authority then action.
- Quote calculator reduces friction by giving value before asking for contact details.
- Free Samples form is a lower-commitment entry point for fence-sitters.
- Mobile sticky bar ensures CTA is always reachable on mobile.

**What could be improved:**
- CTA language is inconsistent: "Book Free Survey" (nav), "Book Your FREE Home Survey" (hero), "Book Your Free Survey — No Obligation" (How It Works), "Book Your Consultation" (gallery), "Book Free Home Consultation" (visualiser), "Book My Free Home Visit" (form submit). Standardise to one phrase: recommend "Book Your FREE Home Survey."
- Value proposition is clear within 5 seconds: headline "Beautiful blinds. Fitted properly." is memorable but abstract. The sub-text carries the actual value prop. On very small screens this may require a scroll before the sub-text is visible.
- The form submit button says "Book My Free Home Visit" but the section is called "Free Consultation." Minor inconsistency.
- No exit-intent or time-on-page pop-up (acceptable for a premium brand, but worth testing).

---

## Message Match / Landing Page Quality Score: 8/10

For a Meta Ads lead gen campaign targeting London homeowners seeking free home surveys:

- "Free home survey" language is present in hero, nav, How It Works, announcement bar, and form — strong message match.
- "No obligation" appears in three locations — key objection handling for cold traffic.
- "We come to you" message aligns with what a lead gen ad would promise.
- Trust signals (reviews, award, years in business) appear within the first viewport — important for cold Meta traffic.
- The page is a single scroll-down experience with no distracting links away from the site — good for landing page quality.
- "We call you within 2 hours" appears under the hero CTA — excellent expectation setting for lead follow-up.
- Weakness: There is no explicit meta description telling Facebook/Instagram users what to expect when they click — though the OG tags are set. OG description ("Bespoke window dressings for London homes. Free consultation, expert fitting, 5-year guarantee.") is good but doesn't mention the specific offer.

---

## Schema.org Data Accuracy

| Field | Value in Schema | Accuracy |
|-------|----------------|---------|
| name | Adams Blinds | Correct |
| telephone | 020 7096 5030 | Correct |
| streetAddress | 124 City Road | Correct |
| postalCode | EC1V 2NX | Correct |
| ratingValue | 4.9 | Correct |
| reviewCount | 129 | Correct — matches display copy |
| openingHours | Mo-Fr 08:00-18:00, Sa 09:00-17:00 | Needs client confirmation |
| areaServed | London | Acceptable (could be more specific) |
| Dynamic FAQ schema | Injected via JS at runtime | Will not be crawled by search engines (must be in HTML, not JS-injected) — move to static `<script type="application/ld+json">` in `<head>` |

---

## Additional Observations

1. **CSS in `<style>` blocks scattered throughout `<body>`** — styles are embedded inside the HTML body (not in `<head>`). This is technically valid but non-standard. For production, consolidate all styles into the `<head>` block to avoid FOUC (flash of unstyled content) risk.

2. **Video file dependency** — Hero video references `website_upgrade/shutter_animation_min.mp4` (local file). On first load with `preload="none"`, the static fallback (`website_upgrade/shutter_open.png`) will show until video loads. This is correct behaviour but the static fallback image is also a local path — both must exist at deployment root.

3. **External image dependencies** — Six gallery images and three section images load from `https://www.adamsblinds.co.uk/london/z-images/`. If adamsblinds.co.uk changes its image paths or goes offline, those sections break. For production, download and host these locally.

4. **Privacy/Terms/Cookie links go to `#`** — three footer links are placeholder anchors. These need real pages (or at minimum, a modal with the actual policies) before the site is used in any paid advertising. Meta Ads policies require a working privacy policy link.

5. **"Which? Trusted Trader" claim in footer trust strip** — this is not confirmed in the client profile. If Adams Blinds is not currently registered as a Which? Trusted Trader, this claim must be removed before launch (consumer protection / advertising standards).

6. **`fa_dismissed` uses sessionStorage** — the announce bar dismissal only persists for the session, not across visits. Users who dismiss the bar will see it again on their next visit. Consider switching to localStorage with a 30-day expiry if the announcement is permanent.

7. **`label-caps` at 0.7rem** — these decorative uppercase labels are intentionally below 16px and exempt from the body text minimum rule (correctly noted in the CSS comment). Confirm the exemption is intentional.

---

## Verdict

**This page is ready for deployment pending resolution of the 4 critical issues.** The design quality, brand compliance, mobile experience and CRO structure are all at a level that will support paid traffic from Meta Ads. The two weakest conversion levers are urgency/scarcity (currently absent) and the non-functional forms (currently broken). Fix the forms first — without them, no leads will be generated regardless of traffic volume.

**Recommended pre-launch checklist:**
- [ ] Connect `#consultation-form` to GHL (or webhook)
- [ ] Connect `#samples-form` to GHL (or webhook)
- [ ] Replace `samples.png` with real image path
- [ ] Replace `team.png` with real image path
- [ ] Standardise guarantee claim (5-year? confirm with Tas)
- [ ] Verify "Which? Trusted Trader" accreditation
- [ ] Add working Privacy Policy page (required for Meta Ads)
- [ ] Move FAQ schema JSON-LD from JS injection to static `<head>` block
- [ ] Standardise CTA button text to "Book Your FREE Home Survey" across all instances
- [ ] Test all local image paths (`website_upgrade/product_images/prod_*.png`, `website_upgrade/shutter_*.png`) resolve correctly at deployment domain
