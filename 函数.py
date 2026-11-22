"""
定义函数
变量（全局）
def 函数名（传入参数）：
    函数体 变量（局部）  global 变量（在函数内部声明该变量为全局变量）
    return 返回值


if判断时，None等同于False
"""
str1 = "Luffy"
str2 = "ONE_PIECE"
str3 = "python"
def my_len(data):
    """
    说明文档
    :param data:
    :return:
    """
    num = 0
    for i in data:
        num += 1
    print(f"字符串{data}的长度是{num}")

my_len(str1)
my_len(str2)
my_len(str3)


# 匿名函数
# lambda 传入参数:函数体    （函数体只能写一行）

def text_func(computer):
    result = computer(1,2)
    print(result)

text_func(lambda a,b: a+b)