# N = int(input())
# nums = [int(i) for i in input().split()]
N = 3
nums = [0, 1, 1]
L = len(nums)
k = nums.count(0)
nums.sort()
def main():
    for i in range(1, N):
        if nums[i] == nums[i - 1] and nums[i] != 0:
            print("Invalid")
            return
    i = 0
    while i < N and nums[i] == 0:
        i += 1
    min_ = nums[i] if i < N else 0
    max_ = nums[-1]
    if (max_ - min_) + 1 - (L - k) <= k:
        print("Valid")
    else:
        print("Invalid")
    return


main()
