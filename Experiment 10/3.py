import heapq
def scheduleCourse(courses):
    """
    计算最多可以修读的课程数目。
    :param courses: 课程数组，每个元素为[durationi, lastDayi]
    :return: 最多可以修读的课程数目
    """
    courses.sort(key=lambda x: x[1])  # 按照lastDayi升序排序
    max_heap = []  # 用于存储课程持续时间的最大堆
    current_time = 0  # 当前时间
    for duration, last_day in courses:
        if current_time + duration <= last_day:
            heapq.heappush(max_heap, -duration)  # 将课程持续时间加入最大堆
            current_time += duration
        elif max_heap and -max_heap[0] > duration:
            current_time += duration + heapq.heappop(max_heap)  # 替换当前堆中持续时间最长的课程
    return len(max_heap)

# 测试用例
print(f"[100,200] [200,1300] [1000,1250] [2000,3200] 最多可以修读的课程数目为{scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])}门")
print(f"[1,2] 最多可以修读的课程数目为{scheduleCourse([[1,2]])}门")
print(f"[3,2] [4,3] 最多可以修读的课程数目为{scheduleCourse([[3,2],[4,3]])}门")