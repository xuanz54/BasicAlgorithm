import random

def Shuffle():
    """
    模拟发牌过程，将52张牌随机分配给4个玩家，每人13张牌。
    
    返回一个13x4的字符串二维列表，其中保存4个玩家的发牌情况。
    
    :return: list, 一个13x4的二维字符串列表，保存4个玩家的发牌情况
    """
    # 生成52张牌，花色为S（黑桃），H（红桃），D（方片），C（梅花），点数为2到A
    suits = ['♠', '♥', '♦', '♣']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = [f'{suit}{value}' for suit in suits for value in values]

    random.shuffle(cards)  # 随机打乱牌序

    # 初始化一个13x4的二维列表，字符串格式，来存储发牌情况
    player_cards = [["" for _ in range(4)] for _ in range(13)]

    # 按顺序将每张牌分配给玩家
    for i in range(52):
        row = i // 4  # 行索引（每个玩家13张牌）
        col = i % 4   # 列索引（4个玩家）
        player_cards[row][col] = cards[i]

    return player_cards  # 返回一个字符串二维列表

def display_cards(player_cards):
    """
    按指定格式显示发牌结果。

    :param player_cards: list, 13x4的二维字符串列表，保存4个玩家的发牌情况
    """
    players = ['玩家E', '玩家S', '玩家W', '玩家N']
    for i in range(4):
        # 每个玩家的牌显示在一行
        player_hand = [player_cards[j][i] for j in range(13)]
        print(f"{players[i]}: {' '.join(player_hand)}")

# 示例运行
player_cards = Shuffle()
display_cards(player_cards)
