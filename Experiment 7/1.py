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

def maxPathSum(root: Node) -> int:
    """
    查找二叉树中子树的最大结点之和。
    :param root: 二叉树的根节点。
    :return: 子树的最大结点之和。
    """
    max_sum = float('-inf')  # 初始化最大和为负无穷大，用于比较
    
    def max_gain(node):
        """
        递归计算从当前节点到其子树的最大路径增益。
        :param node: 当前处理的节点。
        :return: 从当前节点到其子树的最大路径增益。
        """
        nonlocal max_sum  # 使用nonlocal声明，使得max_sum可以在函数内部被修改
        
        if not node:  # 如果节点为空，返回0
            return 0
        
        left_gain = max(max_gain(node.left), 0)  # 递归计算左子树的最大增益，如果为负则取0
        right_gain = max(max_gain(node.right), 0)  # 递归计算右子树的最大增益，如果为负则取0
        
        new_price = node.val + left_gain + right_gain  # 计算以当前节点为根的子树的总价值
        max_sum = max(max_sum, new_price)  # 更新全局最大和
        
        return node.val + max(left_gain, right_gain)  # 返回当前节点的价值加上两个子树中较大的价值
    
    max_gain(root)  # 从根节点开始递归计算最大路径和
    return max_sum  # 返回计算得到的最大路径和

# 测试用例
root = buildTree([1, -5, 2, 0, 3, -4, -5], 0)
print("请输入数组A=1,-5,2,0,3,-4,-5")
print(f"最大子树和是:{maxPathSum(root)}")  # 输出：3