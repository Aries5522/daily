
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
def print_(node):
    res=[]
    i=0
    while node and i<10:
        res.append(node.val)
        i+=1
    print(res)

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        res=ListNode(None)
        res.next=head
        cur=head
        node2=res
        i=1
        while cur:
            if i==1:
                node1=pre=ListNode(cur.val)
                cur=cur.next
            elif i==k:
                temp=cur.next
                cur.next=pre
                node1.next=temp
                node2.next=cur
                i=0
                node2=node1
                cur=temp
            else :
                third=cur.next
                cur.next=pre
                pre,cur=cur,third
            i+=1
        node2.next=node1
        print_(res.next)
        return res.next


nums=[1,2,3,4,5]
p=head=ListNode(1)
for i in range (1,len(nums)):
    node=ListNode(nums[i])
    head.next=node
    head=head.next
print(Solution().reverseKGroup(p,3))