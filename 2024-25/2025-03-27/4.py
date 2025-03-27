from PIL import Image

def f(x):
    return int(-(x - 255) ** 2 / 255 + 255)

img = Image.open('cat2.jpg')

w = img.width
h = img.height

for x in range(w):
    for y in range(h):
        pixel = list(img.getpixel((x, y)))
        for i in range(3):
            pixel[i] = f(pixel[i])
            img.putpixel((x, y), tuple(pixel))
img.save('result.jpg')