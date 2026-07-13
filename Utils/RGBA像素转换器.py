from PIL import Image

print("输入图像目录，将所有黑色像素转换成保留RGB信息的透明像素")
file=str(input("图像目录："))

img=Image.open(file)
data=img.getdata()
new_data=[]

for pixel in data:
    if pixel[0]==0 and pixel[1]==0 and pixel[2]==0:
        new_data.append((pixel[0],pixel[1],pixel[2],0))
    else:
        new_data.append((pixel[0],pixel[1],pixel[2],255))

img.putdata(new_data)
img.save("image.png")
print("图像已保存为“image.png”")
