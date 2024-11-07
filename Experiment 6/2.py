def findRepeatedDnaSequences(s: str) -> list[str]:
    """
    返回所有出现不止一次的长度为10的序列，按出现顺序返回。
    :param s: DNA序列的字符串表示。
    :return: 符合条件的子字符串列表，按它们第一次出现的顺序排列。
    """
    seen = set()
    repeated = []
    # 使用窗口遍历长度为10的子串
    for i in range(len(s) - 9):
        substring = s[i:i+10]
        if substring in seen and substring not in repeated:
            repeated.append(substring)
        seen.add(substring)
    return repeated

def formatDnaSequences(sequences: list[str]) -> str:
    """
    将DNA序列列表格式化为不带引号的字符串表示。
    :param sequences: DNA序列列表。
    :return: 格式化后的字符串，形如 [AAAAACCCCC, CCCCCAAAAA]。
    """
    return "[" + ", ".join(sequences) + "]"

# 测试用例
s = str(input("请输入主串S: "))
result = findRepeatedDnaSequences(s)
# 使用新函数打印结果
print(formatDnaSequences(result))