# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        visited={}
        head=pHead
        def dfs(head):
            if not head:return None
            if head in visited:
                return visited[head]
            else:
                copy_node=RandomListNode(head.label)
                visited[head]=copy_node
                copy_node.next=dfs(head.next)
                copy_node.random=dfs(head.random)
                return copy_node
        return dfs(head)
        # write code here


#简单python解法,
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        import copy
        return copy.deepcopy(pHead)
#正常解法:dfs,图搜索,设置哈希表 没有访问的就创建新节点,保存节点到visited,然后返回该节点,碰到访问的节点就直接返回哈希表中存储的节点