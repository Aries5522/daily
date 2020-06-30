'''
类似牛客上孩子们的游戏那题
但是用循环链表解法会超时

https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/

约瑟夫环的问题

还有递归解法



\数学解法:


解题思路
这个游戏里叫击鼓传花，西方也有叫热土豆。可通过严格的数学推导直接计算得出。但我们用程序来全真模拟才更真实。

生成一个0、1、…、n-1的列表，初始索引i=0
传递m次，意味着从i开始偏移m得到新索引i=i+m-1，考虑m可能大于当前列表长度，所以要对列表长度求模余
从列表中pop出一个值后，实际上下一次偏移的初始索引仍然是当前pop掉的那个（因为后边的值都前移了一位），所以继续用i=i+m-1迭代新的索引，当然也要用新的列表长度求模余
直至列表长度为1，返回最后剩下的数字。
由于列表要执行pop操作 n-1次，而每次pop(i)是平均O(n)复杂度，所以总的时间复杂度是O(n^2)

作者：luanhz
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/pythonquan-zhen-mo-ni-by-luanz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

#循环链表解法
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        temp=[i for i in range(n)]
        if n==0:return -1
        if n==1:return 0
        root=head=ListNode(0)
        if m==1:return n-1
        for i in range(1,n):
            node=ListNode(i)
            root.next=node
            root=root.next
        root.next=head
        i=1
        while head.next!=head:
            if i==m-1:
                head.next=head.next.next
                i=1
            else:
                i+=1
            head=head.next
        return head.val



#数学解法
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        i=0
        temp=[i for i in range(n)]
        while len(temp)!=1:
            i=(i+m-1)%len(temp)
            temp.pop(i)
        return temp[0]