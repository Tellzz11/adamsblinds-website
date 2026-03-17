filepath = r"C:\Users\user\OneDrive\Documents\AdamsBlinds\londonblinds_website_v1.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Roller blind card - replace img with video
    (
        '          <img src="images/product-roller-blinds.jpg" alt="Made-to-measure roller blind in neutral linen fabric inside a London kitchen window recess" loading="lazy">',
        '''          <video autoplay muted loop playsinline poster="images/product-roller-blinds.jpg" aria-label="Roller blind smoothly rolling down a London kitchen window" style="width:100%;height:100%;object-fit:cover;display:block;">
            <source src="images/anim-roller.mp4" type="video/mp4">
            <img src="images/product-roller-blinds.jpg" alt="Made-to-measure roller blind in neutral linen fabric inside a London kitchen window recess">
          </video>'''
    ),
    # Roman blind card - replace img with video
    (
        '          <img src="images/product-roman-blinds.jpg" alt="Natural linen Roman blind with crisp horizontal pleats in a London period bedroom" loading="lazy">',
        '''          <video autoplay muted loop playsinline poster="images/product-roman-blinds.jpg" aria-label="Roman blind elegantly unfolding downward in a London bedroom" style="width:100%;height:100%;object-fit:cover;display:block;">
            <source src="images/anim-roman.mp4" type="video/mp4">
            <img src="images/product-roman-blinds.jpg" alt="Natural linen Roman blind with crisp horizontal pleats in a London period bedroom">
          </video>'''
    ),
    # Curtains card - replace img with video
    (
        '          <img src="images/product-curtains-drapes.jpg" alt="Full-length sage green linen curtains on slim brass pole in London Victorian living room" loading="lazy">',
        '''          <video autoplay muted loop playsinline poster="images/product-curtains-drapes.jpg" aria-label="Curtains gracefully drawing closed in a London living room" style="width:100%;height:100%;object-fit:cover;display:block;">
            <source src="images/anim-curtains.mp4" type="video/mp4">
            <img src="images/product-curtains-drapes.jpg" alt="Full-length sage green linen curtains on slim brass pole in London Victorian living room">
          </video>'''
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        print(f"  OK: replaced {old[:60]}")
    else:
        print(f"  MISS: {old[:60]}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
print(f"\nVideo tags in file: {content.count('<video ')}")
print(f"anim-roller.mp4: {content.count('anim-roller.mp4')}")
print(f"anim-roman.mp4: {content.count('anim-roman.mp4')}")
print(f"anim-curtains.mp4: {content.count('anim-curtains.mp4')}")
print("Done.")
