'''

61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

排序之后
第一遍看有没有不为0的对子
第二遍如果最大值减最小非零值大于=5 就不行,否则就可以
'''

from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(4):
            if nums[i]==nums[i+1]!=0:
                return False
        for i in range(5):
            if nums[i]!=0:
                k=nums[-1]-nums[i]
                break
        if k>=5:
            return False
        else:return True