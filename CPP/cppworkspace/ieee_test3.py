import numpy
import scipy

A=[3,2]
S=[3,1,5]



# A = list(map(int, input().rstrip().split()))
# S = list(map(int, input().rstrip().split()))

S.sort()
for i in range(len(S)):
    for j in range(len(A)):
        if S[i] < A[j]:
            A.insert(j,S[i])
            break
for i in A:
    print(i)