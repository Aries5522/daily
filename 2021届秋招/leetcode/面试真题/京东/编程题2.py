import sys
mat=[0]*10
for i in range(10,1000):
    # N, M = map(int, sys.stdin.readline().strip("\n").split(" "))
    N=10
    M=i
    max_n = 10**6 + 10
    is_prime = [1] * max_n
    is_prime[0], is_prime[1] = 0,0
    res = 0
    for i in range(2, max_n):
        if is_prime[i]:
            j = 2 * i
            while j < max_n:
                is_prime[j] = 0
                j += i
    def is_huiwen(s):
        if str(s) == str(s)[::-1]:
            return True
        else:
            return False
    for num in range(N, M+1):
        lenght = len(str(num))
        i = 0
        while i < lenght:
            num=str(num)
            new = num[:i] + num[i + 1:]
            new = int(new)
            if is_prime[new] and is_huiwen(new):
                res += 1
                break
            else:
                i += 1
    mat.append(res)
print(mat)
print(mat[120]-mat[110])
