'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/

我们比较可以得知,转化为字符串比较相加比较大小大小就好了.
'''
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        help_list = list(map(lambda x: str(x), nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) ):
                if help_list[i] + help_list[j] > help_list[j] + help_list[i]:
                    help_list[i], help_list[j] = help_list[j], help_list[i]
        return ''.join(help_list)


print(Solution().minNumber([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]))
