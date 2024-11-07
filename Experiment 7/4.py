def maximizeSweetness(sweetness: list[int], k: int) -> int:
    """
    找到一个最佳的切割策略,使得你所分得的巧克力总甜度最大。
    :param sweetness: 每个小块巧克力的甜度
    :param k: 要切割的次数(分给k个人)
    :return: 你所分得的巧克力总甜度的最大值
    """
    # 累积甜度数组，prefix_sum[i]表示从第0块到第i块巧克力的总甜度
    prefix_sum = [0]
    for s in sweetness:
        prefix_sum.append(prefix_sum[-1] + s)
    
    # 二分查找最小甜度，left是最小甜度，right是每份最大可分的甜度
    left, right = min(sweetness), sum(sweetness) // (k + 1)
    
    while left <= right:
        mid = (left + right) // 2  # 中间值即当前目标每份最小甜度
        # 如果能根据当前mid值分出k+1份巧克力
        if can_divide(prefix_sum, k + 1, mid):
            left = mid + 1  # 可以分割，尝试更大的甜度
        else:
            right = mid - 1  # 不行，减小甜度
    
    return right  # 返回最大的可分割的最小甜度
    
def can_divide(prefix_sum, parts, target):
    """
    检查是否能够按照目标值将巧克力分成parts份。
    :param prefix_sum: 累积甜度数组
    :param parts: 要分成的份数
    :param target: 目标值,每份巧克力的最小总甜度
    :return: 是否可以分成parts份
    """
    count = 0  # 记录切割后的份数
    last_cut = 0  # 上一次切割的位置
    
    # 遍历每一块巧克力，判断是否可以满足目标甜度
    for i in range(1, len(prefix_sum)):
        # 如果当前累积甜度大于等于目标甜度，切割一次
        if prefix_sum[i] - prefix_sum[last_cut] >= target:
            count += 1  # 切割出一份
            last_cut = i  # 更新切割位置
    
    return count >= parts  # 判断是否切割出了k+1份

# 测试用例
print("请输入甜度数组:1,2,3,4,5,6,7,8,9")
print("请输入朋友数量K=5")
print(f"最大总甜度:{maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)}")  # 输出：6
print("------------------------------------------------------------")
print("请输入甜度数组:5,6,7,8,9,1,2,3,4")
print("请输入朋友数量K=8")
print(f"最大总甜度:{maximizeSweetness([5, 6, 7, 8, 9, 1, 2, 3, 4], 8)}")  # 输出：1
print("------------------------------------------------------------")
print("请输入甜度数组:1,2,2,1,2,2,1,2,2")
print("请输入朋友数量K=2")
print(f"最大总甜度:{maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2)}")  # 输出：5

