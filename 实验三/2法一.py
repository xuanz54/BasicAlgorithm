def addBinary(a: str, b: str) -> str:
    # 模拟二进制加法的每一步计算
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)  # 补齐较短的二进制串前导零
    b = b.zfill(max_len)
     
    carry = 0  # 进位
    result = []  # 结果用数组存储方便操作
     
    # 从右往左逐位相加
    for i in range(max_len - 1, -1, -1):
        bit_sum = carry  # 从上一次的进位开始
        bit_sum += int(a[i]) + int(b[i])
         
        # 当前位的结果是 bit_sum % 2, 进位是 bit_sum // 2
        result.append(str(bit_sum % 2))
        carry = bit_sum // 2
     
    # 如果最后有进位，记得加上
    if carry:
        result.append('1')
     
    # 翻转结果数组并合并为字符串
    return ''.join(result[::-1])
 
# 测试用例
# 接收用户输入的两个二进制字符串并进行加法运算
a=input("请输入a=")
b=input("请输入b=")
print(f"{a}+{b}={addBinary(a, b)}")