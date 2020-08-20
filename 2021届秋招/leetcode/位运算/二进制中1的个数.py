# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        res = 0
        k = 0

        while n > 0:
            res += n % 2
            n = n // 2
        if n < 0:
            n = -n - 1
            while n > 0:
                k += n % 2
                n = n // 2
            res = 32 - k
        return res

        # write code here


print(Solution().NumberOf1(n=-2147483648))
