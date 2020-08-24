# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
比较简单的dfs,判断某个节点的左右都没有(叶子节点),并且节点的值等于当前target


"""


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []

        def dfs(root, target, ans, res):
            if not root: return []
            if not root.left and not root.right and target == root.val:
                res.append(ans + [root.val])
                return
            if root.left:
                dfs(root.left, target - root.val, ans + [root.val], res)
            if root.right:
                dfs(root.right, target - root.val, ans + [root.val], res)
        res = []
        dfs(root, expectNumber, [], res)
        return res

        # write code here
