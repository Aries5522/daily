T = int(input())
for _ in range(T):
    N = int(input())
    data = [int(k) for k in input().split()]

    a = data[0]
    for i in range(1, N):
        b=data[i]
        while b:
            a, b = b, a % b
    print(a)

