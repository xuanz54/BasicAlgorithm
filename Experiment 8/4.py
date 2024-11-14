class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, val=0, left=Nonaae, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: LinkNode) -> Node:
    """
    将有序链表转换为高度平衡的二叉搜索树。
    :param head: 有序链表的头节点。
    :return: 平衡二叉搜索树的根节点。
    """
    def convert(values: list, start: int, end: int) -> Node:
        """
        将值列表的一段转换为BST。
        :param values: 值列表。
        :param start: 起始索引。
        :param end: 结束索引。
        :return: BST根节点。
        """
        if start > end:
            return None
            
        mid = (start + end) // 2
        root = Node(values[mid])
        
        root.left = convert(values, start, mid - 1)
        root.right = convert(values, mid + 1, end)
        
        return root

    # 将链表转换为列表
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
        
    if not values:
        return None
        
    return convert(values, 0, len(values) - 1)

def postorder(root: Node) -> None:
    """后序遍历打印树"""
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')

# 测试用例1
head1 = LinkNode(1)
head1.next = LinkNode(2)
head1.next.next = LinkNode(3)
print("链表内容是1->2->3->null")
root = sortedListToBST(head1)
print("转化为BST后后序遍历结果是", end=' ')
postorder(root)
print()
# 测试用例2
head2 = LinkNode(2)
head2.next = LinkNode(3)
head2.next.next = LinkNode(6)
head2.next.next.next = LinkNode(7)
print("链表内容是2->3->6->7->null")
root = sortedListToBST(head2)
print("转化为BST后后序遍历结果是", end=' ')
postorder(root)