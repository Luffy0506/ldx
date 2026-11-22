money = 5000000.00
name = input("请输入您的姓名：")
def check_money():
    print("------------查询余额------------")
    print(f"{name}您好，您的余额为：{money}元")
def save_money():
    print("------------存款------------")
    num = float(input("请输入您存款的金额："))
    global money
    money += num
    print(f"存款{num}元成功，您的余额为{money}元")
def take_money():
    global money
    take = float(input("请输入您要取的金额："))
    money -= take
    if money >= 0:
        print (f"取款{take}元成功，您的余额为{money}元")
    else:
        print("您的余额不足，无法取款")
        money += take
def main():
    print("------------主菜单------------")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
while True:
    main()
    choose = int(input("请输入您的选择："))
    if choose == 1:
        check_money()
        continue
    elif choose == 2:
        save_money()
        continue
    elif choose == 3:
        take_money()
        continue
    else:
        print("退出程序")
        break