# Quality Review — Adams Blinds Website v4
**File reviewed:** `adamsblinds_website_v4.html`
**Review date:** 2026-03-14
**Reviewer:** Rise Advantage / OpenClaw QA

---

## Executive Summary

v4 is a strong, polished page. The brand identity is cohesive, the conversion funnel is well-structured, and trust signals are present throughout. The primary CTA is clear and repeated at every logical decision point. However there are several conversion-critical issues that need resolving before the page is used as a paid ad landing destination: the forms do not submit to a real backend, the review count in structured data does not match the stated count in copy, and the video hero carries meaningful page-weight risk on mobile. There are also minor psychology and messaging gaps that are straightforward to fix.

---

## 1. CRO Assessment

### Primary CTA — PASS
The primary CTA "Book Your FREE Home Survey" is in the hero, above the fold, in terracotta (#C2704F) on a dark overlay. It is visually dominant and repeated at minimum eight times across the page (hero, how-it-works, before-after, gallery, visualiser, final form section, footer, mobile sticky bar). The CTA label is consistent and benefit-led.

**Issue — minor:** The hero CTA says "FREE Home Survey" but the final form section says "Free Home Visit" and the nav says "Free Consultation". These are the same thing but the inconsistency creates micro-friction. Pick one and use it everywhere. Recommend: "Free Home Visit" (most tangible, least salesy).

### Trust Signals — PASS with gaps
Trust signals appear in the hero (stats bar), immediately below the fold (trust bar), and throughout the page. The following are present and correctly placed:
- 4.9 Google rating (hero stats, testimonials section)
- BUILD Award 2021 (hero stats, trust bar, footer accreditations)
- 4,000+ homes (hero stats, before-after, testimonials, about)
- 5-year guarantee (trust bar, FAQ)
- Free home visit (trust bar, announcement bar, forms)
- BBSA Member (footer accreditations only — see issue below)

**Issue — critical:** BBSA membership is mentioned only in the footer accreditation bar in tiny low-contrast text. For a London bespoke blinds audience this is a meaningful trust signal and should appear in the trust bar or about section with proper prominence.

**Issue — critical:** The structured data (Schema.org) shows `"reviewCount": "847"` but the testimonials section copy reads "847 Google reviews" while the brand brief states 129 reviews. These three numbers must be reconciled. Using an inflated review count in Schema.org can trigger Google trust penalties and misleads users. The correct number (129, per brand brief) should be used consistently or updated to a verified current count.

### Value Proposition Clarity — PASS
Within 5 seconds a user can read: "Your home deserves windows dressed beautifully — Made-to-measure blinds, plantation shutters and curtains — crafted for London homes. Free home survey, expert fitting, 5-year guarantee." This is clear, differentiated, and locally specific. No discount positioning, correctly in line with brand rules.

### Friction Reducers — PASS
- "No obligation. We call within 2 hours." appears directly below the hero CTA button.
- "No hard sell — just expert advice." in the final form section.
- "No commitment required" in the calculator section.
- "No obligation, no hard sell" in the samples checklist.
- "We take your privacy seriously" note in the samples form.

The "we call within 2 hours" promise is a strong commitment. It must be operationally deliverable — if it cannot be guaranteed during evenings/weekends, qualify it with "during business hours" (as is done in the form note, but not in the hero).

### Lead Capture Form Quality — PARTIAL FAIL
The main consultation form (`#consultation-form`) collects: full name, phone, email, postcode, product of interest, and optional message. This is an appropriate data set for a home visit lead — not over-long, not under-specified.

**Issue — critical:** The form `addEventListener('submit')` calls `e.preventDefault()` and shows a toast notification only. There is no backend POST, no API call, no webhook, no email notification. This is demo/placeholder code. The form does not currently capture any leads. This must be connected to a real submission endpoint (e.g. Formspree, Netlify Forms, a CRM webhook, or a direct API) before any paid traffic is sent to this page.

**Issue — medium:** There is no `name` attribute on the free samples form inputs, which means the form data cannot be serialised correctly even if a backend were added. The consultation form inputs have `id` attributes but several lack `name` attributes — verify this before wiring to a backend.

**Issue — medium:** There is no client-side validation feedback. If a user submits with an empty required field, the browser native validation fires but there is no styled inline error state. For a premium brand this looks rough and reduces completion rates, particularly on mobile.

### Social Proof Placement — PASS
Testimonials section is well-positioned: after product presentation and the before-after section, before the calculator and final CTA. The featured quote is specific (named person, location, product type) which is the highest credibility format. The two supporting cards are also specific and conversational in tone — they do not read as fabricated.

**Issue — minor:** The testimonial section heading says "847 Google reviews" — this conflicts with the brand brief (129 reviews). See review count issue above.

**Issue — minor:** There is no link or badge to the live Google Business Profile review page. A "Read all [X] reviews on Google" link anchored to the actual GMB URL would add verification credibility and is a standard pattern for service businesses.

---

## 2. Landing Page Quality (Ads Assessment)

### Message Match — PASS
The page headline "Made-to-measure blinds, plantation shutters and curtains — crafted for London homes" directly matches the ad messaging for bespoke London blinds. The London-specific copy (Kensington, Notting Hill, Chelsea, Dulwich, Clapham, Islington) appears across multiple sections, reinforcing geographic relevance for London-targeted ad audiences. No mismatch between ad promise and page delivery.

### Mobile Experience Readiness — PASS with one issue
Responsive breakpoints are defined at 1024px, 900px, 768px, 640px, 560px, and 480px. The mobile sticky bar (Call / WhatsApp / Free Consultation) is present and correctly positioned. The hamburger menu opens a full-screen mobile nav. The body gets `padding-bottom: 70px` to account for the sticky bar.

**Issue — medium:** On mobile the hero CTA "Book Your FREE Home Survey" is the correct primary button but the mobile sticky bar labels it simply "Free Consultation". The mismatch in label between what users just saw (FREE Home Survey) and what appears sticky at the bottom may cause hesitation. Align labels.

**Issue — minor:** The mobile menu does not contain the phone number or WhatsApp link. A user who opens the mobile nav to find contact details will not find them there — they must close the menu and look elsewhere. Add click-to-call to the mobile menu.

### Page Speed — FLAG
The hero uses an autoplay video (`shutter_animation_min.mp4`). Even a "min" compressed video for a full-viewport hero will typically be 2–6 MB. On a mobile 4G connection this introduces a flash of the static poster image before the video loads.

**Specific risks:**
- No `preload="none"` or `preload="metadata"` attribute on the `<video>` tag. The browser will start downloading the video immediately on page load, consuming bandwidth before any conversion asset has loaded.
- The Google Fonts request (`Libre Bodoni`) is loaded via standard stylesheet link. For a paid landing page, self-hosting this font or using `font-display: swap` with a preconnect (already present) is preferable.
- All `<style>` blocks are inline (no external CSS file), which is correct for a single-page landing scenario — this is fine.
- No `loading="lazy"` on below-fold product images. With 12+ product images below the fold, this will increase initial page load weight significantly.

Recommendation: Add `preload="none"` to the video tag. Add `loading="lazy"` to all product and gallery images below the fold. Self-host Libre Bodoni or subset it.

### Form Quality for Lead Gen — as above (see section 1)
The form data fields are correct for a home visit lead. The backend connection is missing (critical). Phone number is collected, which is correct for a local service business — phone-qualified leads close at higher rates than email-only.

### WhatsApp as Conversion Path — PASS
WhatsApp is well-implemented:
- Floating button (desktop and mobile) with pulse animation to attract attention
- Mobile sticky bar includes a WhatsApp button with green colouring (`rgba(37,211,102,0.15)` background, `#25D366` text)
- WhatsApp number is correctly formatted as international (`442070965030`)
- Link opens in new tab with `rel="noopener noreferrer"`

**Issue — minor:** The floating WhatsApp button has `z-index: 150` and the toast notification has `z-index: 300`. On mobile, if a toast fires (e.g. after form submission), it renders on top of the WhatsApp button area. The toast position on mobile is `bottom: 5rem` and the WhatsApp button is `bottom: 5.5rem` — they will overlap. Adjust z-indices or toast position.

---

## 3. Marketing Psychology

### Authority Signals — STRONG
| Signal | Present | Placement |
|---|---|---|
| 4.9 Google rating | Yes | Hero, testimonials, about section badge |
| BUILD Award 2021 | Yes | Hero stats, trust bar, footer |
| 15 years experience | Yes | Hero stats (Est. 2009), about section |
| 4,000+ homes fitted | Yes | Multiple placements |
| BBSA Member | Yes | Footer only — too buried |
| Which? Trusted Trader | Yes | Footer only — too buried |
| Greater London Enterprise 2020 | Yes | Footer only |
| 5-year guarantee | Yes | Trust bar, FAQ |
| "Never subcontracted" | Yes | How-it-works, about section |
| "Our own trained team" | Yes | How-it-works step 3 |

The "never subcontracted" and "white-glove fitting" messaging are strong differentiators for the London premium home market and are used well.

**Gap:** BBSA and Which? Trusted Trader are not surfaced in the trust bar or anywhere mid-page. These are meaningful third-party validations that cost nothing to surface more prominently.

### Social Proof — GOOD
- Three detailed, specific testimonials with location and product type
- 4.9★ rating displayed prominently in the testimonials header
- "847 reviews" displayed (see review count accuracy issue above)
- 4,000+ homes counter with animated count-up
- 98% would recommend stat in the before-after section
- Neighbourhood name-dropping throughout (Kensington, Chelsea, Dulwich etc.) — this is correctly applied social proof for London audiences

**Gap:** No video testimonial or linked Google review. For a service business a single authentic screen-captured Google review screenshot would add verifiability.

### Loss Aversion — WEAK
The page does not currently use any loss aversion framing. This is a missed psychology lever. Examples that would comply with the no-discount brand rule:
- "Most London homeowners who don't book a home visit end up buying off-the-shelf blinds that don't fit properly." (before-after section)
- "Spring/summer is our busiest fitting period — we recommend booking your consultation early to secure your preferred slot." (announcement bar or below hero CTA)
- "Each home visit slot takes our consultant off the road — we can only offer [X] consultations per week in [their area]."

None of these involve discounts and all are factually plausible for a small London specialist.

### Scarcity and Urgency — ABSENT
No urgency framing exists on the page. This is the biggest psychology gap. For a premium bespoke service, manufactured discount-style urgency is rightly avoided, but *capacity-based* urgency is both authentic and effective:

- "Book early — home visit slots fill 2–3 weeks ahead during spring" (announcement bar)
- Lead time framing in how-it-works: "7–14 days from consultation to fitting — book now to transform your home before [season]"
- "Our consultants cover [London area] on [days] — available slots this week" (dynamic or generic)

The current announcement bar says "Free home survey, free measuring, free fitting advice" which is purely informational and wastes the high-visibility placement. An urgency-oriented message here would lift CTR to the form meaningfully.

### Reciprocity — EXCELLENT
This is the page's strongest psychology play:
- Free fabric samples form (dedicated section with its own high-commitment delivery)
- Free home survey (no obligation)
- Free measuring
- Calculator giving a ballpark estimate before any commitment
- "See it before you commit" visualiser

The three-step funnel of Samples → Calculator → Consultation is well-designed. Users can get value at each stage without committing at any stage. This reduces drop-off at the top of the funnel.

**Issue — medium:** The free samples form and the consultation form are presented as separate, parallel paths. There is no explicit sequencing guidance telling users "not ready to book? Start with free samples." The page assumes users will self-select. A text nudge between the two sections would increase samples opt-ins from users who are not yet ready to book.

### Commitment and Consistency — GOOD
The funnel from Calculator → Samples → Consultation is structurally sound. Each micro-commitment (getting a quote estimate, ordering samples) psychologically primes users toward the bigger commitment (booking a home visit).

**Issue — medium:** After the calculator returns a price estimate, the only next step offered is the terracotta button "Get My Estimate" — but there is no inline prompt to then "Book your consultation to get your exact price." A calculator result that ends with a link to the form section would dramatically improve conversion from calculator users, who are the warmest visitors on the page.

---

## 4. Key Issues — Priority Order

### Critical (Fix Before Live Traffic)

1. **Forms not connected to a backend.** Both the consultation form and samples form show a toast notification only — no leads are captured. This is the most urgent issue. Connect to a real endpoint before any paid ad traffic arrives on this page.

2. **Review count inconsistency.** Structured data shows 847 reviews, the testimonials section copy says "847 Google reviews", but the brand brief states 129 reviews. Using an incorrect count in Schema.org structured data is a Google Trust violation risk. Audit the actual live Google review count and update all three instances to the same verified number.

3. **Video hero preload not controlled.** No `preload` attribute on the `<video>` tag means browsers download the video immediately, adding 2–6 MB to initial page load. Add `preload="none"` to defer video loading until the user has interacted with the page.

4. **CTA label inconsistency.** "FREE Home Survey" vs "Free Home Visit" vs "Free Consultation" used interchangeably. Standardise to one phrase across all touchpoints.

---

### Medium (Fix Within 1 Sprint)

5. **No urgency or loss aversion on the page.** The announcement bar, hero sub-copy, and before-after section all have room for capacity-based urgency messaging. Add one clear urgency signal — particularly in the announcement bar which is the highest-visibility position.

6. **Calculator result does not link to the consultation form.** After a user receives an estimate, there is no inline call to action to book. Add a "Get your exact price — book a free home visit" button that appears within the calculator result area.

7. **Form inputs missing `name` attributes.** Before wiring any backend, audit all form inputs to ensure they have correct `name` attributes for proper data serialisation.

8. **No client-side validation feedback.** Add styled inline error states for required fields. Particularly important for phone and postcode fields which have format requirements.

9. **Below-fold product images lack `loading="lazy"`.** There are approximately 14+ images below the hero. Add `loading="lazy"` to all product cards, gallery items, and about/samples images to reduce initial load weight.

10. **BBSA and Which? Trusted Trader buried in footer.** Move at least one third-party accreditation (BBSA or Which? Trusted Trader) into the trust bar or the about section. These are credibility signals that most competitors cannot match.

11. **Mobile menu lacks phone and WhatsApp links.** A user opening the hamburger menu on mobile likely wants to contact the business. Add click-to-call and WhatsApp links to the mobile nav.

12. **Samples → Consultation funnel lacks sequencing language.** Add a nudge line between the samples section and the consultation form: "Already got your samples? Book your free home visit" or similar.

---

### Nice-to-Have (Backlog)

13. **Google Reviews link absent.** Add "Read all [X] reviews on Google →" with a link to the Google Business Profile in the testimonials section. Provides independent verification.

14. **No neighbourhood-specific landing page variants.** The copy mentions Kensington, Chelsea, Dulwich etc. but the page is generic. For paid search campaigns, consider thin variants with neighbourhood-specific H1 and body copy ("Made-to-measure blinds in Clapham"). Significant quality score uplift.

15. **WhatsApp button z-index conflict with toast on mobile.** Adjust z-index or position to prevent overlap after form submission.

16. **Announcement bar message is purely informational.** This is the highest-attention real estate on the page — use it for urgency or a lead magnet prompt, not a feature list.

17. **No `og:image` meta tag.** When this URL is shared on social or via WhatsApp the link preview will have no image. Add an `og:image` pointing to a high-quality 1200×630 brand image.

18. **Google Fonts dependency for Libre Bodoni.** Self-host or subset the font file to eliminate the external dependency and reduce render-blocking risk. The preconnect hints are already in the `<head>` which helps, but self-hosting is preferable for a production landing page.

19. **BBSA is mentioned in footer accreditations but not in the BBSA's actual membership tone.** Verify the membership is current and that the wording ("BBSA Member") matches what the membership certificate actually states.

20. **Scroll reveal on hero elements may delay CTA visibility on slow connections.** Elements with `.reveal` start at `opacity: 0`. If JS is slow to load on a budget mobile device, the hero CTA will be invisible. Consider removing the reveal animation from the primary hero CTA specifically, or ensuring the CSS initial state falls back gracefully.

---

## Brand Compliance Checklist

| Rule | Status |
|---|---|
| Terracotta CTAs (#C2704F) | PASS |
| No discounts or % off | PASS — none present |
| 4.9 Google rating referenced | PASS |
| BUILD 2021 Award referenced | PASS |
| Free measuring AND fitting | PASS |
| Independent London specialist | PASS |
| Bodoni headlines | PASS (Libre Bodoni loaded via Google Fonts) |
| Candara body/CTAs | PASS (declared as CSS variable, system font fallback) |
| Cream #FAF8F5 background | PASS |
| Aged Brass #B8956A accents | PASS |
| Charcoal #363330 overlays | PASS |

**Note on typography:** The CSS declares `'Candara', 'Candara Condensed', system-ui, sans-serif` for body text. Candara is a Microsoft/Windows font and is not available on iOS or macOS without fallback. The `system-ui` fallback will render as San Francisco on Apple devices. This is acceptable but if brand typography fidelity across devices is a priority, a web-safe fallback closer to Candara (e.g. Trebuchet MS) should be added between Candara Condensed and system-ui.

---

*Review conducted by Rise Advantage — OpenClaw QA pipeline. Next review recommended after backend integration and review count correction.*
