from PIL import Image

img = Image.open('cat2.jpg')
g = Image.new('RGB', (256, 100), (255, 255, 255))

w = img.width
h = img.height

gist = [0] * 256

for x in range(w):
    for y in range(h):
        pixel = img.getpixel((x, y))
        br = sum(pixel) // 3
        gist[br] += 1

mx = max(gist)
for x in range(256):
    for y in range(100):
        if 100 - y < gist[x] * 100 // mx:
            g.putpixel((x, y), (0, 0, 0))
g.show()