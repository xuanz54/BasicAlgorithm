def share_apple(m: int, n: int) -> int:
    """
    计算将 m 个苹果放入 n 个盘子里的不同分法
    :param m: 苹果数量
    :param n: 盘子数量
    :return: 不同分法数量
    """
    # 处理边界情况，如果苹果数量为0或者盘子数量为1，返回1
    if m == 0 or n == 1:
        return 1
    # 如果盘子数量大于苹果数量，递归调用以修正盘子数量
    if n > m:
        return share_apple(m, m)
    else:
        # 递归计算不同分法数量
        return share_apple(m, n - 1) + share_apple(m - n, n)
 
# 测试用例
m=int(input("请输入苹果数m="))
n=int(input("请输入盘子数n="))
print(f"{m}个苹果{n}个盘子的分法有{share_apple(m,n)}种")