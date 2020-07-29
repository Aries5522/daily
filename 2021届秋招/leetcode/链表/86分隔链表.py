"""

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

https://leetcode-cn.com/problems/partition-list/



先找到链表中出现cur大于或者等于x,pre是小于x的
然后遍历后面的,如果小于x的就让pre=cur.next,并且吧cur节点
放到前面找到的空位中,然后别忘记让cur=temp继续更新


我自己写的题解
https://leetcode-cn.com/problems/partition-list/solution/dan-tiao-lian-biao-zheng-chang-si-lu-by-aries-5/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return head
        # res=pre=ListNode(None)
        res = pre = ListNode(x - 1)  # 这样设置可以使得如果head节点大于等于x也成立
        res.next = cur = head
        while cur:
            if cur.val < x:
                pre = pre.next
                cur = cur.next
            else:
                node0 = pre
                node1 = cur
                break
        if cur:  ##特例[1] x=2,过不了.
            pre = pre.next
            cur = cur.next
        else:
            return head
        while cur:
            if cur.val >= x:
                cur = cur.next
                pre = pre.next
            else:
                temp = cur.next
                pre.next = temp
                node0.next = cur
                cur.next = node1
                node0 = cur
                cur = temp
        return res.next
