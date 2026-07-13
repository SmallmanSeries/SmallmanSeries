from PIL import Image

img = Image.open('input.png')

data = img.getdata()
new_data = []

for pixel in data:
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2]==0:
        new_data.append((pixel[0], pixel[1], pixel[2], 0))
    else:
        new_data.append((pixel[0], pixel[1], pixel[2], 255))

img.putdata(new_data)

img.save("output.png")
