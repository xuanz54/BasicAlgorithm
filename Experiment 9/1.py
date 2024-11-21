def maxProfit(prices):
    """
    计算最大可能利润。
    :param prices: 股票每天的价格数组。
    :return: 最大总利润。
    """
    total_profit = 0  # 初始化总利润为0
    for i in range(1, len(prices)):  # 从第二天开始遍历
        if prices[i] > prices[i-1]:  # 如果当前天的价格高于前一天
            total_profit += prices[i] - prices[i-1]  # 则加上这两天的差价
    return total_profit  # 返回计算出的总利润

# 测试用例
print("请输入股票的价格序列:7,1,5,3,6,4")
print(f"最大的利润是:{maxProfit([7,1,5,3,6,4])}")
print("请输入股票的价格序列:1,2,3,4,5")
print(f"最大的利润是:{maxProfit([1,2,3,4,5])}")
print("请输入股票的价格序列:7,6,4,3,1")
print(f"最大的利润是:{maxProfit([7,6,4,3,1])}")