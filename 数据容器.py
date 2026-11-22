"""
列表方法

1  列表.append(元素）：向列表尾部添加一个元素

2  列表.extend(容器)：将容器中的内容依次取出，添加到列表的尾部

3  列表.insert(下标，元素)：在指定下标处插入指定元素

4  del 列表[下标]：删除列表指定下标元素

5  列表.pop(下标)：删除列表指定下标元素，可用变量接收被删除的元素

6  列表.remove(元素)：从前向后删除此元素第一个匹配项

7  列表.clear()：清空列表

8  列表.count(元素)：统计此元素在列表中出现的次数

9  列表.index(元素):查找指定元素在列表的下标，找不到报错ValueError

10  len(列表)：统计容器内有多少元素

11  sorted(容器)/sorted(容器，[reverse=False])（正序）  sorted(容器，[reverse=Ture])(倒序)  排序，均变为列表

(字符串方法）
12  字符串.replace(字符串1,字符串2)：将字符串内的全部字符串1，替换为字符串2，不是修改字符串本身，而是得到一个新字符串

13  字符串.split(分隔符字符串)：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中

14  字符串.strip()：去前后空格以及换行符  字符串.strip(字符串)：去前后指定字符串

(序列)
切片：序列[起始下标:结束下标:步长]  留空[:]代表从头或到尾，步长默认为1,步长为负数则倒序执行

(集合)
集合.pop()：从集合中随机取出一个元素

集合1.difference(集合2)：取出集合1和集合2的差集（集合1有而集合2没有的）（集合1集合2不变，得到一个新的集合）—

集合1.difference_update(集合2)：在集合1内删除和集合2相同的元素。（集合1被修改，而集合2不变）

集合1.union(集合2)：将集合1和集合2组合成新集合

（集合可以用for循环，不支持while循环）

(字典)
字典[key]=value：字典被修改或更新，新增更新了元素

字典.keys()：得到字典中的全部key，可用于for循环
"""

list1 = [21,25,21,23,22,20]
list1.append(31)
print(list1)

list2 = [29,33,30]
list1.extend(list2)
print(list1)

print(list1[0])

print(list1[-1])

print(list1.index(31))

print(len(list1))

str1 = "itheima and itcast"
print(str1)
str2 = str1.replace("it","程序")
print(str2)

str1 = "hello world python Luffy"
str_list = str1.split(" ")
print(str_list)

str2 = str1.strip()
print(str2)
str1 = "  hello world python Luffy  "
print(str1)
str1 = "12hello world python Luffy21"
print(str1)
str2 = str1.strip("12")
print(str2)

list1 = [1,2,3,4,5,6,7,8,9]
list2 = list1[0:1000]
print (list2)

dict1 = dict()