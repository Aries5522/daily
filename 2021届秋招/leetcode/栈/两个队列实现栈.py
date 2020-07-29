"""

两个栈实现一个队列,一直保持一个栈空.也就是说push的时候要往非空的那个queen放元素

pop操作就是把非空的那个元素往空的那个转移,只剩下最后一个的时候,输出那个就是栈顶元素

top的时候一样但是要保存下来然后还是要存下来这个值,不能直接pop出去.

"""



class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queen1 = []
        self.queen2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.queen1 and not self.queen2:
            self.queen1.append(x)
        else:
            if self.queen1:
                self.queen1.append(x)
            else:
                self.queen2.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queen1:
            while len(self.queen1) != 1:
                self.queen2.append(self.queen1.pop(0))
            return self.queen1.pop(0)
        else:
            if self.queen2:
                self.queen1, self.queen2 = self.queen2, self.queen1
                return self.pop()
            else:
                return None

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queen1:
            while len(self.queen1) != 1:
                self.queen2.append(self.queen1.pop(0))
            k = self.queen1.pop(0)
            self.queen2.append(k)
            return k
        else:
            if self.queen2:
                self.queen1, self.queen2 = self.queen2, self.queen1
                return self.top()
            else:
                return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queen1 and not self.queen2:
            return True
        else:
            return False

