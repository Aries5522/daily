

"""
主要是要记录四个节点


"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


def make_List(nums):
    res = head = ListNode(None)
    for i in nums:
        node = ListNode(i)
        head.next = node
        head = head.next
    return res.next



class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return head
        if m == n: return head
        res = pre = ListNode(None)
        pre.next = head
        cur = head
        i = 1
        while cur:
            if i == m:
                node1 = pre
                node2 = cur
                move_pre = cur
                cur = cur.next
                i += 1
                while i > m and i <= n:
                    temp = cur.next
                    cur.next = move_pre
                    move_pre, cur = cur, temp
                    i += 1
                node2.next = cur
                node1.next = move_pre
            elif i < m:
                pre = pre.next
                cur = cur.next
                i += 1
            else:
                cur = cur.next
                i += 1
        return res.next


nums = [1, 2, 3, 4, 5]
head = make_List(nums)


print_(Solution().reverseBetween(head, 2, 4))

