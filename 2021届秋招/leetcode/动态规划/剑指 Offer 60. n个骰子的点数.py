"""



把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


答案参考这个人:
https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/java-dong-tai-gui-hua-by-zhi-xiong/
"""


class Solution:
    def twoSum(self, n: int) -> List[float]:
        pre=[1/6]*6
        for i in range(2,n+1):
            temp=[0]*(i*5+1)
            # print(temp)
            for j in range(len(pre)):
                for x in range(6):
                    temp[x+j]+=pre[j]/6               ##这里是关键,temp[0]只有一种情况出现,temp[1]有两种,temp[2]可能会有0,2还有2,0还有1,1组合.累加会考虑到所有情况,很妙
            pre=temp
        return pre

