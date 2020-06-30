#Definition for a binary tree node.



"""
树的DFS一定要注意步骤



递归的模板

def dfs(x,y):
    第一步:判断递归终止条件
    第二步:如果不终止
    找到下一次递归的输入x和y

    判断是否满足一定条件:要做什么事情
    开始下一次递归
    dfs(x,y)


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res=[]
        path=[]
        def dfs(root,target):
            if not root:return##break条件
            path.append(root.val)
            # print(root.val)
            target=target-root.val##找下一步输入
            if target==0 and (not root.left) and (not root.right): # 判断要做什么
                res.append(list(path))
            dfs(root.left, target)
            dfs(root.right, target)
            print(path)
            path.pop()##难点所在,回溯过程要删除加的点

        dfs(root,sum)
        return res