# print("* ")
# print("* * ")
# print("*   * ")
# print("*     * ")
# print("* * * * *")
from PIL import Image

# Define dimensions
width, height = 300, 430

# Create a new image with a palette (P mode)
img = Image.new("P", (width, height))

# Define our 3-color palette: [Red, Cream, Blue]
# RGB: Red(255,0,0), Cream(245,245,220), Blue(20,40,80)
palette = [
    255, 0, 0,    # Index 0: Red
    245, 245, 220, # Index 1: Cream
    20, 40, 80     # Index 2: Blue
]
# Fill the rest of the 256-color palette with zeros
palette += [0] * (768 - len(palette))
img.putpalette(palette)

# Simple pattern generation
for y in range(height):
    for x in range(width):
        if y < 120: # Top section
            color = 1 if (x + y) % 40 > 10 else 2
        elif y < 350: # Middle section
            # Diamond/Honeycomb pattern for Red section
            color = 0 if (x % 20 < 15 and y % 20 < 15) else 2
        else: # Bottom section
            color = 1 if (y % 30 < 20) else 2

    img.putpixel((x, y), color)

# Save as BMP
img.save("cardigan_pattern.bmp")
