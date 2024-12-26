def solveSudoku(board: list) -> None:
    """
    解决数独问题。
    :param board: 9x9的数独棋盘，空白单元用0表示。
    """
    def is_valid(row, col, num):
        """
        检查在指定位置放置数字是否有效。
        :param row: 行索引。
        :param col: 列索引。
        :param num: 要放置的数字。
        :return: 如果有效返回True，否则返回False。
        """
        # 检查行
        for x in range(9):
            if board[row][x] == num:
                return False
        # 检查列
        for x in range(9):
            if board[x][col] == num:
                return False
        # 检查3x3子网格
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def backtrack():
        """
        使用回溯法尝试填充数独。
        :return: 如果找到解决方案返回True，否则返回False。
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = 0
                    return False
        return True

    backtrack()

# 测试用例
sudoku_board = [
    [0,0,9,7,4,8,0,0,0],
    [7,0,0,0,0,0,0,0,0],
    [0,2,0,1,0,9,0,0,0],
    [0,0,7,0,0,0,2,4,0],
    [0,6,4,0,1,0,5,9,0],
    [0,9,8,0,0,0,3,0,0],
    [0,0,0,8,0,3,0,2,0],
    [0,0,0,0,0,0,0,0,6],
    [0,0,0,2,7,5,9,0,0]
]
solveSudoku(sudoku_board)
# 打印解决后的数独
for row in sudoku_board:
    print(row)