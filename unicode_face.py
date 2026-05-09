from PIL import Image
import numpy as np

# Dense Unicode characters for better detail
chars = np.asarray(list('⠀⠁⠃⠇⠏⠟⠿⣿'))

img = Image.open("cat.png").convert("L")

# Resize for detail
width = 200
aspect_ratio = img.height / img.width
height = int(aspect_ratio * width * 0.5)

img = img.resize((width, height))

# Convert to numpy array
pixels = np.array(img)

# Normalize brightness to character range
normalized = (pixels / 255.0) * (len(chars) - 1)
ascii_image = "\n".join(
    "".join(chars[pixel.astype(int)] for pixel in row)
    for row in normalized
)

# Save output
with open("unicode_face.txt", "w", encoding="utf-8") as f:
    f.write(ascii_image)

print("Done! Check unicode_face.txt")