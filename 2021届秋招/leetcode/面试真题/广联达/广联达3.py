n = int(input())
nums = [int(i) for i in input().split()]
res = 0
nums1 = nums[:]
nums1.sort(reverse=True)
for i in range(1, n):
    if nums.index(nums1[i]) > nums.index(nums1[i - 1]):
        res += 1
        k=nums.pop(i)
        nums.insert(0,k)
print(res)
#
#
# #include <bits/stdc++.h>
# using namespace std;
#
# int main()
# {
#     int n;
#     cin >> n;
#     vector<int> nums(n);
#     int i, j;
#     for (i = 0; i < n; ++i)
#         cin >> nums[i];
#     vector<int> sortedNums = nums;
#     sort(sortedNums.begin(), sortedNums.end());
#     i = j = n - 1;
#     while (i >= 0)
#     {
#         while (i >= 0 && nums[i] != sortedNums[j])
#             --i;
#         --i;
#         --j;
#     }
#     cout << j - i << endl;
#     return 0;
# }