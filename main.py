from PIL import Image

im = Image.open("game.png")
pix = im.load()

print(pix[0,20])

print(im.size)