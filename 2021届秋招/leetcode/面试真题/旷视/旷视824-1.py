# string = input()
string = "FRF"
N = len(string)
M = [int(i) for i in range(N + 1)]
A = list(string)
def is_ok(A, M):
    for i in range(N):
        if A[i] == "R":
            if M[i] >= M[i + 1]:
                return False
        if A[i] == "F":
            if M[i] <= M[i + 1]:
                return False
    return True
def permuteUnique(nums):
    global res
    nums.sort()
    res = 0
    check = [0 for i in range(len(nums))]
    backtrack([], nums, check)
    return res
def backtrack(sol, nums, check):
    global res
    if len(sol) == len(nums) and is_ok(A, sol):
        res += 1
        res %= int((1e9 + 7))
        return
    for i in range(len(nums)):
        if check[i] == 1:
            continue
        check[i] = 1
        backtrack(sol + [nums[i]], nums, check)
        check[i] = 0

print(permuteUnique(M))
