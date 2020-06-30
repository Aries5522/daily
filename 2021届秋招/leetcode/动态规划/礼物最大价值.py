
'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
动态规划

第一列和第一排的数字很容易知道
依次填第二排的数字
依次第三排...

'''
class Solution:
    def maxValue(self, grid) -> int:
        m = len(grid)
        self.grid = grid
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        print(dp)
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        for j in range(1, m):
            dp[j][0] = grid[j][0] + dp[j - 1][0]
        print(dp)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        print(dp)
        return (dp[m - 1][n - 1])


gift = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(Solution().maxValue(grid=gift))
