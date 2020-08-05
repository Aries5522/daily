class Solution:
    def rob(self, root):
        a = self.helper()
        return max(a)

    def helper(self, root):
        a = [0] * 2  ##a[0]表示抢劫该节点,a[1]表示不抢劫这个节点
        if not root:
            return [0, 0]
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            a[0] = root.val + left[1] + right[1]
            a[1] = max(left[0] + left[1]) + max(right[1] + right[0])
        return a
