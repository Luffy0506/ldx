import os

print("当前工作目录:", os.getcwd())

if os.path.exists("bill.txt"):
    size = os.path.getsize("bill.txt")
    print(f"找到 bill.txt 文件了！文件大小是: {size} 字节")
    if size == 0:
        print("🚨 破案了：文件大小是 0 字节，它真的是一个空文件！里面的字没保存进去！")
    else:
        print("文件里有内容！开始尝试读取...")
        with open("bill.txt", 'r', encoding='utf-8') as fr:
            for line in fr:
                print("读到了：", line.strip())
else:
    print("🚨 破案了：当前目录下根本找不到 bill.txt 文件！名字写错了！")