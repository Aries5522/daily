class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


def Order(root):  ##递归实现
    if not root:
        return None
    print(root.val)
    Order(root.left)
    Order(root.right)
    """###中序遍历
    Order(root.left)
    print(root.val)
    Order(root.right)
    """
    """
    ###后序遍历
    Order(root.left)
    Order(root.right)
    print(root.val)
    """
def depth(root):
    if not root :
        return 0
    return max(depth(root.left),depth(root.right))+1

def Order_not_dfs(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            stack.append(node)
            stack.append(None)  ##代表栈的下一个元素需要输出,精髓
        else:
            print(stack.pop().val)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
Order_not_dfs(root)