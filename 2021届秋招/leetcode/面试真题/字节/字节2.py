N = int(input())
nums = [int(i) for i in input().split()]
L = [-1] * N
R = [-1] * N
i = 0
while i < N:
    j = i - 1
    if j >= 0:
        while j >= 0 :
            if nums[j] > nums[i]:
                L[i] = j + 1
                break
            else:
                j -= 1
    if L[i] == -1:
        L[i] = 0
    k = i + 1
    if k < N:
        while k < N:
            if nums[k] > nums[i]:
                R[i] = k + 1
                break
            else:
                k += 1
    if R[i] == -1:
        R[i] = 0
    i += 1
# print(L, R)
res = 0
for i in range(N):
    res = max(res, L[i] * R[i])
print(res)
