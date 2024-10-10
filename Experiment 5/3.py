def totalMoney(n):
    """
    计算在第n天结束时总共存了多少钱，时间复杂度和空间复杂度均为O(1)。
    :param n: 天数
    :return: 总存款
    """
    weeks = n // 7
    remaining_days = n % 7
    
    # 计算完整周的总和
    full_weeks_sum = 28 * weeks + 7 * (weeks * (weeks - 1) // 2)
    # 计算剩余天数的总和
    remaining_days_sum = (remaining_days * (remaining_days + 1) // 2) + (weeks * remaining_days)

    return full_weeks_sum + remaining_days_sum

# 测试用例
n1=int(input("请输入天数n="))
print(f"第{n1}天后一共攒下{totalMoney(n1)}元")
n2=int(input("请输入天数n="))
print(f"第{n2}天后一共攒下{totalMoney(n2)}元")
n3=int(input("请输入天数n="))
print(f"第{n3}天后一共攒下{totalMoney(n3)}元")