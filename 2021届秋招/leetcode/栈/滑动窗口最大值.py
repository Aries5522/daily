'''

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

正常来说是on,但是感觉可以用dp


这一题有点难:参考之前实现栈的结构包含最小值,使得找到最小值的为O(1)

使用一个双向队列来完成,左边出右边进
单调队列(从大到小)
有数值进来的时候,pop()掉比他小的
判断左边最大值是不是弹出去的那个,是的话就弹走,否则就保持

'''

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        n=len(nums)
        if n==0:return []
        if n<k:return []
        if n==k:return [max(nums)]
        deque=collections.deque()
        for i,j in zip(range(1-k,n+1-k),range(n)):
            print(deque)
            if i>0 and deque[0]==nums[i-1]:deque.popleft()
            while deque and nums[j]>deque[-1]:deque.pop()
            deque.append(nums[j])
            if i >=0:res.append(deque[0])
        return res

