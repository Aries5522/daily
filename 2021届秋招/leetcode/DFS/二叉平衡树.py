"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

递归的模板

def dfs(x,y):
    第一步:判断递归终止条件

    判断是否满足一定条件:要做什么事情
    开始下一次递归
    dfs(x,y)
https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/

本题:

"""


class Solution:
    def isBalanced(self, root):
        if not root: return True  ##递归条件

        def depth(root):
            if not root:
                return 0
            return max(depth(root.left), depth(root.right)) + 1

        ##如果不终止,判断他的左右子 树是不是平衡的
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

