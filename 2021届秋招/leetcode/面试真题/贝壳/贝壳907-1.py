n, m = map(int, input().split())
A = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]

import math

# for i in range(n):
#     if A[i] > left:
#         res += min(P[0:i + 1]) * math.ceil((A[i] - left) / m)
#         left = math.ceil((A[i] - left) / m) * m - A[i]
#     else:
#         res += 0
#         left -= A[i]
# print(res)


# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# p=list(map(int,input().split()))

res=0
if A[0]%m==0:
    res+=P[0]*(A[0]//m)
    remain=0
else:
    res+=P[0]*(A[0]//m+1)
    remain=(A[0]//m+1)*m-A[0]

cur=P[0]
for i in range(1,n):
    if cur>P[i]:
        cur=P[i]
    num=A[i]-remain
    if num%m==0:
        res+=cur*(num//m)
        remain=0
    else:
        res+=cur*(num//m+1)
        remain=(num//m+1)*m-num
    #print(res)
print(res)


"""
4 10
11 1 1 10
5 1 1000 5
"""
