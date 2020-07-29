
"""

142:环形链表2
https://leetcode-cn.com/problems/linked-list-cycle-ii/


判断环形链表是不是会相交

快慢指针,如果两个链表相交,那么让快的指针指向头节点
两个指针速度一样往前走,碰面的地方就是交点.


"""







# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:return None
        if head==head.next:return head
        slow=fast=head
        i=0
        meet=False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                meet=True
                break
        if slow==fast and meet: ###为了判断是哪一种情况跳出循环的,证明确实相遇之后,而不是因为fast到头了.
            fast=head
        else:
            return None
        while fast:
            if fast==slow:
                return fast
            else:
                fast=fast.next
                slow=slow.next
                i+=1
