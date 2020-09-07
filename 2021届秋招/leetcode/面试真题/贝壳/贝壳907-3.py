def main():
    n = int(input())
    Prices = [int(i) for i in input().split()]
    q = int(input())
    for _ in range(q):
        x, y, z = map(int, input().split())
        target = x * y * z
        a = [target - i for i in Prices]
        if max(a) < 0:
            res.append([-1])
        else:
            for i in range(n):
                if a[i] < 0:
                    a[i] = 1e9
            idx = a.index(min(a))
            res.append([idx + 1, target - a[idx]])

T = int(input())
res = []
for _ in range(T):
    main()
for i in res:
    if len(i) == 1:
        print(-1)
    else:
        print(i[0], i[1])
'''
2
8
3 6 9 66 66 80 88 99
2
1 1 10
10 4 2
8
3 6 9 66 66 80 88 99
2
1 1 10
10 4 2
'''
