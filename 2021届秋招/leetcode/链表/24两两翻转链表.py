"""
思路是要同时记录四个节点
A-->B-->C-->D

node=A
先记录D节点为temp
C为cur节点
B为pre节点

然后C.next=B
    B.next=D
    node.next=C
    然后这一步关键
    记录下一个node位置
    node=pre
    然后cur变到下一个
    cur=Temp
    但是pre节点不动




"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        res = pre = node = ListNode(None)
        pre.next = head
        cur = head
        i = 1
        while cur:
            if i % 2 == 0:
                temp = cur.next  # 记录D
                pre.next = temp  # B-->D
                cur.next = pre  # C-->B
                node.next = cur  # A-->C
                node = pre  ##更新node
                cur = temp  ##更新cur
                i += 1
            else:
                i += 1
                cur = cur.next
                pre = pre.next
        return res.next
