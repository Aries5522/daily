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
            mid = l + (r - l) // 2
            if arr[l] < arr[mid]:
                if arr[l] <= target and target <= arr[mid]:
                    r = mid
                else:
                    l = mid + 1
            elif arr[l] > arr[mid]:
                if arr[mid] < target and target < arr[r]:
                    l = mid+1
                else:
                    r = mid
            else:
                while arr[l] != target and l<r:
                    l += 1
                    if arr[l] == target:
                        r = l
                        break
                if arr[l]==target:
                    return l
        return l if arr[l] == target else -1


print(Solution().search(arr=[-30, -25, -22, -22, -18, -12, -11, -11, -9, -8, -8, -1, 0, 0, 5, 6, 6, 13, 14, 16, 16, 18, 19, 19, 21, 21, 22, 23, 25, 26, 30, 30, 30, 32, 37, 38, 40, 41, 43, 43, 45, 45, 45, 46, 46, 47, 56, 59, 61, 62, 64, 65, 69, 73, 74, 80, 84, 84, 86, 86, 88, 88, 89, 89, 90, 90, 91, 92, 92, -93, -93, -87, -84, -82, -80, -80, -79, -77, -74, -73, -70, -68, -66, -64, -60, -58, -55, -52, -51, -51, -49, -46, -43, -34]
, target=89))
