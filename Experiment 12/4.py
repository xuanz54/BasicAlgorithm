from typing import List

def mincostTickets(days:List[int], costs:List[int]) -> int:
    """
    计算完成旅行计划的最低票价。
    :param days: 旅行日期数组。
    :param costs: 三种通行证的价格[1天, 7天, 30天]。
    :return: 最低总票价。
    """
    dp = [0] * 366  # 初始化dp数组，记录每天的最小花费
    days_set = set(days)  # 将旅行日期转换为集合，便于查找
    
    # 从第一天开始到最后一个旅行日
    for i in range(1, max(days) + 1):
        if i not in days_set:
            # 如果当天不需要旅行，则费用和前一天相同
            dp[i] = dp[i - 1]
        else:
            # 当天需要旅行，考虑三种购票方案
            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],   
                dp[max(0, i - 7)] + costs[1],   
                dp[max(0, i - 30)] + costs[2]   
            )
    
    return dp[days[-1]]  # 返回最后一个旅行日的最小花费

# 测试用例
print(f"出行日期为[1,4,6,7,8,20],三种有效通行证(1,7,30)价格为[2,7,15],最小开销是{mincostTickets([1,4,6,7,8,20], [2,7,15])}")
print(f"出行日期为[1,2,3,4,5,6,7,8,9,10,30,31],三种有效通行证(1,7,30)价格为[2,7,15],最小开销是{mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])}")
