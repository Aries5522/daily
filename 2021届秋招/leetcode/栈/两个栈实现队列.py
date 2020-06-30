# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res=[]
    def push(self, node):
        self.res.append(node)
        # write code here
    def pop(self):
        if self.res:
            k=self.res.pop(0)
            return k
        else:return []
        # return xx



"""
python中列表可以直接实现
"""