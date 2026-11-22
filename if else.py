print("欢迎来到游乐场，儿童免费，成人收费。")
age = input("请输入你的年龄：")
if int(age) >= 18:
    print("您已成年，请补票10元")
else:
    print("您未成年，可以免费游玩。")
print("祝您游玩愉快")