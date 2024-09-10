from typing import List
def trap(height: List[int]) -> int:
    # 初始化：雨水总量，左指针，右指针，左右最大高度
    ans = left = pre_max = suf_max = 0
    right = len(height) - 1
    # 双指针向中间靠拢
    while left < right:
        pre_max = max(pre_max, height[left])  # 更新左侧最大高度
        suf_max = max(suf_max, height[right]) # 更新右侧最大高度
        if pre_max < suf_max:
            # 左边低于右边，用左边的最大高度计算雨水
            ans += pre_max - height[left]
            left += 1
        else:
            # 右边低于或等于左边，用右边的最大高度计算雨水
            ans += suf_max - height[right]
            right -= 1
    return ans  # 返回总的接雨水量

# 测试用例
column_array1=[0,1,0,2,1,0,1,3,2,1,2,1]
print(f"柱子数组:{column_array1}")
res1=trap(column_array1)
print(f"接了{res1}个单位的雨水")

column_array2=[4,2,0,3,2,5]
print(f"柱子数组:{column_array2}")
res2=trap(column_array2)
print(f"接了{res2}个单位的雨水")