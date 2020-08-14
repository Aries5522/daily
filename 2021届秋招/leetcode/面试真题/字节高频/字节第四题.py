def lower_bound(nums, target):  ##查找大于等于target的最小的下标
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

while True:
    try:
        N = int(input())
        machines = [int(i) for i in input().split()]
        products = [int(i) for i in input().split()]
        P = int(input())
        machines.sort()
        products.sort()
        for i in range(N):
            if products[i] > machines[i]:
                print(0)
                break
        res = 1
        k = 0
        for j in range(N - 1, -1, -1):
            index = lower_bound(machines, products[j])
            res *= (N - index - k) % P
            k += 1
        print(res % P)
    except:
        break

"""
3
1 2 3
1 2 3
100

5
1 3 4 5 6
1 2 3 3 4
100000

"""
