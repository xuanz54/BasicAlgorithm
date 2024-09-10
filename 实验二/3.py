def rotate(nums: list[int], k: int) -> list[int]:
    # 定义一个辅助函数来翻转数组从索引 i 到 j 的元素
    def reverse(i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)  # 获取数组的长度
    if n == 0 or k % n == 0:  # 如果数组为空或 k 是 n 的倍数，则不需要旋转
        return nums

    k %= n  # 由于数组长度有限，轮转 k 次和轮转 k%n 次效果相同
    reverse(0, n - 1)  # 首先翻转整个数组
    reverse(0, k - 1)  # 然后翻转数组的前 k 个元素
    reverse(k, n - 1)  # 最后翻转数组剩余的元素

    return nums

def test_rotate(nums: list[int], k: int)->None:
    print(f"数组:{nums}")
    print(f"向右轮转{k}次")
    print(f"轮转后的数组:{rotate(nums, k)}")

# 测试
test_rotate([1, 2, 3, 4, 5, 6], 2)
test_rotate([-1, -100, 3, 99], 3)