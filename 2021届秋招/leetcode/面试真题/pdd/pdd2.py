import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
hashmap = defaultdict(int)
for i in range(n):
    line = sys.stdin.readline().strip()
    v = list(map(int, line.split()))
    k = sorted([sorted(v[:2]), sorted(v[2:4]), sorted(v[4:])])
    s = str(k[0][0]) + str(k[0][1])+str([1][0]) + str(k[1][1]) + str(k[2][0])+str([2][1])
    if s in hashmap.keys():
        hashmap[s] += 1
    else:
        hashmap[s] = 1
    print(len(hashmap.keys()))
    for r in sorted(hashmap.values())[::-1]:
        print(r, end=' ')
