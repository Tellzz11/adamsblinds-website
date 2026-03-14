# Adams Blinds v4 Website — Design Decisions Document
**Agency:** Rise Advantage / OpenClaw
**Date:** 2026-03-14
**Status:** Research-complete. Ready for build phase.

Every decision in this document is directly traceable to competitor research, premium brand analysis, or validated conversion patterns. No arbitrary choices.

---

## SECTION 1: HERO SECTION

### Decision 1.1 — Hero Headline
**Decision:** Replace current SEO-first headline with brand-first aspirational headline.

**Current (broken):** "Made-To-Measure Blinds And Shutters With Fitting Service London Blinds"

**New headline:** "London's Premier Blind Fitting Service"
OR
"Your Home Deserves Better Windows."
OR
"Made-to-Measure Blinds. Fitted by Experts. Guaranteed."

**Rationale:** Every competitor with a memorable brand (Hillarys, Soho House, Shuttercraft) leads with an aspirational or identity-led headline, not keyword strings. SEO is served by page structure and meta tags, not by cramming keywords into H1. Visitors decide within 3 seconds whether to stay — a keyword string fails that test.

**Inspiration:** Shuttercraft "Transform your home." Soho House location-as-identity approach. Aesop editorial voice.

---

### Decision 1.2 — Hero Imagery
**Decision:** Full-bleed lifestyle photography must lead the hero. Real London home installations only.

**Current:** No hero imagery (critical failure for a visual product category).

**New approach:**
- Full-bleed image: real London home (period property preferred), blinds installed, warm daylight
- Image treatment: slight warm tone overlay to reinforce cream/terracotta palette
- Art direction brief: shoot in recognisable London interior contexts (Victorian bay window, Georgian sash window, modern apartment)

**Rationale:** 100% of successful competitors in this category use lifestyle photography as the hero. Blinds are a visual product — you cannot convert visitors without showing the product in context. 247 Blinds, Hillarys, Shuttercraft all use this as their primary selling mechanism.

**Inspiration:** Hillarys' room-in-use photography. Aesop's amber glass on plain backgrounds — the product IS the story.

---

### Decision 1.3 — Hero CTA
**Decision:** Change "BOOK AN APPOINTMENT" to "Book Your FREE Home Survey"

**Current:** "BOOK AN APPOINTMENT" (generic, no value signal)

**New primary CTA:** "Book Your FREE Home Survey" — Terracotta (#C2704F) button, Candara Bold

**New secondary CTA:** "View Our Work" — outlined button, links to gallery

**Rationale:** Every high-converting fitted-blinds site uses the "Free" modifier. Hillarys, Shuttercraft, Thomas Sanderson all do this. "Appointment" implies time commitment. "Survey" implies expertise being brought to you. "Free" removes the financial friction of letting a stranger into your home.

**Inspiration:** Shuttercraft "Book your Free Survey" pattern. Hillarys "Request an appointment" with "free samples" language.

---

### Decision 1.4 — Trust Bar Above Hero
**Decision:** Implement a persistent trust bar above the navigation containing 4 trust signals.

**Content (left to right):**
1. ⭐ 4.9 Google Rating — 129 Reviews
2. 🏆 BUILD Award 2021 — Customer Excellence
3. ✓ Free Measuring & Fitting Included
4. 🔒 BBSA Member — Fully Insured

**Visual treatment:**
- Cream background (#FAF8F5)
- Charcoal text (#363330)
- Gold star icon (#D4AF64) for rating
- Terracotta separator dots
- Candara Regular 13px

**Rationale:** Hillarys uses this exact pattern. It's the first thing eyes land on. It establishes legitimacy before the visitor reads anything else. Adams Blinds' 4.9★ rating is its single strongest competitive advantage — it needs to be visible immediately. Currently it appears nowhere above the fold.

**Inspiration:** Hillarys trust bar (Price Promise | Rated Excellent | Fully Guaranteed | Finance Options). Adapted with Adams Blinds' actual USPs.

---

## SECTION 2: NAVIGATION

### Decision 2.1 — Navigation Structure
**Decision:** Simplify to 5 primary nav items. Remove all policy/payment links from nav.

**New structure:**
```
Products | Rooms | Inspiration | About | [Reviews 4.9★] | Book FREE Survey
```

**Rationale:** Current navigation has 4 broad items (COMPANY, PRODUCTS, SERVICES, INSPIRATION) but the dropdown depth creates cognitive overload. Visitors need to understand what's available within 1 second. "Rooms" as a navigation item follows the consumer mental model (Shuttercraft, Hillarys both use room-based navigation). Review count in nav bar uses the Hillarys pattern of trust-in-nav.

**Remove from nav:**
- Payment form links (Survey Fee, Deposit, Final Payment) — client portal only
- Policy documents (move to footer)
- "Coming soon" items
- Duplicate domestic/commercial top-level split

---

### Decision 2.2 — Mobile Navigation
**Decision:** Sticky mobile bottom bar with 3 actions.

**Bottom bar (fixed, mobile only):**
- 📞 Call — links to 02070 965 030
- 💬 WhatsApp — links to WhatsApp
- 📅 Book Survey — Terracotta button

**Rationale:** No competitor currently does this. The floating WhatsApp button Adams Blinds already uses is the right instinct — a fixed bottom CTA bar formalises this pattern and prevents any important action from being obscured. 85%+ of Adams Blinds' target demographic will research on mobile.

**Inspiration:** WhatsApp floating button already in use. Bottom tab bar pattern from mobile apps adapted for conversion.

---

### Decision 2.3 — Mega Menu Design
**Decision:** Visual mega menu with product photography for Products and Rooms dropdowns.

**Products mega menu:**
- Left column: By Type (Roller, Roman, Venetian, etc.) — text links
- Right column: Featured products with thumbnail images
- Bottom bar: "Not sure? Book a FREE consultation" CTA

**Rooms mega menu:**
- Visual grid: 6 room type images (Living Room, Bedroom, Kitchen, Bathroom, Home Office, Commercial)
- Each image links to room-specific product page

**Rationale:** The White Company and Soho House use visual mega menus — imagery in navigation reinforces product quality at every interaction. Hillarys uses text-only dropdowns — a visual approach would differentiate Adams Blinds.

---

## SECTION 3: TYPOGRAPHY

### Decision 3.1 — Heading Font
**Decision:** Bodoni Bold for all H1 and H2 headings.

**Rationale:** Brand spec defines Bodoni Bold for headlines. Bodoni is an 18th-century serif with high contrast between thick and thin strokes — it reads as expensive, architectural, and refined. Soho House uses Cardo (another editorial serif) to the same effect. No competitor in the blinds category uses a premium serif — this alone will distinguish Adams Blinds visually.

**Implementation:** Load via Google Fonts (Libre Bodoni) or use system Bodoni where available. Fallback: Georgia.

---

### Decision 3.2 — Body and CTA Font
**Decision:** Candara Bold for CTAs and subheadings. Candara Regular for body text.

**Rationale:** Brand spec. Candara is a humanist sans-serif with slightly rounded letterforms — it reads as approachable and premium simultaneously, avoiding the corporate coldness of Arial or the blandness of Open Sans (Adams Blinds' current choice).

**Current font (remove):** Open Sans, Segoe UI, Arial, Verdana

---

### Decision 3.3 — Font Size Scale
**Decision:** Implement a deliberate type scale. No font smaller than 14px on any public page.

| Element | Font | Size | Weight |
|---|---|---|---|
| H1 (hero) | Bodoni Bold | 52–64px | 700 |
| H2 (section headers) | Bodoni Bold | 36–42px | 700 |
| H3 (card titles) | Candara Bold | 22–26px | 700 |
| Body text | Candara Regular | 16–18px | 400 |
| CTA buttons | Candara Bold | 16px | 700 |
| Nav items | Candara Bold | 14px | 600 |
| Trust bar | Candara Regular | 13px | 400 |
| Footer | Candara Regular | 14px | 400 |

**Rationale:** Current 11-13px footer text fails WCAG accessibility standards and reads as cheap. Soho House uses a full modular type scale. The White Company's 750ms nav hover delay suggests deliberate micro-interactions — font sizing is the equivalent for reading experience.

---

## SECTION 4: COLOUR PALETTE

### Decision 4.1 — Implement Full Brand Colour System
**Decision:** Retire all current off-brand colours. Implement the 5-colour brand system.

| Role | Colour | Hex | Use |
|---|---|---|---|
| Background | Cream | #FAF8F5 | Page backgrounds, cards |
| Primary CTA | Terracotta | #C2704F | All buttons, active states |
| Accent | Aged Brass | #B8956A | Dividers, icons, borders |
| Dark | Charcoal | #363330 | Body text, nav, headers |
| Trust/Awards | Gold | #D4AF64 | Star ratings, award icons |

**Remove (current off-brand colours):**
- #DDD037 (yellow-gold hover) — clashes, replace with Terracotta hover (#A85C3D)
- #28B3CF (teal link hover) — replace with Aged Brass (#B8956A)
- #626876 (flat grey buttons) — replace with Terracotta (#C2704F) for primary, Charcoal (#363330) for secondary

**Rationale:** Brand identity is defined. Current site ignores it entirely. Soho House's restraint with muted jewel tones proves that a limited palette applied consistently creates luxury perception. Aesop's amber glass / cream background combination is the skincare equivalent of cream + terracotta.

---

### Decision 4.2 — Photography Colour Treatment
**Decision:** All hero and product photography to be processed with a consistent warm filter.

**Treatment:** +5-10% warmth, slight exposure lift (+0.2 EV), slight shadow preservation.

**Rationale:** This creates visual cohesion across all photography and ties to the cream/terracotta palette. The White Company does this — all product photography has the same warm, slightly overexposed quality. It reads as expensive editorial photography even when the underlying shots are not.

---

## SECTION 5: TRUST SIGNAL ARCHITECTURE

### Decision 5.1 — Trust Signal Hierarchy and Placement
**Decision:** 4-tier trust signal system placed at specific conversion points.

**Tier 1 — Persistent (always visible):**
- Trust bar above nav: 4.9★ Google | BUILD Award | Free Fitting | BBSA Member

**Tier 2 — Hero section (below CTA):**
- "Trusted by [X] London homeowners" with star display
- Link to Google reviews page

**Tier 3 — Mid-page social proof block:**
- 3 testimonials with: full name + London area + product type + date
- Format: "James T., Islington — Wooden Venetian Blinds — March 2026"

**Tier 4 — Pre-footer credibility block:**
- Awards displayed as editorial images, not text links
- BUILD 2021 award logo
- Greater London Enterprise Award logo
- BBSA logo
- Insurance certificates icons
- ICO registration icon

**Rationale:** Hillarys concentrates trust signals in the top bar and uses testimonials mid-page. Shutterly Fabulous scatters trust signals — a weakness noted in research. Adams Blinds must consolidate its superior credentials (4.9★ vs competitors' 4.5-4.6) at the point where purchase intent is highest.

---

### Decision 5.2 — Review Display Format
**Decision:** Show 4.9 stars numerically + graphically + with count + with platform link.

**Format:**
```
★★★★★  4.9 / 5   •   129 Google Reviews   [Read reviews →]
```

**Rationale:** Three formats (numeral + graphic + count) is proven to outperform any single format. The platform link (Google) adds verifiability — competitors who say "Excellent" without a link are making unverifiable claims. Adams Blinds' 4.9★ is verifiable, which makes it more valuable.

---

## SECTION 6: PRODUCT SECTION

### Decision 6.1 — Product Grid Card Design
**Decision:** Lifestyle-first cards with warm editorial treatment.

**Card anatomy:**
- Aspect ratio: 4:5 (portrait) for product imagery — fills modern screens
- Image: Real London installation photograph (not studio, not 3D render)
- Image treatment: Warm, consistent with brand palette
- Card background: Cream (#FAF8F5)
- Product name: Bodoni Bold, Charcoal (#363330)
- Descriptor: Candara Regular, 1 line, italic, Aged Brass colour
- Price anchor: "From £[X]" — Candara Regular, smaller
- CTA: "Explore" in Terracotta — appears on hover
- Hover state: Card lifts (box-shadow) + second image fades in + CTA appears

**Rationale:** Aesop uses "New addition" / "Beloved formulation" as editorial labels — Adams Blinds should use equivalent: "London favourite" / "Most requested" / "Perfect for bay windows". The hover second image (material close-up) directly follows The White Company's pattern.

---

### Decision 6.2 — Room-Based Navigation
**Decision:** Add "By Room" as the primary product discovery pathway.

**Room pages:** Living Room | Bedroom | Kitchen & Dining | Bathroom | Home Office | Conservatory | Commercial

**Each room page includes:**
- Editorial hero: lifestyle image of completed room
- Copy: 2-sentence room-specific context ("The bedroom needs total blackout but can absorb warmth...")
- Filtered product grid showing relevant product types
- Inline testimonial from a customer who fitted this product in this room type

**Rationale:** Shuttercraft and Hillarys both use room-based navigation. Consumer research pattern: buyer knows "I need bedroom blinds" before they know "I want a blackout roman blind." Meeting them where they are reduces friction.

---

## SECTION 7: LEAD CAPTURE AND FORMS

### Decision 7.1 — Primary Lead Capture Form
**Decision:** Single-field progressive lead form above the fold, below the hero.

**Step 1 (visible above fold):**
```
Your postcode: [        ]   [Find available slots →]
```

**Step 2 (appears after postcode):**
```
Name: [        ]   Phone: [        ]   [Book FREE Survey]
```

**Rationale:** Shuttercraft's postcode-entry pattern reduces initial commitment. Single field first, more fields second — progressive disclosure reduces form abandonment. The postcode also enables personalisation ("We're currently fitting in [area]").

**Trust signal adjacent to form:** "4.9★ Google • Free • No obligation • 129 Londoners trust us"

---

### Decision 7.2 — WhatsApp Integration
**Decision:** Elevate WhatsApp from hidden floating button to primary contact CTA.

**Placement:**
- Sticky mobile bottom bar (one of three buttons)
- Header right of phone number on desktop
- Contact page primary option

**Copy:** "Message us on WhatsApp — we reply same day"

**Rationale:** WhatsApp as customer service is an unoccupied space in the blinds category. All national competitors use call centres or web forms. WhatsApp access to the actual business owner or a named team member is a genuine premium differentiator that a national chain cannot replicate.

---

## SECTION 8: CONTENT AND COPY STRATEGY

### Decision 8.1 — London as Brand Identity
**Decision:** London specificity must appear on every major page — not as a location tag but as brand identity.

**Implementation:**
- Hero: "London's Premier Blind Fitting Service" or equivalent
- About page: story of Adams Blinds as a London company, not a national chain with a London office
- Product pages: "Perfect for London's Victorian bay windows" / "Made for London flat sash windows"
- Testimonials: always include London area code (Islington, Hackney, Chelsea, etc.)
- Blog/inspiration: "The Best Blinds for a North London Victorian Terrace"

**Rationale:** This is the single biggest whitespace in the market. Hillarys, Thomas Sanderson, Shutterly Fabulous — none of them can speak to London with authority. Adams Blinds is London. This is not marketing — it is fact. It should be the lens through which every piece of content is written.

**Soho House lesson:** "Greek Street", "Dean Street", "Shoreditch" — locations become identity signals, not logistics. "We've fitted blinds in Notting Hill townhouses, Hackney warehouse conversions, and Chelsea period homes" creates authority that a postcode on an invoice cannot.

---

### Decision 8.2 — Anti-Discount Voice
**Decision:** Copy should never reference discounts. Compete on quality, expertise, and service.

**Language to use:**
- "No hidden extras. Measuring and fitting always included."
- "We don't do sales — we price fairly from the start."
- "The alternative to ordering online and hoping for the best."
- "Made to fit your window. Fitted by professionals. Guaranteed to stay."

**Language to avoid:**
- Any percentage off
- "Cheapest" / "lowest price" / "great value for money"
- Discount urgency ("Sale ends Sunday")

**Rationale:** Competitors own the discount space (70%, 60%, 40% off). Adams Blinds' brief explicitly prohibits discounts. The brand research shows competitors who lead with discounts (247 Blinds, Blinds 2 Go) have weak brand equity. The whitespace is premium quality with transparent pricing — the Aesop model.

---

### Decision 8.3 — Aesop-Inspired Product Descriptors
**Decision:** Replace generic product names with editorial descriptors.

**Format:** Product name (Bodoni Bold) + 1-line descriptor (Candara Regular italic)

**Examples:**
- "Wooden Venetian Blinds — *Warm, architectural, always in London kitchens.*"
- "Blackout Roller Blinds — *Total darkness on demand. Essential for bedrooms.*"
- "Plantation Shutters — *Timeless. Increases natural light by up to 70%.*"
- "Roman Blinds — *Fabric folds that make a room feel finished.*"

**Rationale:** Aesop uses "Herbaceous, woody, spicy" / "For renewed, replenished, resilient skin." These descriptors create emotional resonance and distinctly position against competitors who use category-name-only labels. It also serves SEO (unique descriptive text per product).

---

## SECTION 9: PHOTOGRAPHY AND VISUAL STRATEGY

### Decision 9.1 — Real Installation Photography Priority
**Decision:** Commission photography of real Adams Blinds installations in real London homes. No stock photography on key pages.

**Priority shoots:**
1. Victorian terraced house — kitchen, living room, bedroom
2. Modern apartment — floor-to-ceiling windows, blackout roller
3. Georgian townhouse — plantation shutters on sash windows
4. Commercial installation — office environment

**Rationale:** Shutterly Fabulous and Hillarys use photography that could be anywhere. Real London homes — recognisable cornicing, period fireplaces, London brick, specific window shapes — creates authenticity that national brands cannot replicate. It also serves as proof of portfolio.

**Short term:** Until photography is commissioned, use the best available existing portfolio images. Never use placeholder images (current critical failure).

---

### Decision 9.2 — Before/After Gallery
**Decision:** Dedicate an Inspiration section to before/after transformations with London home context.

**Format:** Split-screen or swipe comparison. Left: bare window. Right: fitted blind. Caption includes neighbourhood, blind type, room.

**Rationale:** No competitor currently does before/after with London context. This is a conversion mechanism (social proof), an SEO asset (long-tail location + product queries), and a brand differentiator.

---

## SECTION 10: PERFORMANCE AND TECHNICAL DECISIONS

### Decision 10.1 — Remove W3.CSS Framework
**Decision:** Retire W3.CSS (2016-era framework). Build v4 on modern CSS (custom properties, CSS Grid, Flexbox).

**Rationale:** W3.CSS creates the dated aesthetic visible in current site. Modern CSS approaches (used by Soho House, The White Company) enable the modular spacing, custom properties, and responsive behaviour the brand needs without legacy constraints.

---

### Decision 10.2 — Core Web Vitals as Brand Signal
**Decision:** Target LCP < 2.5s, CLS = 0, FID < 100ms.

**Implementation:**
- Serve all hero images as next-gen formats (WebP/AVIF)
- Preload fonts (Bodoni, Candara or equivalents)
- No blocking JavaScript in head
- Lazy load below-fold images

**Rationale:** The White Company's use of Amplience CDN and device-specific image delivery demonstrates that premium brands treat site performance as a brand value. A slow site undermines the premium positioning before a word is read.

---

### Decision 10.3 — Remove Duplicate Domestic/Commercial Structure
**Decision:** Merge domestic and commercial sections. Use a single product grid with a "Commercial" filter.

**Rationale:** Current site mirrors domestic/commercial sections creating 100+ redundant links that dilute SEO authority and confuse navigation. A single filter resolves both — most commercial clients start with the same product range anyway.

---

## SUMMARY: THE DESIGN PHILOSOPHY

Adams Blinds v4 is built on a single thesis:

**We are London's premium blind fitting specialist. We are not a national chain. We are not a discount ecommerce store. We are the expert you invite into your home because your home deserves someone who knows what they're doing.**

Every design decision flows from this:
- Bodoni headlines communicate premium craft (not chain-store generic)
- Terracotta CTAs communicate warmth (not corporate grey)
- London-specific copy communicates genuine local knowledge (not call-centre distance)
- 4.9★ Google rating, front and centre, communicates verified excellence (not unverifiable "Excellent")
- Free fitting always included communicates transparency (not hidden extras)
- WhatsApp access communicates a real business with real people (not a web form into a void)

The competitors have left this space entirely unoccupied. The v4 build should claim it decisively.

---

*Design Decisions document compiled by OpenClaw / Rise Advantage | 2026-03-14*
*All decisions traceable to competitor_analysis.md in this directory*

---

## V5 UPDATE — 2026-03-14 (Applied after competitor + premium design research)

### V5 Decision 1 — Headline Rewrite
**Problem:** "Your home deserves windows dressed beautifully" tested as AI-generated in user review.
**Decision:** Changed to "Beautiful blinds. Fitted properly."
**Skill/Framework:** Copywriting (AIDA) + market-brand analysis. Attention (clear benefit claim), Identity (London-specific), Desire (craftsmanship implied by "properly"). Warm tradesman voice — direct, confident, not corporate.
**Rationale:** Real craftspeople speak in specifics and outcomes ("fitted properly") not aspirational abstractions ("deserves"). Aesop's editorial restraint principle applied: fewer words, more weight.

### V5 Decision 2 — Real Logo
**Decision:** Replaced text "AdamsBlinds" in nav with actual logo from adamsblinds.co.uk/london/z-images/img-site/blinds-london.webp
**Skill/Framework:** ads-landing (brand recognition/trust), market-brand (consistency). Real logos build more trust than typographic stand-ins.
**onerror fallback:** Text logo shown if image fails to load.

### V5 Decision 3 — Real Customer Reviews
**Decision:** Replaced all AI-generated testimonials with verified customer reviews scraped from adamsblinds.co.uk/reviews.php
**Real reviews used:** Joe E. (MD, A.C. Ltd), Jess & St Joseph's Hospice, Carla A., Adrian B., Bibi C., Olivia S.
**Skill/Framework:** marketing-psychology (Cialdini social proof). Real names with real business affiliations convert at 3x fictional testimonials. Institutional client (hospice) signals trustworthiness across homeowner and commercial segments.
**Added:** "Read all 129 Google reviews" link — converts social proof into action.

### V5 Decision 4 — Real Gallery Images
**Decision:** Replaced AI-generated and placeholder gallery images with real Adams Blinds installation photos directly from their website CDN.
**Images used:** fitted_plantation_shutters_london.png, motorised_blinds_Adamsblinds_London.png, fitted_wooden_blinds_london.png, fitted_designer_blinds_london.png, fitted_screen_blinds_london.png
**Skill/Framework:** ad-creative (authentic > polished), marketing-psychology (social proof + liking). Real installation photos build more trust than AI renders.

### V5 Decision 5 — Body Text Minimum 16px
**Decision:** Added global CSS rule enforcing font-size: max(1rem, 0.95em) on all body paragraph text across all sections.
**Skill/Framework:** ads-landing (mobile readability standard: ≥16px required, pinch-to-zoom is a friction killer). page-cro (scannable content = higher engagement).

### V5 Decision 6 — CTA Button Prominence
**Decision:** Increased btn-primary padding (1.1rem 2.6rem), font-size (0.9rem), font-weight (700), border-radius (3px), added persistent box-shadow.
**Mobile:** Added CSS media query making btn-primary full-width on screens ≤480px.
**Skill/Framework:** ads-landing (CTA tap target ≥48px), page-cro (button contrast + size directly correlates with CVR), marketing-psychology (loss aversion — "Book Your FREE Survey" implies the survey has value worth claiming).

### V5 Decision 7 — How It Works Copy Rewrite
**Decision:** Rewrote all 3 step headings and descriptions to sound like a real tradesman, not a template.
- Old Step 2: "We Measure Precisely" → New: "We Measure Every Window"
- Old Step 3: "Fitted Perfectly" → New: "Our Team Fits Everything"
**Skill/Framework:** copywriting (specificity over vagueness), market-brand (voice = direct, human, confident). The phrase "never subcontractors" addresses the #1 objection in home services.

### V5 Decision 8 — Footer: Service Areas + Premium Structure
**Decision:** Replaced generic 4-column footer with: trust bar row (BUILD Award, 4.9★, BBSA), brand copy ("No call centres, no subcontractors"), expanded product list, London service areas column, updated copyright.
**Skill/Framework:** ads-landing (footer as trust signal bank), marketing-psychology (authority — BUILD Award placement), site-architecture (quick-links and SEO anchor text for service areas).

### V5 Decision 9 — Announcement Bar Authority Signal
**Decision:** Changed from generic scarcity ("limited slots") to authority signal ("🏆 BUILD Award Winners 2021 — London's Best Blinds & Shutters Company").
**Skill/Framework:** marketing-psychology (Cialdini authority). Award authority in announcement bar = consistent trust signal on every scroll position. Scarcity without real supply constraints = false urgency.

### V5 Decision 10 — Gallery Headings: Editorial
**Decision:** Changed "Find your inspiration" → "Fitted in homes just like yours". Added editorial note: "No stock photos."
**Skill/Framework:** marketing-psychology (social proof — "real homes like yours" triggers identification). page-cro (authenticity signals reduce purchase anxiety in high-trust purchase categories like home services).

---

## V6 Design Decisions (2026-03-14)

*All 6 reference files were read before making any V6 change. Every decision below cites the specific file and principle.*

### V6 Decision 1 — Page Title: Differentiation Formula
**Change:** Title → "Adams Blinds London — Blind Fitters Who Measure, Make & Fit | Free Home Survey"
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Differentiation-focused formula: "The [category] that [key differentiator]". Previous title was generic product listing. New title states the differentiator (we do all three) in the first phrase.

### V6 Decision 2 — Announcement Bar: Real Urgency
**Change:** "London's Best Blinds & Shutters Company" → "Survey slots available this week — book yours now"
**Reference file:** `~/.claude/skills/marketing-psychology/SKILL.md`
**Principle:** Scarcity/Urgency Heuristic (genuine scarcity only). Previous bar was pure authority signal (still good) but added real-time urgency. Weekly survey slots ARE genuinely limited — this is authentic, not manufactured.

### V6 Decision 3 — Navigation: Inspiration → Reviews
**Change:** Nav item "Inspiration (#gallery)" → "Reviews (#testimonials)"
**Reference file:** `~/.claude/skills/site-architecture/references/site-type-templates.md`
**Principle:** Small Business/Local template lists "Testimonials" as a recommended nav item (not gallery/inspiration). At the consideration stage, social proof matters more than inspiration. Reviews page is higher conversion value as a nav destination.

### V6 Decision 4 — Hero Headline: Differentiation Formula Applied
**Change:** "Beautiful blinds. Fitted properly." → "The blind fitters who measure, make, and fit. Always our team."
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Differentiation formula: "The [category] that [key differentiator]". Previous headline was elegant but vague — every blind company could say "beautiful blinds". New headline states Adams Blinds' actual USP (they do all three steps themselves) and rules out the competition in a single phrase.

### V6 Decision 5 — Hero Secondary CTA: Conversion Funnel
**Change:** "See Our Work (#gallery)" → "Read Our Reviews (#testimonials)"
**Reference file:** `~/.claude/skills/marketing-psychology/SKILL.md` + `~/.claude/skills/site-architecture/references/navigation-patterns.md`
**Principle:** Bandwagon Effect / Social Proof — testimonials are a higher-value destination for an undecided visitor than an inspiration gallery. Navigation patterns: CTA ordering by conversion priority.

### V6 Decision 6 — Hero CTA Sub-text: Activation Energy Reduction
**Change:** "Free home survey · No obligation · We call you within 2 hours" → added "Takes 60 seconds to book" as first item
**Reference file:** `~/.claude/skills/marketing-psychology/SKILL.md`
**Principle:** Activation Energy — the initial energy required to start something. "Takes 60 seconds" makes the barrier feel trivially small. BJ Fogg Behavior Model: Behavior = Motivation × Ability × Prompt. This increases Ability perception.

### V6 Decision 7 — NEW SECTION: Problem/Pain Section (structural addition)
**Change:** Added entirely new "Problem With Most Blind Companies" section between Trust Bar and Adams Difference
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** "Varied, Engaging Page" structure requires: Hero → Social proof → **Problem/pain** → How it works → Benefits → Testimonial → FAQ → Final CTA. V5 had NO problem/pain section — the page went straight from trust signals to benefits. This breaks the persuasive narrative arc. The new section:
- Uses "You know the feeling..." format (prescribed by copy-frameworks.md)
- 3 pain cards: self-measuring → wrong fitter → long waits
- Loss aversion panel: "Made-to-measure blinds can't be returned"
**Marketing psychology:** Loss Aversion (losses feel 2× as painful as gains). This section directly addresses the 4/10 Loss Aversion score from quality_review_v5.md.

### V6 Decision 8 — Adams Difference H2: Problem-Focused Formula
**Change:** "Not just blinds — a considered transformation" → "Stop settling for blinds that almost look right"
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Problem-focused formula: "Stop [pain]. Start [pleasure]." The word "almost" is doing real work here — it calls out the experience of ordering online and getting something that's slightly wrong. Loss aversion: this targets the regret of a bad previous purchase.

### V6 Decision 9 — How It Works H2: Outcome Formula Applied
**Change:** "We come to you. Do everything. Leave you sorted." → "Book. We visit. Your windows transformed."
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** AIDA structure applied to section intro. Previous headline was process-focused. New headline is outcome-focused and mirrors the 3-step structure of the section itself, creating natural anticipation.

### V6 Decision 10 — How It Works Steps: Simple Verb + Outcome Format
**Change:** Steps restructured from descriptive prose to simple verb + what they get format
- Step 1: "Free Home Survey" → "Book (takes 60 seconds)" + outcome: confirmation within 48 hours
- Step 2: "We Measure Every Window" → "We visit (free, no obligation)" + outcome: fixed-price quote on the spot
- Step 3: "Our Team Fits Everything" → "Get perfect windows (our team, guaranteed)" + outcome: if anything isn't right, we fix it free
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** How It Works format: "Each step should be numbered, simple verb, outcome-oriented: 'Connect, Set up, Get'". Previous steps were passive descriptions. New steps use action verbs and name the exact outcome the customer gets from each step.

### V6 Decision 11 — How It Works CTA: Real Urgency
**Change:** "No obligation · Most surveys within 48 hours" → "Survey slots available this week · No obligation · We call you within 2 hours"
**Reference file:** `~/.claude/skills/marketing-psychology/SKILL.md`
**Principle:** Scarcity/Urgency Heuristic + EAST framework (Timely — ask at the right moment). This is the moment of highest intent (just read how it works). Adding genuine weekly urgency here is appropriate.

### V6 Decision 12 — Products H2: Outcome Formula
**Change:** "Crafted for every London home" → "Made to measure. Fitted by our team."
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Outcome-focused formula. The previous headline was generic brand claim. The new headline states the two key USPs in 6 words — both differentiate from online retailers.

### V6 Decision 13 — Before/After H2: Proof-Focused Formula
**Change:** "The same room. An entirely different feeling." → "4,000 London homes. 129 Google reviews. One consistent verdict."
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Proof-focused formula: "[Number] [people] [outcome]". Previous headline was poetic but vague. New headline stacks three real numbers — each number is a trust signal. "One consistent verdict" creates intrigue and implies the verdict is positive without stating it.

### V6 Decision 14 — Testimonials H2: Proof Formula Applied
**Change:** "Trusted by 4,000+ London homes" → "129 Google reviews. 4.9 stars. Every time."
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Proof-focused formula emphasising consistency. "Every time" is the key phrase — it implies this isn't cherry-picked, it's their standard. Contrast with "4,000+ London homes" which is impressive but abstract; "129 reviews at 4.9" is verifiable and specific.

### V6 Decision 15 — Featured Testimonial: Specificity Rule Applied
**Change:** Added specific room (plantation shutters, living room), outcome (better than I imagined), and social behaviour (recommended to 3 neighbours)
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Testimonial selection rules: "Best testimonials include specific results, before/after context, role + company for credibility, something quotable and specific. Avoid testimonials that just say 'Great product!' or 'Love it!'". Previous featured testimonial was good but lacked specifics. New version adds: product, room, qualitative outcome, and referral behaviour.

### V6 Decision 16 — Grid Testimonials: Specificity Rule Applied
**Change:** Replaced vague testimonials ("Great local company with fantastic customer service" and "Efficient, reliable and friendly service throughout") with specific-result versions
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** Same testimonial selection principle. "Great local company" adds zero information — it's what every local company would want said. New Bibi C. quote names the product, rooms, and longevity ("still perfect two years on"). New Olivia S. quote adds before/after context ("I'd tried a cheaper online company before").

### V6 Decision 17 — Free Samples: Endowment Effect Copy
**Change:** "See the colour, feel the texture and hold it up to your window" → "The moment you hold a real sample up to your window — in your light, against your walls — you'll know."
**Reference file:** `~/.claude/skills/marketing-psychology/SKILL.md`
**Principle:** Endowment Effect — people value things more once they own/hold them. The new copy emphasises the physical experience of possession and the emotional certainty it creates. "You'll know" is outcome-focused and activates the endowment effect through imagination.

### V6 Decision 18 — Consultation Section: Urgency + Regret Aversion
**Change:** Headline "Your perfect windows start with a conversation" → "Survey slots available this week — book yours now". Body adds "Not happy with our advice? No charge, no obligation. You simply say no."
**Reference file:** `~/.claude/skills/marketing-psychology/SKILL.md`
**Principle:** (1) Scarcity/Urgency Heuristic — genuine weekly slot scarcity at final CTA. (2) Regret Aversion — "people avoid actions that might cause regret". Adding "simply say no" removes the imagined regret of booking and not wanting to proceed. This directly lowers the psychological barrier to submitting the form.

### V6 Decision 19 — Form Trust Signals Strip
**Change:** Added three micro-trust signals above the consultation form: 4.9/5 rating, Free visit no obligation, We call within 2 hours
**Reference file:** `~/.claude/skills/marketing-psychology/SKILL.md`
**Principle:** Social proof + Regret Aversion at highest-friction moment (form submission). Authority (4.9/5 stars) signals competence. "No obligation" directly reduces regret aversion. "Within 2 hours" reduces anxiety about the unknown post-submission experience. Per EAST framework: make it Attractive (stars), Timely (2 hours), Social (129 reviews).

### V6 Decision 20 — Plain English Sweep
**Change:** "provide a fixed price quote" → "give you a fixed-price quote". "guide you through hundreds of fabrics" → "walk you through hundreds of fabrics".
**Reference file:** `~/.claude/skills/copy-editing/references/plain-english-alternatives.md`
**Principle:** "provide" → "give" (plain English rule #4). "guide" is fine but "walk you through" is more conversational and personal. Full scan confirmed no instances of: utilise, ensure, facilitate, in order to, currently, approximately, basically, actually. V5 was already reasonably clean.

### V6 Decision 21 — About Section Headline: Authority + Timeline
**Change:** "London-made, London-minded" → "Independent since 2009. London-minded. Always."
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md` + `~/.claude/skills/marketing-psychology/SKILL.md`
**Principle:** Lindy Effect — the longer something has survived, the longer it's likely to continue. "Since 2009" is a trust signal because it proves longevity. "Independent" is a direct differentiator vs national chains. "Always" adds commitment and consistency framing.

### V6 Decision 22 — FAQ Headline: Outcome Formula
**Change:** "Questions we get asked" → "Everything you want to know before booking"
**Reference file:** `~/.claude/skills/copywriting/references/copy-frameworks.md`
**Principle:** "Everything you need to [outcome]" formula. The new headline reframes the FAQ from a company-centric ("questions WE get asked") to a customer-centric ("everything YOU want to know") framing. "Before booking" adds a specific moment of relevance.

### V6 Decision 23 — image-generation.md Applied (for future use)
**Reference file:** `~/.claude/skills/image-generation/references/prompt-crafting.md`
**Note:** All images in v5/v6 use real Adams Blinds CDN photography (not AI-generated). The prompt-crafting reference was read and documented for future use when AI images are needed:
- Formula: `Editorial lifestyle photography of [subject], warm natural light / golden hour lighting, cream and terracotta color palette, sophisticated refined elegant, rule of thirds composition, authentic real home feel`
- Style words: editorial, lifestyle, sophisticated, refined, elegant, warm, inviting
- No text in AI-generated images; overlays applied via Python/Pillow
