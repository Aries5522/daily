data = [i for i in map(float, input().split(","))]

res = 0
for i in data:
    if i == min(data):
        res += 1
print(res)
