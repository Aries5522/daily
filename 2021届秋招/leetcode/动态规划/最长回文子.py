class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        动态规划
        """
        n = len(s)
        dp=[[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i]=1
        for i in range(n,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=1
                else:
                    if s[i]==s[j]:
                        dp[i][j]=dp[i+1][j-1]+2
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
        # print(dp)
        # def dp(i, j):
        #     # if i<j:
        #     #     return 1
        #     if i == j:
        #         return 1
        #     if i+1==j:
        #         return 2 if s[i]==s[j] else 1
        #     if s[i] == s[j]:
        #         return dp(i + 1, j - 1) + 2
        #     else:
        #         return max(dp(i + 1, j), dp(i, j -1))
        # return dp(0, n - 1)

print(Solution().longestPalindromeSubseq(s="bbbab"))
