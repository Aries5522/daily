strings = input().split(";")
# strings = "I need book.;I need book 2.".split(";")
s1 = strings[0]
s2 = strings[1]


def minDistance(word1: str, word2: str) -> int:
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    # 第一行
    for j in range(1, n2 + 1):
        dp[0][j] = dp[0][j - 1] + 1
    # 第一列
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i - 1][0] + 1
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    # print(dp)
    return dp[-1][-1]

s3 = ''
s4 = ''
for i in s1:
    if i in [".", ",", "!"]:
        s3 += " ! "
    elif i == "?":
        s3 += " ? "
    else:
        s3 += i
for i in s2:
    if i in [".", ",", "!"]:
        s4 += " ! "
    elif i == "?":
        s4 += " ? "
    else:
        s4 += i
s1_list = [i.lower() for i in s3.split()]
s2_list = [j.lower() for j in s4.split()]
n1 = len(s1_list)
n2 = len(s2_list)
res = [0, 0]
res[1] = n2
dp = [[0] * n1 for _ in range(n2)]

print(s1_list, s2_list)
res[0] = 0
print((res[0], res[1]))

"""
I need book.???;I need book ?2.
"""
