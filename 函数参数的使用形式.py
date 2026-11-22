"""
def user_info(*args):
    print(args)

传进的所有参数都会被args变量接收，它会根据传进参数的位置合并为一个元组（tuple），args是元组类型，这就是位置传递

def user_info(**kwargs):
    print(kwargs)

参数是“键值对”形式的形式的情况下，所有的“键值对”都会被kwargs接收，同时会根据“键=值”组成字典
"""
def user_info(*args):
    print(args)
user_info(1,"aa")
user_info(2)


def user_info(**kwargs):
    print(kwargs)

user_info(name = "Luffy",age = 18,gender = "Male")