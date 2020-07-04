"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。


注意有负数的情况,正常来说没有负数的时候
a^b(a和b求异或可以得到正常位数相加的结果)
a&b<<1(a和b取与得到进位结果然后左移动一位)
然后这俩相加得到结果,但是相加的过程又要用上上述过程直到没有进位,那么全正数做法是

"""

class Solution1:
    def add_zheng(self,a,b):
        while b!=0:
            a,b=a^b,(a&b)<<1
        return a

print(Solution1().add_zheng(3,2))
###如果出现负数的话
"""
由于负数是以补码的形式出现也就是说
如果出现负数与0xffffffff相与,那么前面的负数位会被抵消,变为正数
正数与0xffffffff相与不变

然后和刚才一样的操作但是要注意(a & b) << 1可能会越界,所一要和x取与

最后的结果如果是正数的话那么保持,如果是负数,那么要还原成补码,与x取异或,然后去反




"""
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


print(Solution().add(-1,2))