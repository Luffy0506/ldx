"""
类型转换
"""
# 数字转文字（int\float~str)
bianliang = str(11)
print(type(bianliang),bianliang)
# 小数转整数（舍去小数点）(float~int）
Bianliang = int(2.88)
print(type(Bianliang),Bianliang)
# 整数转小数（加小数点）（int~float)
bl = float(66)
print(type(bl),bl)
# 文字转数字无法转换
BL2 = float("wenzi")
print(type(BL2),BL2)