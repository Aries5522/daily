string1=input()
string2=input()
n=len(string1)
res=0
for i in range(n):
    if string1[i]==string2[i]:
        res+=20
    else:
        if res==0:
            continue
        else:
            res-=10
print(res)