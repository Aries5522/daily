"""
朋友圈

还没弄懂



"""

from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        p = [i for i in range(len(M))]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    a = find(i)     ## 这里就是merge操作，重新写一个函数太麻烦了
                    b = find(j)
                    p[a] = b       ## 直接修改数组中的根节点
        print(p)
        for i in range(len(M)):   ## 需要多这一步，将所有的点都回归其根节点，然后在判断根的数量有多少
            find(i)
        return len(set(p))
print(Solution().findCircleNum([[1,1,0],
 [1,1,0],
 [0,0,1]]))