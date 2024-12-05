class Node:
    """
    二叉树节点的类定义
    
    :param val: 节点的值，可以是任何类型，包括None
    :param left: 左子节点，默认为None
    :param right: 右子节点，默认为None
    """
    def __init__(self, val=None, left=None, right=None):
        self.val = val  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点

def build_tree(nums):
    """
    使用层序遍历的方法创建二叉树
    
    :param nums: 包含节点值的列表，None表示空节点
    :return: 构建好的二叉树的根节点
    """
    if not nums:
        return None  # 如果输入列表为空，返回None

    root = Node(nums[0])  # 创建根节点
    queue = [root]  # 使用队列进行层序遍历
    i = 1  # 索引从1开始

    while queue and i < len(nums):
        current = queue.pop(0)  # 取出队列的第一个节点
        
        if i < len(nums):
            current.left = Node(nums[i])  # 创建左子节点
            queue.append(current.left)  # 将左子节点加入队列
            i += 1
        
        if i < len(nums):
            current.right = Node(nums[i])  # 创建右子节点
            queue.append(current.right)  # 将右子节点加入队列
            i += 1

    return root  # 返回构建好的树的根节点

def preorder_traversal(root):
    """
    前序遍历二叉树并直接打印结果
    
    :param root: 二叉树的根节点
    """
    def dfs(node):
        if not node or node.val is None:
            return  # 如果节点为空或值为None，返回
        print(node.val, end=" ")  # 打印当前节点值
        dfs(node.left)  # 遍历左子树
        dfs(node.right)  # 遍历右子树
    
    print("前序遍历结果:", end="")
    dfs(root)  # 从根节点开始遍历
    print()

def inorder_traversal(root):
    """
    中序遍历二叉树并直接打印结果
    
    :param root: 二叉树的根节点
    """
    def dfs(node):
        if not node or node.val is None:
            return  # 如果节点为空或值为None，返回
        dfs(node.left)  # 遍历左子树
        print(node.val, end=" ")  # 打印当前节点值
        dfs(node.right)  # 遍历右子树
    
    print("中序遍历结果:", end="")
    dfs(root)  # 从根节点开始遍历
    print()

def postorder_traversal(root):
    """
    后序遍历二叉树并直接打印结果
    
    :param root: 二叉树的根节点
    """
    def dfs(node):
        if not node or node.val is None:
            return  # 如果节点为空或值为None，返回
        dfs(node.left)  # 遍历左子树
        dfs(node.right)  # 遍历右子树
        print(node.val, end=" ")  # 打印当前节点值
    
    print("后序遍历结果:", end="")
    dfs(root)  # 从根节点开始遍历
    print()

def level_order_traversal(root):
    """
    层序遍历二叉树并直接打印结果
    
    :param root: 二叉树的根节点
    """
    if not root:
        return  # 如果根节点为空，返回
    
    print("层序遍历结果:", end="")
    queue = [root]  # 使用队列进行层序遍历
    while queue:
        current = queue.pop(0)  # 取出队列的第一个节点
        if current.val is not None:
            print(current.val, end=" ")  # 打印当前节点值
        if current.left:  # 如果左子节点存在，加入队列
            queue.append(current.left)
        if current.right:  # 如果右子节点存在，加入队列
            queue.append(current.right)
    print()

# 测试用例
nums = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, None, 9]
print("输入数组:", nums)

root = build_tree(nums)

preorder_traversal(root)
inorder_traversal(root)
postorder_traversal(root)
level_order_traversal(root)