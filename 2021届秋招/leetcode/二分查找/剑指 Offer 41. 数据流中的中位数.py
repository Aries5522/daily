"""

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

二分找到要插入的地方,然后中位数直接输出
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_sort=[]

    def addNum(self, num: int) -> None:
        nums=self.data_sort
        target=num
        if not nums:
            nums.append(target)
        else:
            if target<=nums[0]:
                nums.insert(0,target)
            elif target>=nums[-1]:
                nums.append(target)
            else:
                l=0
                r=len(nums)-1
                while l<r:
                    mid=l+(r-l)//2
                    if nums[mid] <= target:
                        l=mid+1
                    elif nums[mid] > target:
                        r=mid
                nums.insert(l,target)
    def findMedian(self) -> float:
        n=len(self.data_sort)
        if n==0:
            return None
        if n%2==1:
            return self.data_sort[n//2]
        else:return  (self.data_sort[n//2-1]+self.data_sort[n//2])/2