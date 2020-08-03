# m,n=input().split()
# print(m,n)
import collections

while True:
    try:
        n, m = input().split()
        data = [int(i) for i in input().split()]
        print(n,m)
        print(data)
        dict_ = {}
        for i in data:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        res=[]
        for i in range(n):
            if dict_[data[i]]<=m:
                res.append(data[i])
    except:
        break
