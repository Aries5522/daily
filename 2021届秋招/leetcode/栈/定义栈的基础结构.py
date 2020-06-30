"""

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

"""
##空间换时间,定义辅助栈

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []
        self.stack = []

    def push(self, node):
        self.res.append(node)
        if self.stack == []:
            self.stack.append(node)
        else:
            if node < self.stack[-1]:
                self.stack.append(node)
        # write code here

    def pop(self):
        if self.res[-1] == self.stack[-1]:
            self.stack.pop(-1)

        return self.res.pop(-1)

        # write code here

    def top(self):
        return self.res[-1]
        # write code here

    def min(self):
        return self.stack[-1]
        # write code here