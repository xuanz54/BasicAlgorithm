def kClosestNumbers(A: list[int], target: int, k: int) -> list[int]:
    """
    在给定的有序数组中找到与目标值最接近的k个数。
    :param A: 有序数组
    :param target: 目标值
    :param k: 需要找到的最接近数的个数
    :return: 与目标值最接近的k个数
    """
    # 二分查找，找到目标附近的位置
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    # 设定两个指针，分别指向目标位置的左右两侧
    left, right = left - 1, left
    
    # 用于存放结果
    result = []
    
    # 使用双指针扩展，找到k个最接近的数字
    for _ in range(k):
        if left >= 0 and right < len(A):
            # 比较左右两边，选择更接近target的
            if abs(A[left] - target) <= abs(A[right] - target):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        elif left >= 0:  # 如果右指针越界
            result.append(A[left])
            left -= 1
        else:  # 如果左指针越界
            result.append(A[right])
            right += 1
    
    return result

# 测试用例
print("请输入数组A=1, 2, 3")
print("请输入target=2")
print("请输入k=3")
print(f"最接近的数是: {kClosestNumbers([1, 2, 3], 2, 3)}")  # 输出：[2, 1, 3]
print("请输入数组A=1, 4, 6, 8")
print("请输入target=3")
print("请输入k=3")
print(f"最接近的数是: {kClosestNumbers([1, 4, 6, 8], 3, 3)}")  # 输出：[4, 1, 6]