class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


class chain_op:
    def __init__(self):
        self.cur_node = None

    def print_node(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n==1:return 0
        elif n==0:return -1
        else:
            head=p1=ListNode(0)
            for i in range(1,n):
                node=ListNode(i)
                p1.next=node
                p1=p1.next
            p1.next=head
        # chain_op().print_node(head)
        k=0
        while p1.next!=p1:
            if k==m-1:
                p1.next=p1.next.next
                k=0
            k+=1
            p1=p1.next
        return p1.val

print(Solution().LastRemaining_Solution(n=5,m=3))