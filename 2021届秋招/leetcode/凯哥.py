def find_target(nums, target):
    n = len(nums)
    k = n // 2 - 1 if n % 2 == 0 else n // 2
    z = 0
    for i in range(1, k + 1):
        if target < nums[i][i]:
            z = i  ##在第i圈
            break
    z -= 1
    for p in range(z, n - z):
        if nums[z][p] == target:
            return (z, p)
        if nums[p][z] == target:
            return (p, z)
        if nums[n - z - 1][p] == target:
            return (n - z - 1, p)
        if nums[p][n - z - 1] == target:
            return (p, n - z - 1)
    return False


print(find_target([[1, 9, 10, 11], [102, 133, 157, 29], [101, 200, 169, 30], [100, 40, 32, 31]], 169))
# print(find_target([[1,2,3],[8,9,4],[7,6,5]],9))