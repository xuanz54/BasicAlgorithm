def combinationSum(candidates: list, target: int) -> list:
    """
    找出所有和为target的组合，候选数字可以重复使用。
    :param candidates: 候选数字列表。
    :param target: 目标值。
    :return: 所有满足条件的组合列表。
    """
    candidates.sort()
    result = []
    combination = []

    def backtrack(start, current_sum):
        """
        使用回溯法遍历所有可能的组合。
        :param start: 当前递归的起始索引。
        :param current_sum: 当前累积的和。
        """
        if current_sum == target:
            # 如果累积和等于目标值，添加当前组合到结果中
            result.append(combination.copy())
            return
        for i in range(start, len(candidates)):
            if current_sum + candidates[i] > target:
                # 如果当前组合的和超过目标值，停止当前递归路径
                break
            combination.append(candidates[i])
            backtrack(i, current_sum + candidates[i])
            combination.pop()

    backtrack(0, 0)
    return result
def show_res(nums: list):
    for i in range(len(nums)):
        print(f"第{i+1}种组合方式: {nums[i]}")
# 测试用例
candidates1 = [2, 3, 6, 7]
target1 = 7
print(f"候选值数组:{candidates1},目标值:{target1}")
show_res(combinationSum(candidates1, target1))  # 输出: [[7], [2, 2, 3]]
print("-------------------------------")
candidates2 = [1]
target2 = 3
print(f"候选值数组:{candidates2},目标值:{target2}")
show_res(combinationSum(candidates2, target2))  # 输出: [[1, 1, 1]]