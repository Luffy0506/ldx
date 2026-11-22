"""
while 条件：
    条件满足时，做的事情1
    条件满足时，做的事情2
    条件满足时，做的事情3
    ......

    条件需提供布尔类型结果
"""
# i = 0
# while i < 10:
#     print("Hello")
#     i += 1
# print("Hello,World")



a = 1
sum = 0
while a <= 100:
    a = a + 1      #！
    sum = sum + a  #！
    # sum += a    1   3
    # a +=1       2   4.....
print (sum)
# 2+....100+101=5150
# 漏了1.多了101