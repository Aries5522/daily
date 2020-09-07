N = int(input())
A = [int(i) for i in input().split()]
# N = 6
# A = [4, 3, 2, 3, 2, 1]
B = []
res = 0
while True:
    i = 1
    B.append(A[0])
    while i < len(A):
        if A[i] < A[i - 1]:
            i += 1
        else:
            B.append(A[i])
            i += 1
    if len(A) == len(B):
        break
    res += 1
    A = B[:]
    B = []
print(res)
