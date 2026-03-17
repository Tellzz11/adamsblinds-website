import re

filepath = r"C:\Users\user\OneDrive\Documents\AdamsBlinds\londonblinds_website_v1.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

def replace_line(lines, lineno, old, new):
    idx = lineno - 1
    if old in lines[idx]:
        lines[idx] = lines[idx].replace(old, new)
        print(f"  OK L{lineno}: {old[:50]}")
    else:
        print(f"  MISS L{lineno}: {old[:60]}")

# Meta OG/Twitter
replace_line(lines, 16, 'website_upgrade/images/higgsfield/lb_hero.png', 'images/hero-london-shutters.jpg')
replace_line(lines, 28, 'website_upgrade/images/higgsfield/lb_hero.png', 'images/hero-london-shutters.jpg')

# Hero
replace_line(lines, 1849, 'website_upgrade/images/higgsfield/lb_hero.png', 'images/hero-london-shutters.jpg')
replace_line(lines, 1849, 'alt="Elegant plantation shutters in a London Georgian townhouse living room"',
             'alt="London Victorian living room with white plantation shutters, golden morning light on herringbone oak floor"')

# Bento products
replace_line(lines, 1975, 'website_upgrade/images/higgsfield/lb_prod_shutters.png', 'images/product-plantation-shutters.jpg')
replace_line(lines, 1975, 'alt="White plantation shutters in a bright London living room"',
             'alt="White full-height plantation shutters on London bay window, louvres at 30 degrees, shadow lines on sill"')
replace_line(lines, 1986, 'website_upgrade/images/higgsfield/lb_prod_roller.png', 'images/product-roller-blinds.jpg')
replace_line(lines, 1986, 'alt="Clean roller blind in a minimalist London flat"',
             'alt="Made-to-measure roller blind in neutral linen fabric inside a London kitchen window recess"')
replace_line(lines, 1997, 'website_upgrade/images/higgsfield/lb_prod_roman.png', 'images/product-roman-blinds.jpg')
replace_line(lines, 1997, 'alt="Linen Roman blind with soft folds in a London kitchen"',
             'alt="Natural linen Roman blind with crisp horizontal pleats in a London period bedroom"')
replace_line(lines, 2008, 'website_upgrade/images/higgsfield/lb_prod_venetian.png', 'images/product-venetian-blinds.jpg')
replace_line(lines, 2008, 'alt="Aluminium venetian blind in a contemporary London office"',
             'alt="Basswood Venetian blinds in warm oak finish, slats at 45 degrees over a London home office desk"')
replace_line(lines, 2019, 'website_upgrade/images/higgsfield/lb_prod_vertical.png', 'images/product-vertical-blinds.jpg')
replace_line(lines, 2019, 'alt="Vertical blind on a large London patio door"',
             'alt="Floor-to-ceiling vertical blinds in light grey fabric across a wide London patio door"')
replace_line(lines, 2030, 'website_upgrade/images/higgsfield/lb_prod_curtains.png', 'images/product-curtains-drapes.jpg')
replace_line(lines, 2030, 'alt="Bespoke curtains with linen drapes in a London bedroom"',
             'alt="Full-length sage green linen curtains on slim brass pole in London Victorian living room"')

# Shop grid
replace_line(lines, 2057, 'website_upgrade/images/higgsfield/lb_prod_shutters.png', 'images/shop-plantation-shutters.jpg')
replace_line(lines, 2057, 'alt="Plantation shutters available to order online"',
             'alt="Single white plantation shutter panel, 89mm louvres at 45 degrees, clean white window recess"')
replace_line(lines, 2069, 'website_upgrade/images/higgsfield/lb_prod_roller.png', 'images/shop-roller-blinds.jpg')
replace_line(lines, 2069, 'alt="Roller blinds available to order"',
             'alt="Cassette roller blind in warm white fully extended, aluminium cassette headbox visible"')
replace_line(lines, 2081, 'website_upgrade/images/higgsfield/lb_prod_roman.png', 'images/shop-roman-blinds.jpg')
replace_line(lines, 2081, 'alt="Roman blinds available to order"',
             'alt="Roman blind fully raised showing five neat pleats stacked in warm oat linen fabric"')
replace_line(lines, 2093, 'website_upgrade/images/higgsfield/lb_prod_venetian.png', 'images/shop-venetian-blinds.jpg')
replace_line(lines, 2093, 'alt="Venetian blinds available to order"',
             'alt="Close-up of 25mm aluminium Venetian blind slats in brushed silver showing concave profile"')
replace_line(lines, 2105, 'website_upgrade/images/higgsfield/lb_prod_vertical.png', 'images/shop-vertical-blinds.jpg')
replace_line(lines, 2105, 'alt="Vertical blinds available to order"',
             'alt="White PVC vertical blind vanes hanging from headrail, showing depth and even spacing"')
replace_line(lines, 2117, 'website_upgrade/images/higgsfield/lb_prod_curtains.png', 'images/shop-curtains-drapes.jpg')
replace_line(lines, 2117, 'alt="Curtains and drapes available to order"',
             'alt="Pencil pleat curtain heading on brass pole, natural linen in warm stone, shallow depth of field"')

# HIW process
replace_line(lines, 2161, 'website_upgrade/images/higgsfield/lb_hiw_consult.png', 'images/process-consultation.jpg')
replace_line(lines, 2161, 'alt="Adams Blinds consultation — discussing options with a London homeowner"',
             'alt="Blinds specialist showing fabric sample book to homeowner during free London home consultation"')
replace_line(lines, 2174, 'website_upgrade/images/higgsfield/lb_hiw_measure.png', 'images/process-measuring.jpg')
replace_line(lines, 2174, 'alt="Professional window measuring at a London home"',
             'alt="Specialist hands measuring Victorian sash window recess with tape measure, notepad on sill"')
replace_line(lines, 2187, 'website_upgrade/images/higgsfield/lb_hiw_install.png', 'images/process-fitting.jpg')
replace_line(lines, 2187, 'alt="Professional blind fitting in a London home"',
             'alt="Blinds specialist fitting plantation shutters with cordless drill in London Victorian window recess"')

# About
replace_line(lines, 2267, 'website_upgrade/images/higgsfield/lb_about.png', 'images/about-portrait.jpg')
replace_line(lines, 2267, 'alt="Adams Blinds specialist consulting with a London homeowner about window treatments"',
             'alt="Adams Blinds specialist smiling, white plantation shutters softly blurred behind him"')

content2 = '\n'.join(lines)

# Modal JS productData image paths
modal_map = [
    ("website_upgrade/images/higgsfield/lb_prod_shutters.png", "images/product-plantation-shutters.jpg"),
    ("website_upgrade/images/higgsfield/lb_prod_roller.png", "images/product-roller-blinds.jpg"),
    ("website_upgrade/images/higgsfield/lb_prod_roman.png", "images/product-roman-blinds.jpg"),
    ("website_upgrade/images/higgsfield/lb_prod_venetian.png", "images/product-venetian-blinds.jpg"),
    ("website_upgrade/images/higgsfield/lb_prod_vertical.png", "images/product-vertical-blinds.jpg"),
    ("website_upgrade/images/higgsfield/lb_prod_curtains.png", "images/product-curtains-drapes.jpg"),
    # catch any remaining
    ("website_upgrade/images/higgsfield/lb_hero.png", "images/hero-london-shutters.jpg"),
    ("website_upgrade/images/higgsfield/lb_about.png", "images/about-portrait.jpg"),
    ("website_upgrade/images/higgsfield/lb_hiw_consult.png", "images/process-consultation.jpg"),
    ("website_upgrade/images/higgsfield/lb_hiw_measure.png", "images/process-measuring.jpg"),
    ("website_upgrade/images/higgsfield/lb_hiw_install.png", "images/process-fitting.jpg"),
]
for old, new in modal_map:
    count = content2.count(old)
    if count:
        content2 = content2.replace(old, new)
        print(f"  OK global: {old[:45]} ({count} replaced)")

# Reviews section background
old_rev = 'class="reviews-section">'
new_rev = 'class="reviews-section" style="background-image:url(\'images/reviews-background.jpg\');background-size:cover;background-position:center;">'
if old_rev in content2:
    content2 = content2.replace(old_rev, new_rev, 1)
    print("  OK: reviews background added")

# Add fabric-samples image in samples section (before the CSS swatches)
old_swatch = '<div class="samples-track">'
new_swatch = '''<div class="samples-photo" style="flex:1;min-width:280px;border-radius:8px;overflow:hidden;max-height:320px;">
      <img src="images/fabric-samples.jpg" alt="Fabric swatches fan arrangement including linen cream, sage green, terracotta, charcoal and warm sand on oak table" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div class="samples-track" style="display:none;">'''
if old_swatch in content2:
    content2 = content2.replace(old_swatch, new_swatch, 1)
    print("  OK: fabric-samples image added to samples section")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content2)

# Verify
remaining = content2.count('website_upgrade/images/higgsfield')
print(f"\nRemaining old paths: {remaining}")
print("Done.")
