'''
Welcome to vivo !
'''


def solution(N, M):
    temp = [i for i in range(1, N + 1)]
    print(temp)
    res=[]
    i=1
    temp_index=[]
    while len(res)<=N:
        if i<=len(temp):
            if i%M==0:
                temp_index.append(i-1)
                k=i
            i+=1
        if i>len(temp):
            for m in temp_index:
                res.append(temp[m])
            i = i - len(temp)
            temp = [temp[j] for j in range(0, len(temp), 1) if j not in temp_index]
            temp_index = []
            k=0
    return res





print(solution(6,3))