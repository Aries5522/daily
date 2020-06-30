class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class chain_op:
    def __init__(self):
        self.cur_node = None

    def print_node(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next


nums = [1, 2, 3, 3, 4, 4,5]
p = p1 = ListNode(x=0)
for i in nums:
    temp_node = ListNode(i)
    p.next = temp_node
    p = p.next
input = p1.next


class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None:
            return None
        p1 = p2 =res= ListNode(-1)

        p1.next=pHead
        temp = set()
        while pHead.next:
            if pHead.val == pHead.next.val:
                temp.add(pHead.val)
            pHead = pHead.next
        while p1.next:
            if p1.next.val not in temp:
                p1=p1.next
                p2=p2.next
            else:
                while p1.next and p1.next.val in temp:
                    p1=p1.next

                p2.next=p1.next
        return res.next

m=Solution().deleteDuplication(pHead=input)
chain_op().print_node(m)
