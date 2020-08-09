"""
从最右上角开始找,如果target大,那么肯定在下面,row+=1,如果比他小就王座便开始找,如果target大,就再往下找,持续.

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """二维的二分搜索"""
        if not matrix:
            return False
        raws = len(matrix)
        cols = len(matrix[0])

        raw = 0
        col = cols - 1

        while 0 <= raw < raws and 0 <= col < cols:
            print(matrix[raw][col])
            if matrix[raw][col] < target:
                raw += 1
            elif  matrix[raw][col] > target:
                col -= 1
            else:
                return True
        return False


print(Solution().searchMatrix(matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target=23))