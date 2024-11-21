def numRescueBoats(people, limit):
    """
    计算承载所有人所需的最小船数。
    :param people: 各人的体重数组
    :param limit: 每艘船可以承载的最大重量
    :return: 最小船数
    """
    people.sort()  # 按体重升序排序，以便优先安排轻的人
    boats = 0  # 初始化船数为0
    left, right = 0, len(people) - 1  # 设置左右指针，分别指向最轻和最重的人
    while left <= right:  # 当左指针不大于右指针时循环
        if people[left] + people[right] <= limit:  # 如果最轻和最重的人可以同船
            left += 1  # 将最轻的人移动到下一艘船
        right -= 1  # 将最重的人移动到下一艘船
        boats += 1  # 每轮都需要至少一艘船
    return boats

# 测试用例
print("请输入体重的序列:1,2")
print("请输入救生艇的最大载重量:3")
print(f"需要的救生艇数量是:{numRescueBoats([1,2], 3)}")
print("--------------------------------------")
print("请输入体重的序列:3,5,3,4")
print("请输入救生艇的最大载重量:5")
print(f"需要的救生艇数量是:{numRescueBoats([3,5,3,4], 5)}")
print("--------------------------------------")
print("请输入体重的序列:3,2,2,1")
print("请输入救生艇的最大载重量:3")
print(f"需要的救生艇数量是:{numRescueBoats([3,2,2,1], 3)}")