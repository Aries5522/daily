while True:
    try:
        N = int(input())
        data = [i.zfill(3) for i in input().split()]
        dict_ = {0: "0000", 1: "0001", 2: "0010"
            , 3: "0011", 4: "0100", 5: "0101"
            , 6: "0110", 7: "0111", 8: "1000", 9: "1001"}
        for i in data:
            i = str(i)
            res = ""
            for j in range(3):
                res += dict_[int(i[j])]
            print(int(res[::-1]))
    except:
        break
