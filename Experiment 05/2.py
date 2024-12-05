def ChessStyle()->list[int]:
    """
    解决象棋算式问题，返回每个棋子对应的数字。
    :return: 兵，炮，马，卒，车对应的值
    """
    for 兵 in range(10):  # 遍历兵的可能值
        for 炮 in range(10):  # 遍历炮的可能值
            if 炮 == 兵:
                continue
            for 马 in range(10):  # 遍历马的可能值
                if 马 == 兵 or 马 == 炮:
                    continue
                for 卒 in range(10):  # 遍历卒的可能值
                    if 卒 == 兵 or 卒 == 炮 or 卒 == 马:
                        continue
                    for 车 in range(10):  # 遍历车的可能值
                        if 车 == 兵 or 车 == 炮 or 车 == 马 or 车 == 卒:
                            continue
                        sum1 = 兵 * 1000 + 炮 * 100 + 马 * 10 + 卒
                        sum2 = 兵 * 1000 + 炮 * 100 + 车 * 10 + 卒
                        result = 车 * 10000 + 卒 * 1000 + 马 * 100 + 兵 * 10 + 卒
                        if sum1 + sum2 == result:  # 检查算式是否成立
                            return [兵, 炮, 马, 卒, 车]
    return None

# 测试用例
result = ChessStyle()
if result:
    print("兵=%d, 炮=%d, 马=%d, 卒=%d, 车=%d" % (result[0], result[1], result[2], result[3], result[4]))
else:
    print("无解")