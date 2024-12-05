def addBinary(a, b):
    # 先将二进制字符串转换为整数
    num1 = int(a, 2)
    num2 = int(b, 2)
    # 使用内置函数进行加法并转换回二进制字符串
    sum_binary = bin(num1 + num2)
    # bin函数返回值前缀为'0b', 需要去掉
    return sum_binary[2:]
 
# 测试用例
# 获取用户输入的两个二进制字符串
a=input("请输入a=")
b=input("请输入b=")
# 输出两个二进制字符串的和
print(f"{a}+{b}={addBinary(a, b)}")