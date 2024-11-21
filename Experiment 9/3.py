import math

def min_weight(stripies):
    """
    计算所有stripies两两碰撞至只剩一个时的最小质量。
    :param stripies: 变形虫体重列表
    :return: 最小质量
    """
    # 将列表按从大到小排序
    stripies.sort(reverse=True)
    # 当列表中有多于一个元素时，继续执行循环
    while len(stripies) > 1:
        # 碰撞后的新质量是两个质量的2倍的几何平均值
        new_weight = 2 * math.sqrt(stripies[0] * stripies[1])
        stripies[0] = new_weight  # 更新第一个元素
        stripies.pop(1)  # 移除第二个元素
        # 重新排序列表
        stripies.sort(reverse=True)
    # 返回最终的质量，格式化为三位小数
    return "{:.3f}".format(stripies[0])

# 测试用例
print("请输入变形虫的体重序列:72,30,50")
stripies = [72.0, 30.0, 50.0]
print(f"最后的变形虫的重量是{min_weight(stripies)}")