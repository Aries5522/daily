
n = int(input())
nums = [int(i) for i in input().split()]
import math
def main(n, nums):
    if n == 1:
        print("%.2f" % nums[1] / nums[0])
        return
    if n == 2:
        res = []
        a, b, c = nums
        if a==0:
            main(1,nums[1:])
        if b ** 2 - 4 * a * c > 0:
            res.append((-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            res.append((-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            res.sort()
            print("%.2f" % res[0], end=" ")
            print("%.2f" % res[1])
        elif b ** 2 - 4 * a * c == 0:
            print("%.2f" % -1 * b / (2 * a))
        else:
            print("No")
    else:
        print("No")

main(n, nums)
