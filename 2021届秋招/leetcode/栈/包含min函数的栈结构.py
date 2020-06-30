'''

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中
，调用 min、push 及 pop 的时间复杂度都是 O(1)。

https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/

##开始想的太复杂了,和队列一样,但是栈有先进后出来的特点,所以辅助栈中,碰到更小的就
放在第一位,没碰到就不管了.(因为总会先出去,不影响结果)
辅助栈也是单调不减的.

'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.help_stack=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.help_stack==[]:
            self.help_stack.append(x)
        else:
            if x<=self.help_stack[0]:
               self.help_stack.insert(0,x)
    def pop(self) -> None:
        k=self.stack.pop(-1)
        if k==self.help_stack[0]:
            m=self.help_stack.pop(0)
        return k
    def top(self) -> int:
        if len(self.stack)==0:
            return None
        return self.stack[-1]
    def min(self) -> int:
        print(self.help_stack)
        return self.help_stack[0]

