from collections import Counter


def count(s):
    if len(s) <= 1: return 0
    n = len(s)
    temp = 1
    i = 1
    data = []
    while i < n:
        while i < n and s[i] == s[i - 1]:
            temp += 1
            i += 1
        data.append(temp)
        temp = 1
        i += 1
    if s[n - 1] != s[n - 2]:
        data.append(temp)
    # print(data)
    if len(data) <= 1:
        return 0
    res = 0
    for j in range(1, len(data)):
        res += min(data[j], data[j - 1])
    return res


print(count("00110"))
