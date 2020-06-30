"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


动态规划 dp[n]=dp[n-1]+dp[n-2]或者dp[n-1]
"""


class Solution:
    def translateNum(self, num: int) -> int:
        num=list(str(num))
        n=len(num)
        dp=[0]*(n)
        dp[0]=1
        if n==1:
            return 1
        if 10<=int(num[0]+num[1])<26:
            dp[1]=2
        else:
            dp[1]=1
        for i in range(2,n):
            if 10<=int(num[i-1]+num[i])<26:
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        print(dp)
        return dp[n-1]