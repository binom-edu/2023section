from PIL import Image

img = Image.open('catbw.png')

w = img.width
h = img.height

for x in range(w):
    for y in range(h):
        pixel = list(img.getpixel((x, y)))
        if sum(pixel) < 750:
            img.putpixel((x, y), (182, 135, 79))
        
img.save('result.jpg')
        

