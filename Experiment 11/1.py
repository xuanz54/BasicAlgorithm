def numberDecoding(s):
    """
    计算解码方法的总数。
    :param s: 只含数字的非空字符串。
    :return: 解码方法的总数。
    """
    n = len(s)
    if n == 0 or s[0] == '0':  # 处理空字符串或以0开头的情况
        return 0
    
    dp = [0] * (n + 1)
    dp[0] = 1  # 空字符串有一种解码方式
    dp[1] = 1  # 单字符有一种解码方式
    
    for i in range(2, n + 1):
        # 如果前一个字符不是'0'，可以考虑只解码一个字符
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        # 如果当前字符和前一个字符组成的两位数小于等于26，可以考虑解码两个字符
        if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
            dp[i] += dp[i - 2]
    
    return dp[n]

# 测试用例
print("请输入一个字符串:12")
print(f"解码方法的数量是:{numberDecoding('12')}")
print("请输入一个字符串:226")
print(f"解码方法的数量是:{numberDecoding('226')}")
print("请输入一个字符串:06")
print(f"解码方法的数量是:{numberDecoding('06')}")