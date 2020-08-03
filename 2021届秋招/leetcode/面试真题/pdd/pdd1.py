while True:
    try:
        K, N = 9, 2
        nums = [6, 3]
        d = K
        i = 0
        back_nums = 0
        while i != N:
            if d < 0:
                d = -d
                back_nums += 1
            if d != 0:
                d -= nums[i]
                i += 1
                if d==0:
                    print(0,0)
                    break
            else:
                print("paradox")
                break

        if d < 0:
            d = -d
            back_nums += 1
        if d != 0:
            print(d, back_nums)
    except:
        break
