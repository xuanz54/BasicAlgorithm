from functools import cmp_to_key
def largestNumber(nums):
    """
    将给定的非负整数数组重新排列，组成一个最大的整数。
    :param nums: 非负整数数组
    :return: 组成的最大整数
    """
    # 将整数转换为字符串，以便进行比较
    nums = list(map(str, nums))
    # 定义比较规则：如果两个数的拼接结果不同，则根据拼接结果的大小进行排序
    nums.sort(key=cmp_to_key(lambda x, y: int(y+x) - int(x+y)))
    # 将排序后的字符串拼接成一个整数
    largest_num = ''.join(nums)
    # 如果结果以0开头，说明所有数都是0，直接返回0
    return largest_num if largest_num[0] != '0' else '0'

# 测试用例
print(f"[1,2,3,4,5,6,7,8,9,0]组成的数组能够构成最大数: {largestNumber([1,2,3,4,5,6,7,8,9,0])}") 
print(f"[2147483647,2147483647,2147483646,9,1,8]组成的数组能够构成最大数: {largestNumber([2147483647,2147483647,2147483646,9,1,8])}")
print(f"[0,0,0,0]组成的数组能够构成最大数: {largestNumber([0,0,0,0])}")