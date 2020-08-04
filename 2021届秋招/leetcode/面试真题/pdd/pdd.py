def main():
    T=int(input())
    res=[]
    t=0
    for i in range(T):
        N=int(input())
        import math
        k=math.sqrt(N)
        k=k+1 if k**2<N else k
        res.append(k)
    for num in res:
        print(num,end="\n")
main()