class Solution:
    def mySqrt(self, x: int) -> int:
        # if x==0:return 0
        l=0
        r=x+1
        while l<r:
            mid=(r-l)/2+l
            if mid**2>x:
                r=mid
            elif mid**2==x:
                return mid
            else:l=mid
            if abs(mid**2-x)<=0.0001:
                return mid

print(Solution().mySqrt(9))