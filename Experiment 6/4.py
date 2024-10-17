def tictactoe(moves:list[list[int]])->str:
    """
    根据给定的井字棋步数判断比赛结果。
    
    :param moves: 每个玩家的步数列表，形式为[row, col]。
    :return: 返回比赛结果："A", "B", "Draw", 或 "Pending"。
    """
    # 初始化3x3的棋盘
    grid = [[None for _ in range(3)] for _ in range(3)]
    
    # 依次落子
    for i, (row, col) in enumerate(moves):
        player = 'A' if i % 2 == 0 else 'B'
        grid[row][col] = player

    # 定义检查胜利者的函数
    def check_winner(player):
        # 检查行、列和对角线
        for i in range(3):
            if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
                return True
        if all(grid[i][i] == player for i in range(3)) or all(grid[i][2-i] == player for i in range(3)):
            return True
        return False

    # 检查A或B是否胜利
    if check_winner('A'):
        return "A"
    if check_winner('B'):
        return "B"
    # 检查是否平局或未结束
    return "Draw" if len(moves) == 9 else "Pending"

# 测试用例
moves1 = [[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]
moves2 = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
moves3 = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
moves4 = [[0, 0], [1, 0], [2, 1]]
print(f"moves1:{moves1}棋局的结果是：{tictactoe(moves1)}")
print(f"moves2:{moves2}棋局的结果是：{tictactoe(moves2)}")
print(f"moves3:{moves3}棋局的结果是：{tictactoe(moves3)}")
print(f"moves4:{moves4}棋局的结果是：{tictactoe(moves4)}")