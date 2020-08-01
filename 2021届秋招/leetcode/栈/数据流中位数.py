"""
优先队列,放的复杂度log(n)
取的复杂度是O(1)合起来O(logn)


两个堆,一个存一半,维持平衡
"""



import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap=[]##存取负数
        self.min_heap=[]##python默认小顶堆
    def addNum(self, num: int) -> None:
        if len(self.max_heap)==len(self.min_heap):   ##先放小顶堆,再抽出来放大顶堆,再拿回来放小顶堆.太麻烦了,可以放大堆,然后放小堆就行了
            k=heapq.heappushpop(self.max_heap,-1*num)
            # heapq.heappush(self.min_heap,-1*k)
            k1=heapq.heappushpop(self.min_heap,-1*k)
            heapq.heappush(self.max_heap,-1*k1)
        else:
            k=heapq.heappushpop(self.min_heap,num)
            # heapq.heappushpop(self.max_heap,-1*k)
            k1=heapq.heappushpop(self.max_heap,-1*k)
            heapq.heappush(self.min_heap,-1*k1)
    def findMedian(self) -> float:
        if len(self.max_heap)>len(self.min_heap):
            return -1*self.max_heap[0]
        else:
            return (-1*self.max_heap[0]+self.min_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap=[]##存取负数
        self.min_heap=[]##python默认小顶堆
    def addNum(self, num: int) -> None:
        if len(self.max_heap)==len(self.min_heap):   ##先放小顶堆,再抽出来放大顶堆,再拿回来放小顶堆.
            k=heapq.heappushpop(self.min_heap,num)
            heapq.heappush(self.max_heap,-k)
        else:
            k=heapq.heappushpop(self.max_heap,-num)
            heapq.heappush(self.min_heap,-k)
    def findMedian(self) -> float:
        # print(self.max_heap,self.min_heap)
        if len(self.max_heap)>len(self.min_heap):
            # k=heapq.heappop(self.min_heap)
            # heapq.heappush(self.min_heap,k)
            return -self.max_heap[0]
        else:
            return (-1*self.max_heap[0]+self.min_heap[0])/2