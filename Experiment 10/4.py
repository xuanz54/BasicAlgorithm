class Cow:
    """
    表示一头奶牛的类，包含奶牛到达牛舍的时间和每分钟破坏花朵的数量。
    """
    def __init__(self, t, d):
        """
        初始化方法，设置奶牛到达牛舍的时间和每分钟破坏花朵的数量。
        :param t: 奶牛到达牛舍的时间（分钟）。
        :param d: 奶牛每分钟破坏花朵的数量。
        """
        self.t = t
        self.d = d 
        self.div = d / t  # 计算破坏效率，即破坏花朵的速率除以到达牛舍的时间

    def __lt__(self, other):
        """
        重载小于运算符，用于比较两个奶牛的破坏效率。
        :param other: 另一个奶牛对象。
        :return: 如果当前奶牛的破坏效率大于另一个奶牛，则返回True。
        """
        return self.div > other.div 

def removeCows(cows):
    """
    确定约翰应该捡起奶牛的顺序，以最小化被破坏的花朵总数。
    :param cows: 奶牛数组，每个元素为[Ti, Di]，Ti代表奶牛到达牛舍的时间（分钟），Di代表奶牛每分钟破坏花朵的数量。
    :return: 最小化被破坏的花朵总数。
    """
    n = len(cows)
    # 输入的同时计算破坏力
    for i in range(n):
        cows[i] = Cow(cows[i][0], cows[i][1])  # 将奶牛列表中的每个元素转换为Cow对象
    cows.sort()  # 对奶牛列表进行排序，根据破坏效率从高到低
    ans = 0
    sum_d = 0
    for i in range(n):  # 计算所有奶牛的破坏效率
        sum_d += cows[i].d
    
    # 减去当前正在运输的奶牛的破坏效率，并计算被破坏的花朵总数
    for i in range(n - 1):
        sum_d -= cows[i].d
        ans += 2 * sum_d * cows[i].t
    
    return ans

# 测试用例
cows = [[3, 1], [2, 5], [2, 3], [3, 2], [4, 1], [1, 6]]
print("请输入奶牛的数量:6")
print("将第1只奶牛拉回牛舍的时间和每分钟吃掉花朵的数量:3,1")
print("将第2只奶牛拉回牛舍的时间和每分钟吃掉花朵的数量:2,5")
print("将第3只奶牛拉回牛舍的时间和每分钟吃掉花朵的数量:2,3")
print("将第4只奶牛拉回牛舍的时间和每分钟吃掉花朵的数量:3,2")
print("将第5只奶牛拉回牛舍的时间和每分钟吃掉花朵的数量:4,1")
print("将第6只奶牛拉回牛舍的时间和每分钟吃掉花朵的数量:1,6")
print(f"将奶牛全部拉回牛舍后，被吃掉的花朵总数为:{removeCows(cows)}")