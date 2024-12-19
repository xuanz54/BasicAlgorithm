from typing import List

def coinChange(coins: List[int], amount:int)->int:
    """
    计算凑成总金额所需的最少硬币个数。
    :param coins: 硬币面额数组。
    :param amount: 目标金额。
    :return: 最少硬币个数，如果无法凑出则返回-1。
    """
    dp = [float('inf')] * (amount + 1)  # 初始化dp数组，初值设为无穷大
    dp[0] = 0  # 金额为0时不需要硬币
    
    # 对于每个金额，尝试使用每种面额的硬币
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # 如果最终金额仍为无穷大，说明无法凑出
    return dp[amount] if dp[amount] != float('inf') else -1

# 测试用例
print("请输入硬币的币值(以,分隔):1,2,5")
print("请输入总金额:11")
if coinChange([1, 2, 5], 11) == -1:
    print("没有任何一种硬币组合能组成总金额11")
else:
    print(f"最少的换硬币个数:{coinChange([1, 2, 5], 11)}种") 
print("--------------------")

print("请输入硬币的币值(以,分隔):2")
print("请输入总金额:3")
if coinChange([2], 3) == -1:
    print("没有任何一种硬币组合能组成总金额3")
else:
    print(f"最少的换硬币个数:{coinChange([2], 3)}种") 

print("--------------------")
print("请输入硬币的币值(以,分隔):1")
print("请输入总金额:0")
if coinChange([1], 0) == -1:
    print("没有任何一种硬币组合能组成总金额0")
else:
    print(f"最少的换硬币个数:{coinChange([1], 0)}种") 
