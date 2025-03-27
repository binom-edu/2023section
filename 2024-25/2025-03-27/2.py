from PIL import Image

img = Image.open('cat2.jpg')

w = img.width
h = img.height

for x in range(w):
    for y in range(h):
        pixel = list(img.getpixel((x, y)))
        for i in range(3):
            pixel[i] = min(pixel[i] + 60, 255)
            img.putpixel((x, y), tuple(pixel))
img.save('result.jpg')
        

