import os

#初始化
print("输入世界region目录和r.x.z.mca文件x,z坐标的起始数字，将区域转换到指定坐标")
mulu=str(input("转换目录："))
print("转换前")
a=int(input("region起始数字（x）："))
b=int(input("region起始数字（z）："))
print("转换后")
c=int(input("region起始数字（x）："))
d=int(input("region起始数字（z）："))
i=a
j=b

print("转换开始！")

qwe1=1
while qwe1<=5:
    qwe2=0
    while qwe2<=5:
        if os.path.exists(os.path.join(mulu,"r."+str(i)+"."+str(j)+".mca")):
            os.rename(os.path.join(mulu,"r."+str(i)+"."+str(j)+".mca"),os.path.join(mulu,"r."+str(i-a+c)+"."+str(j-b+d)+".mca"))
            print("已转换：r."+str(i)+"."+str(j)+".mca -> r."+str(i-a+c)+"."+str(j-b+d)+".mca")
            qwe1=1
            qwe2=1
        else:
            print("未找到：r."+str(i)+"."+str(j)+".mca，已跳过（已尝试",str(qwe1)+"/5,",str(qwe2)+"/5次）")
            qwe2 = qwe2+1
        j=j+1
    qwe1=qwe1+1
    i=i+1
    j=b

print("转换完成！")
