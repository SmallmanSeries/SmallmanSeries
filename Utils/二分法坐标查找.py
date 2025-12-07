top=int(input("最大"))
bot=int(input("最小"))
while True:
    mid=(top+bot)//2
    print(mid)
    inp=input("当前坐标小于目标坐标，输入b，大于目标坐标，输入a")
    if inp=="a":
        top=mid
    elif inp=="b":
        bot=mid
    elif inp=="top":
        print(top)
    elif inp=="bot":
        print(bot)
    else:
        continue
