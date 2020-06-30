'''

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

遍历一遍,计数
遍历哈希表,返回
'''

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        hash_map={}
        for i in list(s):
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        for k in hash_map:
            if hash_map[k]==1:
                return k
        return ' '