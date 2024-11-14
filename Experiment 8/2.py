class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Node, k: int) -> int:
    """
    找到二叉查找树中第 K 小的元素。
    :param root: 二叉查找树的根节点。
    :param k: 要找的第 K 小的元素。
    :return: 第 K 小的元素的值。
    """
    stack = [] # 用于中序遍历的栈
    current = root # 从根节点开始

    # 中序遍历，直到找到第 K 小的元素
    while stack or current:
        while current: # 向左走到底
            stack.append(current) 
            current = current.left
        current = stack.pop() 
        k -= 1
        if k == 0: # 如果找到第 K 小的元素
            return current.val
        current = current.right # 转向右子树

# 测试用例
root = Node(12)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(9)
root.right = Node(18)
root.right.left = Node(15)
root.right.right = Node(19)
root.right.left.right = Node(17)
root.right.left.right.left = Node(16)
print(f"第4小的节点值是{kthSmallest(root, 4)}")