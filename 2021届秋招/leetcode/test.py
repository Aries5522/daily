if __name__=="__main__":
    a=[int(i) for i in input().split()]
    print(a)
    M=a[0]
    N=a[1]
    m=0
    data=[]
    while True:
        line=input()
        if not line:
            break
        temp=[int(i) for i in line.split()]
        data.append(temp)
    print(data)

#不确定行数

if __name__=="__main__":
    a=[int(i) for i in input().split()]
    print(a)
    M=a[0]
    N=a[1]
    m=0
    data=[]
    while m<M:
        line=input()
        temp=[int(i) for i in line.split()]
        data.append(temp)
        m+=1
    print(data)
#确定行数






