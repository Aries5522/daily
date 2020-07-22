class Solution:
    def largestRectangleArea(self, heights) -> int:
        if not heights: return 0
        n = len(heights)
        left_ = [-2] * n
        right_ = [n - 1] * n
        left_[0] = -1
        for i in range(1, n):
            if heights[i] <= heights[i - 1]:
                k = left_[i-1]
                if k == -1:
                    left_[i] = -1
                while k != -1:
                    if heights[i] > heights[left_[k]]:
                        left_[i] = left_[k]
                        break
                    else:
                        k = left_[left_[k]]
            else:
                left_[i] = i - 1
        print(left_)


print(Solution().largestRectangleArea([3,1,6,4,5,2]))
