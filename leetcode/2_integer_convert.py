def reverse(x):
    if x>0:
        str_x=list(str(x))
        l=len(str_x)
        y=0
        for i in range(0,l):
            y+=int(str_x[i])*(10**i)
    if x==0:
        y=0
    if x<0:
        x=-x
        y=0-reverse(x)
    if (y>2**31-1 or y<-2**31):
        y=0
    return y

print(reverse(-23443410))
