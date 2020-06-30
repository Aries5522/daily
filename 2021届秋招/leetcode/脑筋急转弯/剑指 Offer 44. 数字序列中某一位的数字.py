"""

数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

先找对应的数的位数
然后找到这个数是当前位数中的第几个数

然后确认是这个i位数中的第几个数
"""

# class Solution:
#     def findNthDigit(self, n: int) -> int:
#         str_=''
#         for i in range(n+1):
#             str_=str_+str(i)
#             if len(str_)>n:
#                 return int(str_[n])
##暴力肯定超时

class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 0
        if n < 10:
            return n
        temp = [int(9 * i * 10 ** (i - 1)) for i in range(0, 10)]
        while True:
            if n <= sum(temp[:i]):
                break
            i += 1
        print(temp)
        i -= 1
        print(i)
        t = (n - (sum(temp[0:(i)])+1)) // i
        p = (n - (sum(temp[0:(i)])+1)) % i
        num = 10 ** (i-1)  + t
        return int(str(num)[p])


print(Solution().findNthDigit(191))
