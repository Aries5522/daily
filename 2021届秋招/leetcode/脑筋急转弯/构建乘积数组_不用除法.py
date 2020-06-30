'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/

遍历两次从左到右从右到左,分块之后,对应相乘

'''

from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if len(a)==0:
            return []
        n=len(a)
        temp_k=[]
        temp_p=[]
        k=1
        p=1
        for i in a:
            k=k*i
            temp_k.append(k)
        for i in a[::-1]:
            p=i*p
            temp_p.append(p)
        print(temp_p,temp_k)
        res=[]
        res.append(temp_p[n-2])
        for i in range(0,n-2):
            res.append(temp_k[i]*temp_p[n-3-i])
        res.append(temp_k[n-2])
        return res


