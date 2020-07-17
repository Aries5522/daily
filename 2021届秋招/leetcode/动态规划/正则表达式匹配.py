class Solution:
    # @classmethod
    def __init__(self):
        None
    def isMatch(self,s,p):
        if (not s and not p):
            return True
        if (not s and p) or (not p and s):
            return False
        M=len(s)
        N=len(p)
        dp=[[0]*N for _ in range(M)]
        dp[0][0]=True
        print(dp)
        for j in range(1,N):
            dp[0][j]=dp[0][j-1] if p[j-1]=="*" else False
        for i in range(1,M):
            dp[i][0]=False
        print(dp)
        for i in range(1,M):
            for j in range(1,N):
                if p[j-1]!="*":
                    dp[i][j]=dp[i-1][j-1]
                else:
                    if s[i-1]!=p[j-2]:
                        dp[i][j]=dp[i][j-2]
                    elif s[i-1]==p[j-2] or p[j-2]==".":


        return dp[N-1][M-1]



print(Solution().isMatch(s="aa",p="a*********"))