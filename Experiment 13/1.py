class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: Node) -> int:
    """
    计算所有根到叶的数的总和。
    :param root: 二叉树的根节点。
    :return: 所有根到叶的数的总和。
    """
    if not root:
        # 如果根节点为空，返回0
        return 0
    
    def dfs(node, current_sum):
        """
        深度优先搜索遍历二叉树，累积路径上的数字。
        :param node: 当前节点。
        :param current_sum: 当前累积的数字。
        :return: 当前路径表示的数字。
        """
        if not node.left and not node.right:
            # 如果是叶子节点，返回累积的数字
            return current_sum * 10 + node.val
        left_sum = 0
        right_sum = 0
        if node.left:
            # 遍历左子树
            left_sum = dfs(node.left, current_sum * 10 + node.val)
        if node.right:
            # 遍历右子树
            right_sum = dfs(node.right, current_sum * 10 + node.val)
        return left_sum + right_sum
    
    return dfs(root, 0)

# 测试用例
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
print(sumNumbers(root1))  

root2 = Node(4)
root2.left = Node(9)
root2.right = Node(0)
root2.left.left = Node(5)
root2.left.right = Node(1)
print(sumNumbers(root2))  