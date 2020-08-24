# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix: return []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        res = []
        while True:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            if t >= b: break
            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1
            if r <= l: break
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b-1][i])
            b -= 1
            if t >= b: break
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if r <= l: break
        return res

        # write code here


print(Solution().printMatrix([[1,2],[3,4]]))
