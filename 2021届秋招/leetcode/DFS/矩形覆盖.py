# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 0: return 0
        global res
        res=0
        def dfs(number, path):
            if number == 0:
                global res
                res += 1
                return
            if number < 0:
                return
            for i in ["竖", "2横"]:
                if i == "竖":
                    dfs(number - 1, path + i)
                if i == "2横":
                    dfs(number - 2, path + i)
        dfs(number, "")
        return res


print(Solution().rectCover(4))
