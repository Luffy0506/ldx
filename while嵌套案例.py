# i = 1
# # j = 0 不可以在这里，否则只有第一天输出送花朵数
# while i <= 100:
#     print(f"每天给小美送花，今天是第{i}天")
#     j = 1   # 重置变量j
#     while j <= 10:
#         print(f"给小美送了{j}朵花")
#         j += 1
#     i += 1
# print(f"坚持了{i - 1}天，小美同意了我的表白。")



# print语句在""后加上  ,end=''则不会换行
# print("123",end='')
# print("456",end='')
# 结果为123456


# \t可以让多行字符串进行对齐  print()为换行
# print("Hello",end='')
# print("World")
# print("Hello World")
# print("Good morning")
# print("Hello\tWorld")
# print("Good\tmorning")




i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}\t",end='')
        j += 1
    i += 1
    print()