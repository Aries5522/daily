"""
一般来说做不出来 感觉


dfs做法


交换两者顺序

确定搜索
判断搜索终止条件
x到倒数第二位就终止

因为最后一位确定了
如果不终止的话就
跳下一位

一直到跳出为止然后开始回溯


"""


from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        res=[]
        c=list(s)
        def dfs(x):
            if x==len(c)-1:
                res.append("".join(c))
            else:
                dict=set()
                for i in range(x,len(c)):
                    if c[i] in dict:continue
                    else:
                            dict.add(c[i])
                            c[i],c[x]=c[x],c[i]
                            dfs(x+1)
                            c[i],c[x]=c[x],c[i]
        dfs(0)
        return res
print(Solution().permutation("abc"))