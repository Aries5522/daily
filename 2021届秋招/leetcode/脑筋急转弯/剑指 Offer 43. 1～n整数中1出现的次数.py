"""


输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

我觉得很难,这一题,很细节

找规律
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/c-cong-ge-wei-bian-li-dao-zui-gao-wei-yi-ci-qiu-ji/


"""


class Solution:
    def countdigitOne(self, n):
        res = 0
        i = 1
        while (n // i) != 0:
            high = n // (i * 10)
            cur = (n -high*10*i)//(i)
            lower = n - high * 10 * i - cur  * i
            if cur == 0:
                res += high * i + 0
            if cur == 1:
                res += high * i + lower + 1
            if cur > 1:
                res += (high * i + i)
            i=i*10
        return res


print(Solution().countdigitOne(13))