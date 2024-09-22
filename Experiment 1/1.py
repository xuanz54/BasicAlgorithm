def josephus(n, m):
    """
    模拟约瑟夫环问题，确定最后一个不被挂科的学生编号。

    :param n: int, 学生的总数量
    :param m: int, 报到m的学生将被挂科
    :return: int, 最后一个不被挂科的学生编号
    """
    students = list(range(1, n+1))  # 创建学生编号列表
    index = 0  # 初始化报数的起始位置
    while len(students) > 1:  # 当列表中剩余学生多于1人时，继续循环
        index = (index + m - 1) % len(students)  # 计算挂科的学生位置
        students.pop(index)  # 移除挂科学生
    return students[0]  # 返回最后剩下的学生编号

# 示例运行
n=int(input("请输入参与游戏的学生人数: "))
m=int(input("请输入逢m出局的m: "))
print(f"最后没挂科的学生是{josephus(n, m)}号")
