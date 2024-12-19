def wordBreak(s: str, wordSet: set) -> bool:
    """
    判断是否可以利用字典中的单词拼接出字符串s。
    :param s: 需要拼接的字符串。
    :param wordSet: 单词字典。
    :return: 是否可以拼接出s。
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # 空字符串可以由空集拼接
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[n]

# 测试用例
if wordBreak("ynufe", {"ynu", "ufe"}):
    print("ynufe可以由[ynu, ufe]组成")
else:
    print("ynufe不可以由[ynu, ufe]组成")
if wordBreak("astronaut", {"tro", "as", "na", "ut"}):
    print("astronaut可以由[tro, as, na, ut]组成")
else:
    print("astronaut不可以由[tro, as, na, ut]组成")

