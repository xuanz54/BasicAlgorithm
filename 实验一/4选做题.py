def FoldingMatrix(n):
    """
    构造一个n×n的矩阵，按指定的折叠规则从1开始递增填充。
    :param n: int, 矩阵的阶数
    :return: list, 构造出的n×n矩阵
    """
    # 创建一个n×n的矩阵，初始化为0
    a = [[0 for _ in range(n)] for _ in range(n)]
    k = 1  # 初始化起始数为1
    a[0][0] = k  # 左上角置为1
    k += 1
    # 逐步填充矩阵
    for i in range(1, n):
        x, y = 0, i  # 初始化位置，行x从0开始，列y从i开始
        a[x][y] = k  # 填充起始位置
        k += 1
        x += 1  # 移动到下一行
        # 填充对角线向下部分
        for j in range(i):
            a[x][y] = k
            k += 1
            x += 1
        x -= 1  # 回退到最后填充的行
        y -= 1  # 向左移动一列
        # 填充对角线向左部分
        for j in range(i):
            a[x][y] = k
            k += 1
            y -= 1
    return a

def print_matrix(matrix):
    """
    按指定格式打印矩阵。
    :param matrix: list, 需要打印的二维列表矩阵
    """
    for row in matrix:
        for elem in row:
            print(f"{elem:4d}", end="")
        print()  # 换行

# 示例运行
n = int(input("请输入方阵的阶数："))  # 从用户获取方阵阶数
matrix = FoldingMatrix(n)
print_matrix(matrix)
