"""
一般来说做不出来 感觉


dfs做法


交换两者顺序

确定搜索
判断搜索终止条件
x到倒数第二位就终止

因为最后一位确定了
如果不终止的话就
跳下一位

一直到跳出为止然后开始回溯


"""


# from typing import List
#
#
# class Solution:
#     def permutation(self, s: str) -> List[str]:
#         res = []
#         c = list(s)
#
#         def dfs(x):
#             if x == len(c) - 1:
#                 res.append("".join(c))
#             else:
#                 dict = set()
#                 for i in range(x, len(c)):
#                     if c[i] in dict:
#                         continue
#                     else:
#                         dict.add(c[i])
#                         c[i], c[x] = c[x], c[i]
#                         dfs(x + 1)
#                         c[i], c[x] = c[x], c[i]
#
#         dfs(0)
#         return res


# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        ss = "".join(sorted(list(ss)))
        res = []
        n = len(ss)
        record = [0] * n

        def dfs(lenth, record, path):
            if lenth == n:
                res.append(path)
                return
            for i in range(n):
                if record[i]==0:
                    if i != 0 and ss[i]== ss[i - 1] and record[i - 1]: ##代表当前字母和前面字母一样,并且前面的字母已经被用了,这里就剪枝
                        continue
                    record[i] = 1
                    dfs(lenth + 1, record, path + ss[i])
                    record[i] = 0
        dfs(0, record, "")
        return res


print(Solution().Permutation("aaAb"))
