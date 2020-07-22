if __name__=="__main__":
    while True:
        try:
            a=[int(i) for i in input().split()]
            n=a[0]
            h=a[1]
            line=input()
            data=[int(i) for i in line.split()]
            print(0)
            for i in range(1,n):
                j=i-1
                while j>=0:
                    if ((j+1)/(i+1)*(data[i]-h)+h)<=data[j]:
                        print(j+1)
                        break
                    else:
                        j-=1
                if j==-1:
                    print(0)
        except:
            break