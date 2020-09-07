n = int(input())
nums = []
for _ in range(n - 1):
    w, r = map(int, input().split())
    nums.append((w, r))
nums_kid = [int(i) for i in input().split()]
q = int(input())
question = []
for _ in range(q):
    w, r = map(int, input().split())
    question.append((w, r))
relations = [[0] * n for _ in range(n)]
for i in nums:
    w, r = i
    relations[w - 1][r - 1] = 0
    relations[r - 1][w - 1] = 0
for j in question:
    u, v = j
    if relations[u][v]==0:
        print("先祖")
    else:
for i in range(n):
    
