def BuyBurger(n:int, m:int)->list[int]:
    """
    计算最多能购买的汉堡数量及总费用。
    """
    t = m // 5  # 5元汉堡个数
    m %= 5  # 剩余的钱
 
    if t * 5 > n:
        # 如果预算不够买 t 个 5 元汉堡，返回最多能买的数量和总费用
        return [n // 5, (n // 5) * 5]
    else:
        n -= t * 5  # 扣除 t 个 5 元汉堡的费用
        if n >= 10 - m:
            # 预算还够买一个 10 元汉堡
            n -= (10 - m)
            # 返回 t + 1 + (n // 10) 个汉堡数量和总费用
            return [t + 1 + (n // 10), t * 5 + 10 - m + (n // 10) * 10]
        else:
            # 预算不够买一个 10 元汉堡，只能买 t 个 5 元汉堡
            return [t, t * 5]
 
# 测试用例
n=int(input("请输入你手头上的钱数："))
m=int(input("请输入一起购买汉堡的朋友数量："))
num, cost = BuyBurger(n, m)
print(f"你能购买的最多的汉堡数量是{num}个")
print(f"购买最多汉堡时最少需要花的钱是{cost}元")