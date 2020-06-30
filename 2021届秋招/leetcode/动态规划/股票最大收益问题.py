'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 做差后 转换为最大子序和问题

 动态规划

 https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        if n<=1:
            return 0
        temp=[]
        for i in range(n-1):
            temp.append(prices[i+1]-prices[i])
        print(temp)
        dp=[temp[0]]
        for i in range(1,n-1):
            dp.append(max(temp[i],temp[i]+dp[i-1]))
        print(dp)
        return max(max(dp),0)