import sys
n=int(sys.stdin.readline().strip("\n"))
s1=sys.stdin.readline().strip("\n").split(" ")
s2=sys.stdin.readline().strip("\n").split(" ")
s1="".join(s1)
s2="".join(s2)
n=len(s1)
def longestcommon(s1,s2):
    s1="*"+s1
    s2="#"+s2
    n1=len(s1)
    n2=len(s2)
    dp=[[0]*n2 for i in range(n1)]
    for i in range(1,n1):
        for j in range(1,n2):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n1-1][n2-1]
k=longestcommon(s1,s2)/n
if k>0.5:
    print("%.2f" % k,"Yes")
else:
    print("%.2f" % k,"no")
