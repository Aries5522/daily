"""


数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

https://leetcode-cn.com/problems/generate-parentheses/

q切记考虑回溯过程,回到上一个函数初始状态

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def dfs(left, right, temp):
            if left == 0 and right == 0:
                res.append(''.join(temp))
                return
            if left > 0:
                temp .append( "(")
                dfs(left-1, right, temp)
                temp.pop(-1)###回溯过程中记得返回以前状态
            if left < right:
                temp .append( ")")
                dfs(left, right-1, temp)
                temp.pop(-1)
        dfs(n, n, temp)
        return res


print(Solution().generateParenthesis(3))
