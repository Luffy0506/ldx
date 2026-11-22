try:
    print("1. 开始尝试读取文件...")
    # 注意这里先尝试 utf-8 编码，如果不行，代码里会提示
    fr = open("bill.txt", 'r', encoding='utf-8')
    print("2. 读取成功！开始准备写入备份文件...")
    fw = open("bill.txt.bak", 'w', encoding='utf-8')

    count = 0
    for line in fr:
        print(f"正在读取: {line}")
        line = line.strip()
        if not line:
            continue

        parts = line.split("，")
        last_word = parts[-1]
        print(f"读取到行: {line} -> 分隔后最后一个词是: [{last_word}]")

        if last_word == "测试":
            print("   -> 命中'测试'，跳过")
            continue

        fw.write(line)
        fw.write("\n")
        count += 1

    fr.close()
    fw.close()
    print(f"处理完成！一共写入了 {count} 行数据。")

except Exception as e:
    print("\n🚨 程序崩溃了！错误原因：")
    print(e)