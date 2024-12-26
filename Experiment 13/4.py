def restoreIpAddresses(s: str) -> list:
    """
    复原IP地址。
    :param s: 只包含数字的字符串。
    :return: 所有可能的有效IP地址列表。
    """
    result = []
    path = []

    def backtrack(start, dots):
        """
        使用回溯法尝试在字符串的不同位置插入点'.'。
        :param start: 当前递归的起始索引。
        :param dots: 当前已经插入的点的数量。
        """
        if dots == 4:
            if start == len(s):
                # 如果已经插入4个点，并且字符串已经遍历完，则添加当前IP地址到结果中
                ip = '.'.join(path)
                result.append(ip)
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if is_valid(segment):
                # 如果当前段有效，则继续递归
                path.append(segment)
                backtrack(end, dots + 1)
                path.pop()

    def is_valid(segment):
        """
        检查当前段是否为有效的IP地址段。
        :param segment: 当前段。
        :return: 如果有效返回True，否则返回False。
        """
        if len(segment) > 1 and segment[0] == '0':
            return False
        if int(segment) > 255:
            return False
        return True

    backtrack(0, 0)
    return result

# 测试用例
s1 = "25525511135"
print(f"有效的ip地址:{restoreIpAddresses(s1)}") 

s2 = "0000"
print(f"有效的ip地址:{restoreIpAddresses(s2)}") 

s3 = "101023"
print(f"有效的ip地址:{restoreIpAddresses(s3)}") 