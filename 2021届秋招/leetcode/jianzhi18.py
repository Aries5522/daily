# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @staticmethod
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
            p=ListNode(-1)
            p.next=head
            q=p
            while p:
                if p.next.val==val:
                    p.next=p.next.next
                    break
                p=p.next
            p=p.next
            return q.next

print(Solution.deleteNode())

