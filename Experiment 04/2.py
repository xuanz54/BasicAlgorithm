# 定义一个递归函数来解决骨牌问题
def dominoes_recursion(n: int) -> int:
    """
    使用递归法解决骨牌问题
    :param n: 方格数，表示长方形的长，宽为1
    :return: 骨牌铺法数量
    """
    # 如果方格数为0，表示没有空间放置骨牌，只有一种方式（不放置骨牌）
    if n == 0:
        return 1
    # 如果方格数为1，表示只有一种方式放置一个骨牌
    if n == 1:
        return 1
    # 递归地计算n-1和n-2个方格的铺法数量，并将它们相加
    # 这是因为我们可以在最后一个方格放置一个骨牌，然后考虑剩下的n-1个方格
    # 或者不放置骨牌，然后考虑剩下的n-2个方格
    return dominoes_recursion(n - 1) + dominoes_recursion(n - 2)
 
# 定义一个非递归函数来解决骨牌问题
def dominoes_nonrecursion(n: int) -> int:
    """
    使用非递归法（动态规划）解决骨牌问题
    :param n: 方格数
    :return: 骨牌铺法数量
    """
    # 如果方格数为0或1，直接返回1，因为只有一种铺法
    if n == 0:
        return 1
    if n == 1:
        return 1
    # 初始化一个长度为n+1的列表，用于存储从0到n每个方格数的骨牌铺法数量
    dp = [0] * (n + 1)
    # 已知dp[0]和dp[1]的值都是1
    dp[0], dp[1] = 1, 1
    # 从2开始遍历到n，计算每个方格数的骨牌铺法数量
    # 每个状态的值等于前一个状态的值加上前前一个状态的值
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # 返回n个方格的骨牌铺法数量
    return dp[n]
 
# 测试用例
# 输入方格数并计算两种方法的骨牌铺法数量
n = int(input("请输入长方形方格n="))
# 调用递归函数计算骨牌铺法数量
print(f"使用递归法：{n}个格子骨牌排列的方法为：{dominoes_recursion(n)}")
# 调用非递归函数计算骨牌铺法数量
print(f"使用非递归法：{n}个格子骨牌排列的方法为：{dominoes_nonrecursion(n)}")