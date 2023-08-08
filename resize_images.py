from PIL import Image

image_paths = ['./input/1.png', './input/2.png']

# Open the images
image1 = Image.open(image_paths[0])
image2 = Image.open(image_paths[1])

print(f"Original size of Image 1: {image1.size}")
print(f"Original size of Image 2: {image2.size}")

# Resize image2 to match image1
image2_resized = image2.resize(image1.size)

print(f"Resized size of Image 2: {image2_resized.size}")

# Optionally, save the resized image
image2_resized.save('./input/2_resized.png')

# Optionally, show the images
image1.show()
image2_resized.show()
