list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
num = 0
while num < len(list1):
    if list1[num] % 2 == 0:
        list2.append(list1[num])
    num += 1
print(list2)


list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(i)
print(list2)


# 集合

my_list = ["黑马","播客","黑马","播客","heima","cast","heima","cast","best"]
set1 = set()
for i in my_list:
    set1.add(i)
print(set1)