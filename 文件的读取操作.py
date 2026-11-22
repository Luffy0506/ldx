"""
文件对象 = open(file,mode,encoding)   打开文件获得文件对象（文件路径,运行模式，编译器）运行模式r:只读 w：重写 a：追加

文件对象.read(num)     读取指定长度字节，不指定num读取文件全部

文件对象.readline()      读取一行

文件对象.readlines()    读取全部行，得到列表

for line in 文件对象:      for循环文件行，一次循环得到一行数据

文件对象.close()    关闭文件对象

with open() as f   通过with open语法打开文件，可以自动关闭

write(),写入内容

flush(),刷新内容到硬盘中
"""


# f = open("D:/text.txt",'a',encoding="utf-8")
# f.write("hello world\n")
# f.flush()
# f.close()





fr = open("D:/python/bill.txt",'r',encoding='utf-8')
fw = open("D:/python/bill.txt.bak",'w',encoding='utf-8')
count = 0
for line in fr:
    count += 1
    line = line.strip()
    last_word = line.split("，")[-1]
    print(f"第{count}行内容: {repr(line)}, 截取到的最后一个词: {repr(last_word)}")
    if last_word == "测试":
         continue
    fw.write(line)
    fw.write("\n")
fr.close()
fw.close()