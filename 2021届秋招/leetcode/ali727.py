while True:
    try:
        T=int(input())
        t=0
        res=[]
        while t<T:
            data=[int(i) for i in input().split(" ")]
            n=data[0]
            nums=data[1:]
            record=1
            i=n-1
            while i>0:
                while i>0 and nums[i]==nums[i-1]:
                    i-=1
                    record+=1
                if nums[i]!=nums[i-1]:
                    if record%2==1:
                        res.append("先手胜利")
                        break
                    else:
                        record=1
                        i-=1
            if i==0:
                res.append("后手胜利")
            t+=1
        for k in res:
            print(k,end="\n")
    except:
        break