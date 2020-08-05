while True:
    try:
        def string2num(s):
            res = 0
            for i in s:
                res += ord(i.lower()) - ord("a") + 1
            return res
        data = [i for i in input().split(" ")]
        data_nums = [string2num(s) for s in data]
        K = data_nums[0]
        n = len(data_nums)
        for i in range(1, n):
            data_nums[i] = abs(data_nums[i] - K)
        min_ = min(data_nums[1:])
        index_min = [i for i, x in enumerate(data_nums) if x == min_][-1]
        print(data[index_min])
    except:
        break

