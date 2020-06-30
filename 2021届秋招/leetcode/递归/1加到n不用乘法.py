"""

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
https://leetcode-cn.com/problems/qiu-12n-lcof/


可以用加法,那就递归
"""


class Solution:
    def sumNums(self, n: int) -> int:
        sum_=0
        def dfs(n):
            if n==0:
                return 0
            return dfs(n-1)+n
        sum_=dfs(n)
        return sum_