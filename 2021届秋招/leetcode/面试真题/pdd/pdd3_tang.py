import sys
class task:
    def calories(self, deli, lun, din, maxd, maxl):
        if maxd + maxl < deli:
            return -1
        if deli <= 0:
            return 0

        din.sort(key=lambda x: (x[0], x[1]))
        # print(lun, din)
        mincali = 1e9

        for ele in lun:
            delici, cali = ele[0], ele[1]
            if delici >= deli:
                mincali = min(mincali, cali)
                # print(mincali)

            else:
                remaindeli = deli - delici
                idx = self.bise(din, remaindeli)
                remaincali = 1e10
                for values in din[idx:]:
                    remaincali = min(values[1], remaincali)
                mincali = min(mincali, cali + remaincali)
                # print(mincali, remaindeli, idx, remaincali)

        for ele in din:
            delici, cali = ele[0], ele[1]
            if delici >= deli:
                mincali = min(mincali, cali)
            # print(deli, delici, cali, mincali)
        return mincali

    def bise(self, slist, val):
        lo, hi = 0, len(slist)
        while lo < hi:
            mid = (lo + hi) // 2
            if val < slist[mid][0]:
                hi = mid
            elif val == slist[mid][0]:
                return mid
            else:
                lo = mid + 1
        return lo


cases = sys.stdin.readline().strip().split(' ')  # 去除首尾空格
lunch, dinner, delicious = map(int, cases)
lunches, dinners = [], []
maxlun, maxdin = 0, 0

for _ in range(lunch):
    numbers = sys.stdin.readline().strip().split(' ')  # 返回分割好的字符列表
    numbers = list(map(int, numbers))
    lunches.append((numbers[1], numbers[0]))  # 注意字符转换为int
    maxlun = max(maxlun, numbers[1])

for _ in range(dinner):
    numbers = sys.stdin.readline().strip().split(' ')  # 返回分割好的字符列表
    numbers = list(map(int, numbers))
    dinners.append((numbers[1], numbers[0]))  # 注意字符转换为int
    maxdin = max(maxdin, numbers[1])

# print(lunches, dinners)
sol = task()
res = sol.calories(delicious, lunches, dinners, maxdin, maxlun)
print(res)