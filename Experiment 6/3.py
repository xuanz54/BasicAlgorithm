def longestIncreasingContinuousSubsequence(nums:list[int])->int:
    """
    找到最长上升连续子序列的长度（从左到右或从右到左）。
    
    :param nums: 数组，包含整数。
    :return: 最长上升连续子序列的长度。
    """
    if not nums:
        return 0
    # 计算左到右的最长子序列
    max_len_lr = 1
    cur_len_lr = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur_len_lr += 1
        else:
            cur_len_lr = 1
        max_len_lr = max(max_len_lr, cur_len_lr)

    # 计算右到左的最长子序列
    max_len_rl = 1
    cur_len_rl = 1
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            cur_len_rl += 1
        else:
            cur_len_rl = 1
        max_len_rl = max(max_len_rl, cur_len_rl)

    return max(max_len_lr, max_len_rl)

# 测试用例
nums1 = [99, 55, 7, 29, 80, 33, 19, 23, 6, 35, 40,
          27, 44, 74, 5, 17, 52, 36, 67, 32, 37, 42, 18, 
          77, 66, 62, 97, 79, 60, 94, 30, 2, 85, 22,
            26, 91, 3, 16, 8, 0, 48, 93, 39, 31, 63, 
            13, 71, 58, 69, 50, 21, 70, 61, 43, 12, 88, 47,
              45, 72, 76]
print(f"最长上升连续子序列的长度为：{longestIncreasingContinuousSubsequence(nums1)}")
nums2 = []
print(f"最长上升连续子序列的长度为：{longestIncreasingContinuousSubsequence(nums2)}")