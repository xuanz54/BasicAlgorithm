import os

def print_matrix(matrix):
    """
    格式化打印二维01矩阵。
    """
    os.linesep = '\n'  # 设置打印时的行分隔符为换行符
    for row in matrix:
        print(' '.join(map(str, row)))

def maxSquare(matrix):
    """
    找到全为1的最大正方形的面积。
    """
    if not matrix or not matrix[0]:  # 检查矩阵是否为空
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]  # 初始化动态规划数组
    max_side = 0  # 记录最大正方形的边长
    
    # 遍历矩阵中的每个元素
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side ** 2

# 测试用例
matrix1 = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print_matrix(matrix1)
print(f"最大的正方形面积是{maxSquare(matrix1)}") 

matrix2 = [
    [0, 0, 0],
    [1, 1, 1]
]
print_matrix(matrix2)
print(f"最大的正方形面积是{maxSquare(matrix2)}") 