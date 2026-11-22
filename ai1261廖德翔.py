# 1
a = 15
b = 4
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a//b=",a//b)
print("a%b=",a%b)

# 2
num = int(input("请输入一个整数："))
if num > 0:
    print("该数字为正数")
elif num < 0:
    print("该数字为负数")
else:
    print("该数字为0")

# 3
sum = 0
for i in range(1,21):
    if i % 2 == 0:
        sum += i
print("1到20所有偶数的和为",sum)

# 4
nums = [12,7,25,3,18]
list_max = max(nums)
list_min = min(nums)
nums.sort()
print("该列表的长度为",len(nums))
print(f"该列表的最大值为{list_max},最小值为{list_min}")
print(f"从小到大排序的结果是{nums}")

# 5
student = {
    "name": "张三",
    "age": 19,
    "major": "计算机科学与技术",
    "scores": [85, 92, 78],
}
print("该学生的姓名是:",student["name"],"，专业为:",student["major"])
print("最高分为",student["scores"][1])
student["email"] = "zhangsan@example.com"
print("遍历输出：")
for key,value in student.items():
    print(key,value)

# 6
sids = ["2023CS01045", "2022EE02137", "2023CS01088", "2021MA03021"]
year = sids[0][:4]
print(f"第一个学号入学年份为{year}")
num = sids[0][4:6]
print(f"专业代码为{num}")
sids_class = sids[0][6:]
print(f"班级序号为{sids_class}")
for i in sids:
    if i[:4] == 2023:
        sum += 1
print(f"2023年入学的个数为{sum}")

# 7
for n in range(19,191):
    if n < n+1 :
        pass
    else:
        print("n不满足19<n<190时严格单调递增")
print("n满足19<n<190时严格单调递增")

# 8
def stats(scores)->dict:
    count = scores.count
    avg = count(scores)/len(scores)
    num = 0
    for i in scores:
        if i>60:
            num += 1
    pass_rate = num/len(scores)
    return {"count":count,"avg":avg,"pass_rate":pass_rate}
my_list = [85,92,58,71,63]
