
'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1
'''

##定义一个辅助栈实现,空间换时间,这个辅助栈单调递减.进来一个教大的,那么前面那个小的就都要走.

"""
https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
"""

class MaxQueue:

    def __init__(self):
        self.res = []
        self.temp = []

    def max_value(self) -> int:
        if self.res == []: return -1
        return self.temp[0]

    def push_back(self, value: int) -> None:
        self.res.append(value)
        if self.temp == []:
            self.temp.append(value)
        else:
            while self.temp != []:
                if value > self.temp[-1]:
                    self.temp.pop(-1)
                else:
                    break
            self.temp.append(value)

    def pop_front(self) -> int:
        if self.res != []:
            if self.res[0] == self.temp[0]:
                self.temp.pop(0)
        else:
            return -1
        return self.res.pop(0)


