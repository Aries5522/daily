
def part_n(n):
    t=0
    res=[]
    while n>3 :
        if t ** 2 <= n and (t + 1) ** 2 > n:
            res.append(t ** 2)
            n=n-t**2
            t=0
        else:
            t+=1
    res+=[1]*n
    return res
print(part_n(195))

