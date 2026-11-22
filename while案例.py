import random
num = random.randint(1,100)
flag = True
count = 0
while flag:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:

        print(f"恭喜你猜对了！该数字就是{num}")
        print(f"你猜了{count}次")
        flag = False
    else:
        if guess_num < num:
            print("猜小了，再猜一次")
        else:
            print("猜大了，再猜一次")
