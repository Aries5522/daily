"""
自己想的一个题,简单题
是剑指 Offer 41. 数据流中的中位数的子题目


"""


class Solution:
    def insert_bin(self,nums,target):
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
        return nums

print(Solution().insert_bin([2,6,10],6))