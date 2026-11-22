# continue 为跳过本次循环。临时中断
# break 为结束这个循环。永久中断
# 二者均可嵌套运用，仅影响内层


money = 10000
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{i}绩效分为{num}，不满足要求")
        continue
    if money >= 1000:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额{money}元")
        if money < 1000:
            print("没钱了，下个月再发")
            break
    else:
        print("没钱了，下个月再发")
        break
