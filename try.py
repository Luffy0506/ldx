def conv(image, kernel):
    # 1. 获取输入图像和卷积核的尺寸
    img_h = len(image)
    img_w = len(image[0])
    ker_h = len(kernel)
    ker_w = len(kernel[0])

    # 2. 计算输出特征图的尺寸
    out_h = img_h - ker_h + 1
    out_w = img_w - ker_w + 1

    # 3. 初始化一个空的输出二维列表
    output = []

    # 4. 开始滑动窗口（外层循环遍历输出的行和列）
    for i in range(out_h):
        row_result = []  # 存放这一行的结果
        for j in range(out_w):
            # 每次滑动到一个新位置，初始化总和为0
            total_sum = 0

            # 5. 卷积核与对应区域逐元素相乘并求和
            for m in range(ker_h):
                for n in range(ker_w):
                    # 这里就是你的核心操作：累加乘积
                    # 提示：输入图像的对应位置是 image[i+m][j+n]，核是 kernel[m][n]
                    total_sum += image[i + m][j + n] * kernel[m][n]

            # 将这个位置计算出的总和加入当前行
            row_result.append(total_sum)

        # 将当前行加入最终的输出
        output.append(row_result)

    return output


# 测试你的代码
img = [
    [12, 25, 18, 32, 15],
    [28, 45, 37, 22, 19],
    [14, 33, 50, 41, 27],
    [23, 19, 29, 36, 44],
    [31, 26, 21, 17, 39]
]

ker = [
    [2, -3, 1],
    [-1, 4, -2],
    [3, -1, 2]
]

# 运行看看结果是不是和图片上的完全一致！
print(conv(img, ker))