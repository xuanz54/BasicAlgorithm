def evalRPN(tokens: list[str])->int:
    # 评估逆波兰表达式并返回结果
    stack = []  # 使用栈来保存操作数
     
    # 定义操作符的运算规则
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),  # 这里需要注意python的除法是浮点数，需要强制转换为整型
    }
     
    for token in tokens:
        if token in operators:
            # 如果是操作符，则从栈中取出两个操作数进行运算
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            # 将运算结果压回栈中
            stack.append(result)
        else:
            # 如果是数字，则直接压入栈中
            stack.append(int(token))
     
    # 最终栈中只剩下一个值，即为计算结果
    return stack.pop()
 
# 测试用例
print("逆波兰式:[4, 13, 5, /, +]")
print(f"运算结果是:{evalRPN(["4", "13", "5", "/", "+"])}")  # 输出: 6
print("逆波兰式:[10, 6, 9, 3, +, -11, *, /, *, 17, +, 5, +]")
print(f"运算结果是:{evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])}")  # 输出: 22
print("逆波兰式:[18]")
print(f"运算结果是:{evalRPN(["18"])}")  # 输出: 18