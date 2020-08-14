"""
折半删除,第k小数解法
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        flg = (m + n) % 2
        k = (m + n) // 2 - 1 + flg

        def binarydelete(nums1, nums2, k):
            m = len(nums1)
            n = len(nums2)
            if not nums1 and not nums2:
                raise ValueError
            if not nums1:
                return nums2[k] if flg == 1 else (nums2[k] + nums2[k + 1]) / 2
            if not nums1:
                return nums1[k] if flg == 1 else (nums2[k] + nums2[k + 1]) / 2
            if k == 0:
                return min(nums1[0], nums2[0])
            mid1 = m // 2 - 1
            mid2 = n // 2 - 1
            if nums1[mid1] <= nums2[mid2]:
                return binarydelete(nums1[mid1 + 1:], nums2, k - m // 2)
            else:
                return binarydelete(nums1, nums2[mid2 + 1:], k - n // 2)

        return binarydelete(nums1, nums2, k)


print(Solution().findMedianSortedArrays(nums1=[1, 3, 5, 8, 9, 10], nums2=[2, 4, 6, 7, 11, 12]))
