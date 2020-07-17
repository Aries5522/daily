"""

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

先找根节点再中序遍历,就很简单

"""

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        target=pNode
        while pNode.next:
            pNode=pNode.next
        res=[]
        def dfs(Node):
            if not Node:return
            if Node.left:
                dfs(Node.left)
            res.append(Node)
            if Node.right:
                dfs(Node.right)
        dfs(pNode)
        res.append(None)
        for i in range(len(res)-1):
            if res[i] == target:
                return res[i+1]