key = 0


def ZigZagPrintMatrix(arr):
    tc = 0
    tr = 0
    dr = 0
    dc = 0
    end_r = len(arr) - 1
    end_c = len(arr[0]) - 1
    reverse_flag = False
    while tr != end_r + 1:
        print_level(arr, tr, tc, dr, dc, reverse_flag)

        tr = tr + 1 if tc == end_c else tr
        tc = tc if tc == end_c else tc + 1
        dc = dc + 1 if dr == end_r else dc
        dr = dr if dr == end_r else dr + 1
        # 注意此处先后顺序。
        reverse_flag = not reverse_flag
    return arr


def print_level(arr, tr, tc, dr, dc, reverse_flag):
    global key
    if reverse_flag == False:
        while dr != tr - 1:
            arr[dr][dc] = str(key)
            key += 1
            dr -= 1
            dc += 1
    else:
        while tr != dr + 1:
            arr[tr][tc] = str(key)
            key += 1
            tr += 1
            tc -= 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    li = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(str(i * m + j))
        li.append(temp)
    res = ZigZagPrintMatrix(li)
    for i in range(n):
        print(" ".join(res[i]))
