"""
剑指 Offer 48. 最长不含重复字符的子字符串

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



哈希表加滑窗
感觉写复杂了

https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
"""


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len=0
#         temp=set()
#         n=len(s)
#         temp_len=0
#         i=0
#         j=0
#         while i<n:
#             # if j==n-1:
#             #     return max_len
#             while j < n:
#                 if s[j] not in temp:
#                     temp.add(s[j])
#                     j+=1
#                 else:
#                     temp=set()
#                     if j-i>max_len:
#                         max_len= j-i
#                     i+=1
#                     j=i
#                     break
#             if j==n:
#                 return max(max_len,len(temp))
#         return max(max_len,len(temp))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<=1:return n
        max_len=0
        for i in range(n):
            for j in range(i+1,n+1):
                if len(set(s[i:j]))==j-i and j-i>max_len:
                    max_len=j-i
        return max_len

print(Solution().lengthOfLongestSubstring(s="au"))