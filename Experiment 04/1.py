def get_row(rowIndex: int) -> list[int]:
    """
    获取杨辉三角的第 rowIndex 行
    :param rowIndex: 非负整数，表示行索引
    :return: 杨辉三角的第 rowIndex 行
    """
    row = [1]  # 初始化第0行
 
    for i in range(rowIndex):
        # 生成新行
        new_row = [1]  # 每行开始为1
        for j in range(1, len(row)):
            new_row.append(row[j - 1] + row[j])  # 当前元素是上方两个元素之和
        new_row.append(1)  # 每行结束为1
        row = new_row  # 更新行
 
    return row
 
# 测试用例
rowIndex=int(input("请输入rowIndex="))
print(get_row(rowIndex))