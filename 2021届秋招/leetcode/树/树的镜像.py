# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return None
        root.left,root.right=self.Mirror(root.right),self.Mirror(root.left)
        return root
        # write code here

'''
三步走
总的来说是一个递归
但是中间变量

'''