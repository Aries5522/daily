"""
138. 复制带随机指针的链表

https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-by-leetcod/
具体思路可以看上面解答,第三个思路


第一遍走复制好节点放在当前节点后面
第二遍走 把每个random指针给赋值好
第三遍走只留下后面保存的节点

"""



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if  not head:return head
        res=pre=Node(1)
        pre.next=head
        cur=head
        random_run=head
        split_run=head
        while cur:
            temp=cur.next
            node=Node(cur.val)
            cur.next=node
            node.next=temp
            cur=temp
        while random_run:
            if random_run.random:
                random_run.next.random=random_run.random.next
            random_run=random_run.next.next
        while  pre.next:
            pre.next=pre.next.next
            pre=pre.next
        return res.next