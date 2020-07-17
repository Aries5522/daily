"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，
向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
​矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中
的第一行第二个格子之后，路径不能再次进入该格子。

https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?tpId=13&&tqId=11218&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


一定要注意dfs的时候是不是需要return,一定要注意
"""

import copy

class Solution:
    def hasPath(self, matrix, rows, cols, path):

        self.visited = [[0] * cols for _ in range(rows)]
        p1 = copy.deepcopy(self.visited)
        matrix = [list(matrix)[i * cols:i * cols + cols] for i in range(rows)]
        print(matrix)
        path = list(path)
        p = copy.deepcopy(path)

        def dfs(i, j, path):
            if i < 0 or i >= rows or j < 0 or j >= cols or self.visited[i][j] == 1 or matrix[i][j] != path[0]:
                return
            self.visited[i][j] = 1
            k = path.pop(0)
            if not path:
                return True
            else:
                if dfs(i + 1, j, path):
                    return True
                if dfs(i - 1, j, path):
                    return True
                if dfs(i, j + 1, path):
                    return True
                if dfs(i, j - 1, path):
                    return True
                path.insert(0, k)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    if dfs(i, j, path):
                        return True
                    else:
                        self.visited = p1
        return False


print(Solution().hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))
import collections

collections.defaultdict
