import turtle#加载turtle函数。
import datetime#加载datetime函数。
import random#加载rabdon函数。
GouYun=random.randint(0,100)#获取0-100随机数，并使GouYun变量等于获取随机数。
print("此次Python测得您的幸运值为：",GouYun)#打印"此次Python测得您的幸运值为："和GouYun变量。
if GouYun <= 10:#如果GouYun<= 10。
    print("fvv,咋那么差👎，√8东西，滚吧！")#打印"fvv,咋那么差👎，√8东西，滚吧！"
    turtle.done()#程序退出。
elif GouYun <= 50 and GouYun >= 11:#如果GouYun<= 50。且#如果GouYun>= 11。
    print("劳弟，还是没实力。")#打印"劳弟，还是没实力。"
    turtle.done()#程序退出。
elif GouYun <= 90 and GouYun >= 51:#如果GouYun<= 90。且#如果GouYun>= 70。
    print("woc，有实力的。")#打印"woc，有实力的。"
else:#那么。
    print("666这个入是桂！")#打印"666这个入是桂！"
name = input("自己的名字，快输入sb！")#输入自己的名字。
if name != "sb":#如果名字≠“sb”。
    print("Fuck,you!")#打印"Fuck you!"
    print("F","u","c","k",",","y","o","u","!")#打印"Fuck you!"
    turtle.done()#程序退出。
else:#如果名字=“sb”。
    TimeNow = datetime.datetime.now()#获取当前时间，并使TimeNow变量等于当前时间。
    if str(TimeNow.strftime("%H")) == 0o00:#判断现在时间是否等于特定时间。
        print("早点睡牢底！")#打印"早点睡牢底"
        turtle.done()#程序退出。
    else:
        print("你过关！")#打印"你过关！"
        turtle.speed(10000)#turtle10000的速度。
        for man in range(100000000000000000000000000000):#循环100000000000000000000000000000次man。
            for kobe in ('blue', 'red', 'green','yellow','black','orange','brown','white'):#Kobe变量变化颜色。
                man=10 + man#man持续+10。
                turtle.color(kobe)#设颜色为Kobe。
                turtle.right(man/10)#设向右转角度为man/10。(135为德国)
                turtle.forward(50)#前进50单位。
                turtle.right(90)#向右转90°。
                turtle.forward(50)#前进50单位。
                turtle.left(180)#向左转180°。
                turtle.forward(50)#前进50单位。
                turtle.left(90)#向左转90°。
                turtle.right(90)#向右转90°。
                turtle.forward(50)#前进50单位。
                turtle.left(180)#向左转180°。
                turtle.forward(50)#前进50单位。
                turtle.left(90)#向左转90°。
                turtle.forward(50)#前进50单位。
                turtle.left(90)#向左转90°。
                turtle.forward(50)#前进50单位。
                turtle.right(90)#向右转90°。
                turtle.forward(50)#前进50单位。
                turtle.left(180)#向左转180°。
                turtle.forward(50) #前进50单位。
                turtle.left(90)#向左转90°。
                turtle.forward(100)#前进100单位。
                turtle.right(90)#向右转90°。
                turtle.forward(50)#前进50单位。
turtle.done()#程序结束。