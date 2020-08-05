n, k = list(map(int, input().split()))
num = []
for i in range(n):
    num.append((i,int(input())))
num=sorted(num,key=lambda x:x[1])
num=num[0:k]
num=sorted(num,key=lambda x:x[0])
for item in num:
	print(item[1])