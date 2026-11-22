"""
类：
用来定义一类事物的“图纸”，后续依照类的“模板”来创建相应的对象。较为抽象的存在
对象：
根据类内部的定义，所得到的实际数据，同时能够使用运行类内部的方法。是实际的内容
继承：
使用父类中的信息，在子类的更新中减少工作量，同时可以添加新的内容。描述类与类之间的关系

方法重写：在子类方法名与父类方法名相同时，子类重新定义该方法的内容。
super()：调用父类中被方法重写覆盖的内容
"""
# 1
"""
num_str = input("请输入整数数组（用空格分隔）：")
target = int(input("请输入target："))
num_list = num_str.split()
nums = []
for i in num_list:
    nums.append(int(i))
num = []
for x in range(len(nums)):
    for y in range(x+1,len(nums)):
        if nums[x] + nums[y] == target:
            nums = [x,y]
            break
    if num:
        break
print(nums)
"""
# 2
# num_str= input("请输入一个数组（请用空格分隔）：")
# num_list = num_str.split()
# count = 0
# for x in range(len(num_list)):
#     if num_list[x] == "0":
#         num_list.remove("0")
#         count += 1
#
# for y in range(count):
#         num_list.append("0")
# 不能字与数比较
# 正着删除会导致顺序错误，要倒着删

"""
num_str= input("请输入一个数组（请用空格分隔）：")
num_list = num_str.split()
num_int = []
for i in num_list:
    num_int.append(int(i))
count = 0
for x in range(len(num_int)-1,-1,-1):  # 从最后一位开始倒数，一直到第0位（终点2应设为0-1即-1）
    if num_int[x] == 0:
        num_int.remove(0)
        count += 1
for y in range(count):
    num_int.append(0)

print(num_int)
"""
"""
# 3
n =input("请输入元素数量：")
num_str = input("请输入数组（用空格分隔）：")
num_list = num_str.split()
num_int = []
for i in num_list:
    num_int.append(int(i))
print("排序前：",num_str)
def my_sort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
last_list = my_sort(num_int)
print(f"排序后",*last_list)
"""
"""
# 4  # 指针
def func(a):
    set_1 = set()
    left = 0
    length_max = 0
    for right in range(len(a)):
        set_2 = a[right]
        while set_2 in set_1:     # 如果新字符在原来的set_1中，需要去掉左边重复的部分
            set_1.remove(a[left])   # 去掉左侧重复的部分
            left += 1
        set_1.add(set_2)
        length = right - left + 1  # 计算长度
        length_max = max(length_max, length) # 更新长度
    return length_max
print(func("pwwkew"))
"""
"""
# 5
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    step_2 = 1   # 前两阶
    step_1 = 2   # 前一阶
    for i in range(3,n+1):
        now = step_1 + step_2  # 从第3阶开始计算
        
        step_2 = step_1      # 到第4阶，前两阶为第3阶的前一阶
        step_1 = now
    return step_1
print(func(5))
"""
"""
# 6
d = int(input("请输入传播距离："))
n = int(input("请输入公共场所数量："))


两个数组，一个记录公共场所坐标，一个记录公共场所数量
用循环把129*129个路口全部计算一遍，根据发射器的坐标与公共场所坐标的距离，进行判断
根据要求比出最优解
"""

# 7
