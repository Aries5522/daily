"""
答案搜索的oneline solution.
直接用filter lambda函数
本来自己用的哈希表
"""

# -*- coding:utf-8 -*-
# class Solution:
#     # 返回对应char
#     def __init__(self):
#         self.data={}
#     def FirstAppearingOnce(self):
#         if not self.data:return "#"
#         for (k,v) in self.data.items():
#             if v==1:
#                 return k
#         return "#"
#         # write code here
#     def Insert(self, char):
#         if char not in self.data:
#             self.data[char]=1
#         else:self.data[char]+=1
#         # write code here


class Solution:

    def __init__(self):
        self.s = ""

    def FirstAppearingOnce(self):
        res = list(filter(lambda c: self.s.count(c) == 1, self.s))
        return res[0] if res else "#"

    def Insert(self, char):
        self.s += char

solu=Solution()
for i in "google":
    solu.Insert(i)
    print(solu.FirstAppearingOnce())
