def backPack(a, v, m):
    """
    计算可以装入背包的最大价值。
    :param a: 每种物品的体积数组。
    :param v: 每种物品的价值数组。
    :param m: 背包的容量。
    :return: 最大价值。
    """
    n = len(a)  # 获取物品种类数
    dp = [0] * (m + 1)  # 初始化动态规划数组，dp[j] 表示容量为j时的最大价值
    
    # 遍历每种物品
    for i in range(n):
        # 遍历背包的每个可能容量
        for w in range(a[i], m + 1):  # 从当前物品体积到背包容量
            # 更新最大价值，考虑是否加入当前物品
            dp[w] = max(dp[w], dp[w - a[i]] + v[i])
    
    return dp[m]

# 测试用例
print("物品的重量是:[2, 3, 5, 7]")
print("物品的价值是:[1, 5, 2, 4]")
print("背包的容量是:10")
print(f"背包能够装入的最大价值是:{backPack([2, 3, 5, 7], [1, 5, 2, 4], 10)}")
print("-------------------------------------------")
print("物品的重量是:[1, 2, 3]")
print("物品的价值是:[1, 2, 3]")
print("背包的容量是:5")
print(f"背包能够装入的最大价值是:{backPack([1, 2, 3], [1, 2, 3], 5)}")