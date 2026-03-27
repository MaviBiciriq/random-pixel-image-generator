from PIL import Image
import random
import matplotlib.pyplot as plt

# Change resolution here (example: 1000x1000)
width, height = 500, 500

print(f"Generating image: {width}x{height}")

img = Image.new("RGB", (width, height))
pixels = img.load()

for x in range(width):
    for y in range(height):
        pixels[x, y] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

# Save as PNG
img.save("random_image.png", "PNG")
print("Saved as random_image.png")

# Show image
plt.imshow(img)
plt.axis('off')
plt.show()