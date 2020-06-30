

"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
利用队列先进先出
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        queen=[]
        queen.append(root)
        while queen!=[]:
            node=queen.pop(0)
            res.append(node.val)
            if node.left:
                queen.append(node.left)
            if node.right:
                queen.append(node.right)
        return res