def destCity(paths: list[list[str]]) -> str:
    """
    找出旅行的终点站。
    :param paths: 旅行线路图
    :return: 终点站名称
    """
    in_degree = {}  # 记录每个城市的入度
    out_degree = {}  # 记录每个城市的出度

    # 构建图
    for start, end in paths:
        if start not in out_degree:
            out_degree[start] = 0
        if end not in in_degree:
            in_degree[end] = 0
        out_degree[start] += 1
        in_degree[end] += 1

    # 寻找入度大于0且出度为0的城市
    for city in in_degree:
        if city not in out_degree or out_degree[city] == 0:
            return city
    return None

def test(paths:list[list[str]])->None:
    # 将路径列表转换为字符串，去除引号
    path_str = str(paths).replace("'", "")
    result = destCity(paths)
    print(f"旅行路线：{path_str}的终点城市是：{result}")

# 测试用例
test([["昆明","墨江"],["墨江","普洱"],["普洱","景洪"]])
test([["昆明","大理"],["丽江","昆明"],["大理","迪庆"]])
test([["昆明","腾冲"]])