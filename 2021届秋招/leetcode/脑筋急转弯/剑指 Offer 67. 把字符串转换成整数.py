"""
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

 

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，
请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

很无聊的题目


"""


class Solution:
    def strToInt(self, str: str) -> int:
        i = 0
        n = len(str)
        temp=list(str)
        while temp and temp[0]==" ":
            temp.pop(0)
        k=len(temp)
        if k==0:
            return 0
        if temp[0] not in ["-","+","0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return 0
        else:
            flag=""
            res = ""
            if temp[0] in ["-","+"]:
                flag=temp[0]
            elif temp[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                res=temp[0]
            i=1
            while i<k and temp[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                res+=temp[i]
                i+=1
            if len(res)==0:
                return 0

            if -2147483648 <= int(flag+res) <= 2147483647:
                return int(flag+res)
            elif int(flag+res)  >= 2147483648:
                return 2147483647
            elif int(flag+res) < -2147483648:
                return -2147483648

print(Solution().strToInt("-91283472332"))









