"""

简单题核心是,开始的pre要设置为None而不是ListNode(None)
记住!!!!!

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        cur=head
        while cur:
            # print(cur)
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre