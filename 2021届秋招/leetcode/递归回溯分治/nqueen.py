from typing import List
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # temp=[[0]*n for _ in range(n)]

        temp = [[0] * n for _ in range(n)]
        record = [[0] * n for _ in range(n)]
        left = n

        def sum_(i, j):
            sum_1 = 0
            for k in range(n):
                sum_1 += temp[i][k]
            sum_2 = 0
            for k in range(n):
                sum_2 += temp[k][j]
            sum_3 = 0
            sum_4 = 0
            for idx in range(n):
                for jdx in range(n):
                    if idx + jdx == i + j:
                        sum_3 += temp[idx][jdx]
                    if idx - i == jdx - j:
                        sum_4 += temp[idx][jdx]

            return sum_1 + sum_2 + sum_3 + sum_4

        def traceback(left, temp, res, record):
            if left == 0:
                if max(record+temp)<=1:
                    record+=temp
                    res.append(copy.deepcopy(temp))
            for i in range(n):
                for j in range(n):
                    if sum_(i, j) == 0:
                        # print(i, j)
                        temp[i][j] = 1
                        traceback(left - 1, temp, res, record)
                        temp[i][j] = 0

        traceback(left, temp, res, record)
        return res


print(Solution().solveNQueens(n=4))
