# height = int(input("请输入您的身高（cm）："))
# vip_level = int(input("请输入您的VIP等级（1-5)："))
# if height < 120:
#     print("身高小于120cm，可以免费游玩")
# elif vip_level > 3:
#     print("VIP等级大于3，可以免费游玩")      # 若if满足则不执行elif。即多条件判断下，条件是互斥的，完成后停止执行
# else:
#     print("不好意思，条件都不满足，请补票10元")

# 练习
num = 6
words = "很抱歉，全猜错了，我想的是%d"%num
if int(input("请猜一个数字（1-10）：")) == num:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对了")
elif int(input("不对，最后再猜一次：")) == num:
    print("恭喜你猜对了")
else:
    print (words)
