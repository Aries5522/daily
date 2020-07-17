"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

翻转链表,思路一定要清晰



正常的反转链表

pre->cur->c

temp=cur.next
cur.next=pre
pre,cur=cur,temp

迭代

这一题稍微变化

"""
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None



class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:
            return head
        k=1
        cur=head
        res=ListNode(None)
        res.next=cur
        while cur:
            if m==1:
                node1=res
            elif k==m-1:
                node1=cur
            if k>=m and k <n:
                if k==m:
                    node2=pre=ListNode(cur.val)
                    cur=cur.next
                else:
                    temp1=cur.next
                    cur.next=pre
                    pre,cur=cur,temp1
            elif k==n:
                node2.next=cur.next
                cur.next=pre
                node1.next=cur
                break
            else:
                cur=cur.next
            k+=1
        # P=res.next
        return res.next
nums=[1,2,3,4,5]
p=head=ListNode(1)
for i in range (1,len(nums)):
    node=ListNode(nums[i])
    head.next=node
    head=head.next
print(Solution().reverseBetween(p,2,4))