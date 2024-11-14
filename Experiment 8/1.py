class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isValidBST(root: Node) -> bool:
    """
    判断给定的二叉树是否是合法的二叉查找树(BST)。
    :param root: 二叉树的根节点。
    :return: 布尔值，表示树是否是BST。
    """
    return isBST(root, float('-inf'), float('inf'))

def isBST(node, lower, upper)->bool:
    """
    判断给定的节点是否是合法的BST。
    :param node: 节点。
    :param lower: 左子树的最小值。
    :param upper: 右子树的最大值。
    :return: 布尔值，表示节点是否是合法的BST。
    """
    if not node:
        return True
    if not lower < node.val < upper:
        return False
    return isBST(node.left, lower, node.val) and isBST(node.right, node.val, upper)

# 测试用例1
print("请输入建树的数组:2,1,4,#,#,3,5")
root1 = Node(2)
root1.left = Node(1)
root1.right = Node(4)
root1.right.left = Node(3)
root1.right.right = Node(5)
if isValidBST(root1):
    print("这棵树是BST")
# 测试用例2
print("请输入建树的数组:-2147483648,#,2147483647")
root2 = Node(-2147483648)
root2.right = Node(2147483647)
if isValidBST(root2):
    print("这棵树是BST")
# 测试用例3
print("请输入建树的数组:")
root3=None
if isValidBST(root3):
    print("这棵树是BST")