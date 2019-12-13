# N = get_number()
# A = get_number()
# B = get_number()
N=4
A=2
B=3
m=[]

def test(N,A,B,m):
    if B<A:
        return m
    if N-B>B:
        m.append(B)
        return test(N=N-B,A=A,B=B,m=m)
    elif N-B<=B and N-B>=A:
        m.append(B)
        m.append(N-B)
        return m
    return test(N=N,A=A,B=B-1,m=m)

if __name__ == '__main__':
    N = 44
    A = 8
    B = 10
    m = []
    if N<2*A:
        print("NO")
    else:
        print("YES")
        m=sorted(test(N,A,B,m))
        for i in m[:-1]:
            print(i,end=" ")
        print(m[-1])