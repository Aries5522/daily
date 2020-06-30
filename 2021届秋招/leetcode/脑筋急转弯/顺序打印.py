from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while True:
            for i in range(l, r + 1): res.append(matrix[l][i])
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1
            if r < l: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1
            if b < t: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1
            if r < l: break
        return res


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(matrix))
