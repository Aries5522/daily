"""
动态规划 感觉比较难想到
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
https://leetcode-cn.com/problems/unique-binary-search-trees/


https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
"""



class Solution:
    def numTrees(self, n: int) -> int:
        G=[0]*(n+1)
        G[0]=1
        G[1]=1
        for i in range(2,n+1):
            for j in range(0,i+1):
                G[i]+=(G[i-j]*G[j-1])
        print(G)
        return G[n]

print(Solution().numTrees(3))