from collections import Counter


class Solution:
    def minWindow(self, s, t):
        hash_t = Counter(t)
        cnt = len(hash_t)
        c, j, res = 0, 0, ''
        for i in range(len(s)):
            if hash_t[s[i]] == 1: c += 1
            hash_t[s[i]] -= 1
            while hash_t[s[j]] < 0 and j < i:
                hash_t[s[j]] += 1
                j += 1
            if c == cnt:
                if not res or len(res) > i - j + 1:
                    res = s[j:i + 1]
        return res


#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         dict_t = Counter(t)
#         dict_s = Counter(s)
#         print(dict_s, dict_t)
#         for k, v in dict_t.items():
#             if dict_s[k] < v: return ""
#         i, j, n, max_l = 0, 0, len(s), len(s)
#
#         def OK(dict):
#             flag = True
#             for k, v in dict.items():
#                 if v > 0:
#                     flag = False
#             return flag
#
#         while 0 <= i < n and 0 <= j < n:
#             while not OK(dict_t) and i < n:
#                 if s[i] in dict_t:
#                     dict_t[s[i]] -= 1
#                 i += 1
#             while OK(dict_t) and j < i:
#                 if i - j <= max_l:
#                     res = (j, i)
#                     max_l = i - j
#                 if s[j] in dict_t:
#                     dict_t[s[j]] += 1
#                 j += 1
#         return s[res[0]:res[1]]


print(Solution().minWindow(s= "ADOBECODEBANC", t = "ABC"))
