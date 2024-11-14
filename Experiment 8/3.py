class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLeftMost(root: Node) -> int:
    """
    找到二叉树最后一行中最左边的值。
    :param root: 二叉树的根节点。
    :return: 最后一行最左边节点的值。
    """
    def getHeight(node: Node) -> int:
        """获取树的高度。"""
        if not node:
            return 0
        return max(getHeight(node.left), getHeight(node.right)) + 1
    
    def dfs(node: Node, depth: int, maxDepth: int) -> tuple:
        """
        深度优先搜索找最左下节点。
        :param node: 当前节点。
        :param depth: 当前深度。
        :param maxDepth: 树的最大深度。
        :return: (是否找到, 节点值)。
        """
        if not node:
            return False, None
        if depth == maxDepth:  # 如果到达最大深度且是叶子节点
            return True, node.val   
        found, val = dfs(node.left, depth + 1, maxDepth) # 优先搜索左子树
        if found:
            return True, val
        return dfs(node.right, depth + 1, maxDepth)

    maxDepth = getHeight(root)
    # 深度优先搜索找最左下节点
    _, result = dfs(root, 1, maxDepth)
    return result

# 测试用例1
print("请输入二叉树对应的数组:2,1,3")
root1 = Node(2)
root1.left = Node(1) 
root1.right = Node(3)
print(f"最左边节点的值是{findLeftMost(root1)}")
# 测试用例2
print("请输入二叉树对应的数组:1,2,3,4,5,6,#,#,7")
root2 = Node(1)
root2.left = Node(2) 
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(6)
root2.left.left.right = Node(7)   
print(f"最左边节点的值是{findLeftMost(root2)}")

