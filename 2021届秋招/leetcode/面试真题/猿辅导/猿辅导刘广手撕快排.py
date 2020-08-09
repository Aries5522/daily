def quicksort(nums):
    return quicksort([i for i in nums[1:] if i <= nums[0]]) + [nums[0]] + quicksort([i for i in nums[1:] if i > nums[0]]) if len(nums)>1 else nums


print(quicksort([1, 8, 2, 6, 4, 5, 9, 10, 1]))
