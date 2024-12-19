class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: Node)-> int:
    """
    计算二叉树中的最大路径和。
    :param root: 二叉树的根节点。
    :return: 最大路径和。
    """
    max_sum = float('-inf')  # 初始化全局最大和
    
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
            
        # 计算左右子树的最大贡献值
        left_gain = max(max_gain(node.left), 0)  # 如果子树贡献为负，则不选取该子树
        right_gain = max(max_gain(node.right), 0)
        
        current_path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path_sum)  # 更新全局最大和
        
        return node.val + max(left_gain, right_gain)  # 只能选择一条路径返回给父节点
    
    max_gain(root)  # 启动递归
    return max_sum

# 测试用例
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
print("最大路径和是:", maxPathSum(root1)) 

root2 = Node(-10)
root2.left = Node(9)
root2.right = Node(20)
root2.right.left = Node(15)
root2.right.right = Node(7)
print("最大路径和是:", maxPathSum(root2))