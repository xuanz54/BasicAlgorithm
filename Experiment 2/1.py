# 定义罗马数字符号对应的表，分别为个位、十位、百位、千位的罗马数字表示
roman_numerals = (
    ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),  # 个位
    ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),  # 十位
    ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),  # 百位
    ("", "M", "MM", "MMM"),  # 千位
)

def Digital2Rome(num: int) -> str:
    # 根据千位、百位、十位、个位分别从R中获取对应的罗马数字
    return roman_numerals[3][num // 1000] + roman_numerals[2][num // 100 % 10] + roman_numerals[1][num // 10 % 10] + roman_numerals[0][num % 10]

res=input("请输入一个数(0,3999]:")
res=Digital2Rome(int(res))
print(f"翻译成罗马数字是：{res}")