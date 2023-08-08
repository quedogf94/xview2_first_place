from PIL import Image

image_paths = ['./input/1.png', './input/2.png']

for path in image_paths:
    image = Image.open(path)
    print(f"Image at {path}:")
    print(f" - Size: {image.size}")
    print(f" - Mode: {image.mode}\n")
