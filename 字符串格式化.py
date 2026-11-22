num_ji = 123456
num_tu = 654321
words = "笼中有鸡%s只，兔%s只"%(num_ji,num_tu)
print (words)
num_ji-= 123450
num_tu-= 654320
print (num_ji,num_tu)
words = "笼中有鸡%s只，兔%s只"%(num_ji,num_tu)
print (words)
# %s 内容转为字符串
# %d 内容转为整数
# %f 内容转为浮点数

name = "Luffy"
age = 18
mark = 99.99
message = "我叫%s，今年%d岁，考了%f分"%(name,age,mark)
print(message)

"""
我们可以使用辅助符号"m.n来控制数据的宽度和精度
m，控制宽度，   
要求是数字（很少使用)，设置的宽度小于数字自身，不生效
.n，float为控制小数点精度，int为至少输出n位，不足则补0。要求是数字，会进行小数的四舍五入

示例:
%5d:表示将整数的宽度控制在5位，如数字11，被设置为5d，就会变成:【空格][空格][空格]11，用三个空格补足
宽度。
%5.2f：表示将宽度控制为5，将小数点精度设置为2

小数点和小数部分也算入宽度计算。如，对11.345设置了%7.2f后，结果是：[空格]空格]1.35。2个空格补足宽
度，小数部分限制2位精度后，四舍五入为.35

%.2f：表示不限制宽度，只设置小数点精度为2，如11.345设置%.2f后，结果是11.35
"""
num = 2
words = "数字：%3.2d"%num
print (words)# 宽度为3，不足补空格；输出2位；结果为 02

num = 6.646
words_2 = "数字:%5.2f"%num
print(words_2)

# 快速写法 format
# f"内容{变量}"
# 不做精度控制，不影响类型
name = "Luffy"
age = 18
mark = 99.9999
print(f"我叫{name}，今年{age}岁，考了{mark}分。")

# 表达式进行格式化
print("1*1=%d"%(1*1))
print(f"2*3={2*3}")
print("\"字符串\"在python中的类型名是：%s"%type('字符串'))


# 练习
name = "传智博客"
stock_price = 19.99
stock_code = "003032" # 数字不能以0开头
stock_price_daily_growth_factor = 1.2
growth_days = 7
final_price = stock_price*(stock_price_daily_growth_factor**growth_days)
print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日增长系数是:%.2f,经过%d天的增长后，股价达到了:%.2f"%(stock_price_daily_growth_factor,growth_days,final_price))