T = int(input())
from collections import Counter

for _ in range(T):
    n = int(input())
    set_ = set()
    f = 0
    for _ in range(n):
        line = [int(i) for i in input().split()]
        if f == 0:
            line.sort()
            if tuple(line) in set_:
                f = 1
                print('YES')
            set_.add(tuple(line))
    if f:
        continue
    else:
        print('NO')
