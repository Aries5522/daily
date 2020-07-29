class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A=[]
        self.B=[]
    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B:
            self.B.append(x)
        elif x<=self.B[-1]:
            self.B.append(x)
    def pop(self) -> None:
        k=self.A.pop()
        if k==self.B[-1]:
            self.B.pop()
        return k

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        if self.B:
            return self.B[-1]
        else:return None
