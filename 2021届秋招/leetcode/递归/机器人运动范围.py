


"""


地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 深度优先搜索

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def movingCount(self, threshold, rows, cols):
        res = 0
        record=[[0]*cols for _  in range(rows)]
        def con(n):
            k = 0
            while n >= 10:
                k += n % 10
                n = n // 10
            k += n
            return k
        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and record[i][j] == 0 and con(i) + con(j) <= threshold: ##满足条件的值1
                record[i][j] = 1
            else:
                return False   ##不满足条件的及时返回,不然会遍历所有点,
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
        dfs(0, 0)
        print(record)
        for i in record:
            res+=sum(i)
        return res

print(Solution().movingCount(10,1,100))
