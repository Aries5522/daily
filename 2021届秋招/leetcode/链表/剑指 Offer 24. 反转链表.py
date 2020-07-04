"""

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。



"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None    ##创建一个空
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
            # cur.next,pre,cur=pre,cur,cur.next
        return pre