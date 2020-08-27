# nums = [int(i) for i in input().split()]
nums = [2, 2, 2, 4]
nums.sort()


def main(nums):
    while nums[3] != nums[0]:
        if nums[3] - nums[0] > 2:
            nums[3] -= 2
            nums[0] += 1
            nums.sort()
        elif nums[3] - nums[0] == 2:
            nums[3] -= 1
            nums[2] -= 1
            nums[0] += 1
            nums.sort()
        elif nums[3] - nums[0] == 1:
            print(-1)
            return
    print(nums[0] * 4)


main(nums)
