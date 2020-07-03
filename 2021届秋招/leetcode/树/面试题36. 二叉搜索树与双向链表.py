"""

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



思路就是中序遍历的时候修改,节点指向
递归实现

"""



# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.pre=Node(None)   #创建空的节点
        self.head=Node(None)
        self.is_first=True  #是不是第一个节点

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            print(self.pre)
            if self.is_first:
                self.head=node    ##是第一个就让他是head
                self.pre=node
                self.is_first=False
            else:
                self.pre.right=node   ##不是的话就让pre右边指向他
                node.left=self.pre    ## 他的左边指向pre
                self.pre=self.pre.right  ## 然后pre往前继续走
            print(node.val)
            dfs(node.right)

        dfs(root)
        # print("111")
        # print(self.pre.val)
        self.pre.right=self.head    ##递归完成之后 pre目前是最后一个,让他右边指向head
        self.head.left=self.pre# 让head的左边指向尾巴
        return self.head
