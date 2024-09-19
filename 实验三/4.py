def isHappy(n):
    """判断一个数字是否是快乐数"""
    def get_next_number(num):
        """将每个数字拆分并求其平方和"""
        total_sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total_sum += digit * digit
        return total_sum
    
    seen_numbers = set()  # 用来记录已经出现过的数字，防止无限循环
    
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = get_next_number(n)
    
    return n == 1

def show_result(n):
    """显示数字是否为快乐数的结果"""
    if isHappy(n):
        print(f"{n}是快乐数")
    else:
        print(f"{n}不是快乐数")

# 测试用例
n1,n2=19,2
show_result(n1)
show_result(n2)