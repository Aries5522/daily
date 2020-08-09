from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < cols):
                return 0
            elif grid[i][j] == "0":
                return 0
            else:
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
                return 1

        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                res += dfs(i, j)
        return res


print(Solution().numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
