class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput): return []
        import heapq
        data = [-x for x in tinput]
        heap_ = data[:k]
        heapq.heapify(heap_)
        for i in range(k, len(data)):
            heapq.heappushpop(heap_, data[i])
        res = []
        while heap_:
            res.append(-heapq.heappop(heap_))
        return res[::-1]


print(Solution().GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
