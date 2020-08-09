"""
将字符串分割开来,规则是
任何两个子串不能有同样的数字

思路是先记录每个字母出现的最大index处,如果当前字母前面所有的最大index都小于当前index索命在此处可以分割,记录分割点.

"""

def main(s):
    n = len(s)
    index = [0] * n
    s = list(s)
    for i in range(n):
        index[i] = [k for k, v in enumerate(s) if v == s[i]][-1]
    start = 0
    print(index)
    index_record = []
    for i in range(0, n - 1):
        if i >= max(index[start:i + 1]):
            index_record.append(i)
            start = i
    print(index_record)


main("abcdeafgasda")
