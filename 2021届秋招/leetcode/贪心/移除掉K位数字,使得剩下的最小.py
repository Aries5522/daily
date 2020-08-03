"""
考虑每一位数字的去留,如果当前数字比后面那一位大,去除他就会变小,就应该去掉,否则就留下
类似于栈,往里面放,来一个新的和top比较,如果新的大就留下,否则就弹出.

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        remain=n-k
        if n <= k: return "0"
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'


print(Solution().removeKdigits("10200", k=1))
