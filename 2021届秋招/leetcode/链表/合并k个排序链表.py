# Definition for singly-linked list.

"""
这里用优先队列

heapq用法

nums=[1,3,4,6]
item=[]
for i in nums:
    heapq.heappush(item,nums)#吧nums中的都push进优先队列
while item:
    print(heapq.heappop())##从小到大弹出
这里主要是第一次把每个链表的第一个值放进去维护一个优先队列,后面看第一个取出来的是谁
然后记住index,然后让lists[index]往后走一个,一直到全部走完.


"""
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
###两两合并之后
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # def mergeLists(l1,l2):
        #     res=temp=ListNode(None)
        #     while l1 and l2:
        #         if l1.val<=l2.val:
        #             temp.next=ListNode(l1.val)
        #             l1=l1.next
        #         else:
        #             temp.next=ListNode(l2.val)
        #             l2=l2.next
        #         temp=temp.next
        #     if l1:
        #         temp.next=l1
        #     if l2:
        #         temp.next=l2
        #     return res.next
        # if not lists:return None
        # n=len(lists)
        # res=lists[0]
        # for i in range(1,n):
        #     k=mergeLists(res,lists[i])
        #     # print(k)
        #     res=k
        # return res
        ##两个两个合并会超时

        ##下面采用优先队列
        import heapq
        heap = []
        n = len(lists)
        ans = res = ListNode(None)
        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))##元组之间大小比较,按照第一位先来,构建val和index组
                lists[i] = lists[i].next
        while heap:
            val, index = heapq.heappop(heap)
            node = ListNode(val)
            res.next = node
            res = res.next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next
        return ans.next



