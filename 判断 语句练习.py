import random
num = random.randint(1,10)
# print (num)
guess_num1 = int(input("请输入你猜测的数字："))
if guess_num1 == num:
    print("恭喜你猜对了")

elif guess_num1 > num:
    guess_num2 = int(input("猜错了，数字比它小，请再猜一次："))
    if guess_num2 == num:
        print("恭喜你猜对了")
    elif guess_num2 > num:
        guess_num3 = int(input("猜错了，数字比它小，再猜一次："))
        if guess_num3 == num:
            print("恭喜你猜对了")
        else:
            print(f"很抱歉，你三次都猜错了，数字为{num}")
    elif guess_num2 < num:
        guess_num3 = int(input("猜错了，数字比它大，再猜一次："))
        if guess_num3 == num:
            print("恭喜你猜对了")
        else:
            print(f"很抱歉，你三次都猜错了，数字为{num}")

elif guess_num1 < num:
    guess_num2 = int(input("猜错了，数字比它大，请再猜一次："))
    if guess_num2 == num:
        print("恭喜你猜对了")
    elif guess_num2 > num:
        guess_num3 = int(input("猜错了，数字比它小，再猜一次："))
        if guess_num3 == num:
            print("恭喜你猜对了")
        else:
            print(f"很抱歉，你三次都猜错了，数字为{num}")
    elif guess_num2 < num:
        guess_num3 = int(input("猜错了，数字比它大，再猜一次："))
        if guess_num3 == num:
            print("恭喜你猜对了")
        else:
            print(f"很抱歉，你三次都猜错了，数字为{num}")

