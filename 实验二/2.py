def isValid(s: str) -> bool:
    # 初始化一个空的栈，用于存放期望匹配的右括号
    stack = []
    # 遍历输入的括号字符串
    for c in s:
        # 如果当前字符是左括号之一，则将相应的右括号压入栈中
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        else:
            # 如果遇到右括号，判断栈是否为空或栈顶元素是否与当前右括号不匹配
            if not stack or stack.pop() != c:
                return False
    
    # 如果栈为空，说明所有括号都匹配正确，否则返回False
    return len(stack) == 0

# 接收用户输入的括号字符串并验证其有效性
res = input("请输入括号字符串：")
print(isValid(res))
