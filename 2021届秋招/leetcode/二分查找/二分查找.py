"""
二分查找模板:
[l, r) 左闭右开

def binary_search(l, r):
    while l < r:
        m = l + (r - l) // 2
        if f(m):    # 判断找了没有，optional
            return m
        if g(m):
            r = m   # new range [l, m)
        else:
            l = m + 1 # new range [m+1, r)
    return l    # or not found

"""

"""
完全平方
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        # if x==0:return 0
        l,r=0,x+1         ###因为输出空间可能为x
        while l<r:
            mid=l+(r-l)//2
            if mid**2==x:
                return mid
            if mid**2<x:
                l=mid+1
            else:
                r=mid
        return l-1


print(Solution().mySqrt(0))