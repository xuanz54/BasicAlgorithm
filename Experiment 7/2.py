class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None
    node = Node(nums[index])
    node.left = buildTree(nums, 2 * index + 1)
    node.right = buildTree(nums, 2 * index + 2)
    return node

def closestValue(root: Node, target: float) -> int:
    """
    在二叉搜索树中找到最接近给定值的节点值。
    :param root: 二叉搜索树的根节点。
    :param target: 给定的浮点数目标值。
    :return: 树中最接近target的节点值。
    """
    closest = root.val
    diff = abs(target - root.val)
    
    while root:
        # 如果左子树可能包含更接近的值，则更新当前节点和差异
        if root.left and (target - root.left.val) <= diff:
            closest = root.left.val
            diff = abs(target - root.left.val)
            root = root.left
        # 如果右子树可能包含更接近的值，则更新当前节点和差异
        elif root.right and (root.right.val - target) < diff:
            closest = root.right.val
            diff = abs(target - root.right.val)
            root = root.right
        else:
            break
    return closest

# 测试用例
nums1 = [5, 4, 9, 2, None, 8, 10]
root1 = buildTree(nums1, 0)
print("请输入数组:5,4,9,2,None,8,10")
print("请输入target=6.124780")
print(f"最接近的值是:{closestValue(root1, 6.124780)}")
nums2 = [3,2,4,1]
root2 = buildTree(nums2, 0)
print("请输入数组:3,2,4,1")
print("请输入target=4.142857")
print(f"最接近的值是:{closestValue(root2, 4.142857)}")