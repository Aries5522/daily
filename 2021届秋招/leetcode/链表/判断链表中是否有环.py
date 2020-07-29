"""
正常是快慢指针,快的一直走,
如果快的最终快的追上慢的就证明存在环,不然不存在


另外看到一个思路,如果下一个节点不为None就让当前节点
跳过下一个节点,会破坏链表结构
但是神奇的是不会破坏环的结构
这样一直删除下去如果出现cur=cur.next就证明有环
否则会走穿
然后返回没有环

"""




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:return False
        if head.next==head:
            return True
        slow=fast=head
        while fast and  fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False

        # while head:
        #     if head==head.next:
        #         return True
        #     if head.next!=None:
        #         head.next=head.next.next
        #     head=head.next
        # return False
