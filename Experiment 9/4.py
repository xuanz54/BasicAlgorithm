class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def minMeetingRooms(intervals):
    """
    计算所需最少会议室数量
    :param intervals: 会议时间区间列表
    :return: 所需最少会议室数
    """
    if not intervals:
        return 0
    
    # 分别存储开始时间和结束时间，并排序
    start_times = sorted([i.start for i in intervals])
    end_times = sorted([i.end for i in intervals])
    
    rooms_needed = 0  # 当前需要的会议室数量
    max_rooms = 0  # 最多需要的会议室数量
    start_ptr = 0  # 开始时间指针
    end_ptr = 0  # 结束时间指针
    
    while start_ptr < len(intervals):
        # 如果当前开始时间早于结束时间，表示需要新的会议室
        if start_times[start_ptr] < end_times[end_ptr]:
            rooms_needed += 1  # 增加所需会议室数量
            start_ptr += 1  # 移动开始时间指针
        else:
            rooms_needed -= 1  # 会议室结束，减少所需会议室数量
            end_ptr += 1  # 移动结束时间指针
        
        max_rooms = max(max_rooms, rooms_needed)  # 更新最多需要的会议室数量
    
    return max_rooms

# 测试用例
intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
print("会议开始时间:0,会议结束时间:30\n会议开始时间:5,会议结束时间:10\n会议开始时间:15,会议结束时间:20")
print(f"需要的最小会议室数量是:{minMeetingRooms(intervals1)}")
print("--------------------------------------")
intervals2 = [Interval(2, 7)]
print("会议开始时间:2,会议结束时间:7")
print(f"需要的最小会议室数量是:{minMeetingRooms(intervals2)}")