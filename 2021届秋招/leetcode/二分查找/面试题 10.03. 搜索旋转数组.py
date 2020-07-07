"""

搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-rotate-array-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

from typing import List
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        if n == 0:
            return -1
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2+1
            print(arr[mid])
            if arr[l] <= arr[mid]:
                if target < arr[l]:
                    l = mid
                elif target >= arr[mid]:
                    l = mid
                else:
                    r = mid-1
            if arr[l] > arr[mid]:
                if target > arr[r]:
                    r = mid-1
                elif target >= arr[mid]:
                    l = mid
                else:
                    r = mid-1
        return l if arr[l]==target else -1

print(Solution().search(arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5))
