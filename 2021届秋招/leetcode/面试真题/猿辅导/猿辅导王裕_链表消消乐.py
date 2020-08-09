class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def list2ListNode(nums):
    if not nums:
        return None
    else:
        n=len(nums)
        res=head=ListNode(None)
        for i in range(n):
            node=ListNode(nums[i])
            head.next=node
            head=head.next
        return res.next

def ListNode_xiaoxiaole(head):
    stack=[]
    while head:
        while stack and head.val==stack[-1]:
            head=head.next
            if head.val!=stack[-1]:
                stack.pop(-1)
        stack.append(head.val)
        head=head.next
    return list2ListNode(stack)

print(ListNode_xiaoxiaole(list2ListNode([1,2,3,3,3,2,1,4])))