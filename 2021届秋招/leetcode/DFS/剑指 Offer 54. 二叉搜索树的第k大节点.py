# Definition for a binary tree node.

"""



剑指 Offer 54. 二叉搜索树的第k大节点
先序遍历,中序遍历和后续遍历


遍历模板
def dfs(root):
    if not root:return None
    print(root.val)###先序遍历
    dfs(root.left)
    print(root.val)###中序遍历
    dfs(root.right)
    print(root.val)###后序遍历

二叉搜索树钟中序遍历是从小到大的,那么这一题就要用中序遍历的倒叙第k个数字/
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k
        def dfs(root):
            if not root:return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)
        dfs(root)
        return self.res
