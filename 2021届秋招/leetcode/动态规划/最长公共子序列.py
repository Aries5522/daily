class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = "*" + text1
        text2 = "#" + text2
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0] * (n2) for i in range(n1)]
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1 - 1][n2 - 1]

print(Solution().longestCommonSubsequence("abcde", "ace"))
