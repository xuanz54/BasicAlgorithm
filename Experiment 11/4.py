def print_matrix(matrix):
    """
    格式化打印二维矩阵。
    """
    for row in matrix:
        print(' '.join(row))

def maxKilledEnemies(grid):
    """
    计算可以用一个炸弹杀死的最大敌人数。
    :param grid: 二维矩阵，包含 'W', 'E', '0'
    :return: 可以用一个炸弹杀死的最大敌人数
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    max_killed = 0
    
    for i in range(rows):
        for j in range(cols):
            # 只在空地放炸弹
            if grid[i][j] == '0':
                # 计算当前位置可以杀死的敌人数
                current_killed = 0
            
                left_j = j
                while left_j >= 0 and grid[i][left_j] != 'W':
                    if grid[i][left_j] == 'E':
                        current_killed += 1
                    left_j -= 1
                
                right_j = j
                while right_j < cols and grid[i][right_j] != 'W':
                    if grid[i][right_j] == 'E':
                        current_killed += 1
                    right_j += 1
                
                up_i = i
                while up_i >= 0 and grid[up_i][j] != 'W':
                    if grid[up_i][j] == 'E':
                        current_killed += 1
                    up_i -= 1

                down_i = i
                while down_i < rows and grid[down_i][j] != 'W':
                    if grid[down_i][j] == 'E':
                        current_killed += 1
                    down_i += 1
                
                max_killed = max(max_killed, current_killed) # 更新最大杀死敌人数
    
    return max_killed

# 测试用例
grid1 = [
    ["0", "E", "0", "0"],
    ["E", "0", "W", "E"],
    ["0", "E", "0", "0"]
]
print_matrix(grid1)
print("最大杀死敌人数:", maxKilledEnemies(grid1)) 

grid2 = [
    ["0", "E", "0", "0"],
    ["E", "E", "W", "E"],
    ["0", "E", "0", "0"]
]
print_matrix(grid2)
print("最大杀死敌人数:", maxKilledEnemies(grid2))  