#
# def cur_max(nums):
#     res=0
#     max_=0
#     i=0
#     n=len(nums)
#     while i < n :
#         if nums[i]==0:
#             max_=max(max_,res)
#             res=0
#             i+=1
#         else:
#             res+=nums[i]
#             i+=1
#     return max_
#
#
#
# # n = int(input())
# # W = [int(i) for i in input().split()]
# # Order = [int(i) for i in input().split()]
#
#
#
# n=5
# W=[3,2,4,4,5]
# Order=[4,2,5,3,1]
# res = 0
# sum_forword = []
# for i in W:
#     res += i
#     sum_forword.append(res)
# print(sum_forword)
# for k in Order:
#     temp=sum_forword[k-1]
#     W[k-1]=0
#     sum_forword[k-1]=0
#     while k<n and sum_forword[k]!=0:
#         sum_forword[k]-=temp
#         k+=1
#     print(sum_forword)
#
#

"""

5
3 2 4 4 5 
4 2 5 3 1
"""


def cur_max(nums):
    res = 0
    max_ = 0
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == 0:
            max_ = max(max_, res)
            res = 0
            i += 1
        else:
            res += nums[i]
            i += 1
    return max(max_,res)


n = int(input())
W = [int(i) for i in input().split()]
Order = [int(i) for i in input().split()]
# n=5
# W=[3,2,4,4,5]
# Order=[4,2,5,3,1]
res = 0
for k in Order:
    W[k - 1] = 0
    print(cur_max(W))