import numpy as np


def solve3(vlist,wlist,totalWeight,totalLength):
    """完全背包问题"""
    resArr = np.zeros((totalWeight),dtype=np.int32)
    for i in range(0,totalLength):
        for j in range(0,totalWeight):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])

    print(resArr)
    return resArr[-1]



if __name__ == '__main__':
    v = [92, 22, 36, 46, 90]
    w = [77, 22, 29, 50, 99]
    weight = 100
    n = 5
    result = solve3(v, w, weight, totalLength=5)
    print(result)
