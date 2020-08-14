class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2Node(nums):
    root = cur = ListNode(None)
    for i in nums:
        node = ListNode(i)
        cur.next = node
        cur = cur.next
    return root.next
def print_(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
        if len(res) > 15:
            break
    print(res)

def kgropu_reverse(head, k):
    if k == 1: return head
    res = pre=ListNode(None)
    res.next = head
    len_ = 0
    cur = head
    while cur:
        len_ += 1
        cur = cur.next
    cur = head
    # print(len_)
    for i in range(len_ // k):
        for j in range(k - 1):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        pre = cur
        cur = cur.next
    return res.next


print_(kgropu_reverse(list2Node([1, 2, 3, 4, 5]), 3))
