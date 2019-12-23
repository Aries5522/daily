class Solution:
    def romanToInt(self, s: str) -> int:
        num_list = []
        for i in ['M', 'D', 'C', 'L', 'X', 'V', 'I']:
            num_i = s.count(i)
            num_list.append(num_i)

        num_list1 = []
        for j in ['CD', 'CM', 'XL', 'XC','IV', 'IX']:
            num_j = s.count(j)
            num_list1.append(num_j)

        num_list2 = [num_list1[0] + num_list1[1],
                     num_list1[2] + num_list1[3], num_list1[4] + num_list1[5]]
        num = num_list[0] * 1000+num_list[1] * 500-num_list2[0] * 100 + (num_list[2] - num_list2[0]) * 100+num_list[3] * 50-num_list2[1] * 10 + (num_list[4] - num_list2[1]) * 10+num_list[5] * 5-num_list2[2] * 1 + (num_list[6] - num_list2[2]) * 1
        return num
    def romanToInt_1(self, s: str) -> int:
        hashmap={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        print(len(s))
        list_str=list(s)
        num=hashmap[list_str[-1]]
        index=0
        while index < len(s)-1:
            if (hashmap[s[index]] >= hashmap[s[index+1]]):
                num+=hashmap[s[index]]
                index+=1
            else:
                num-=hashmap[s[index]]
                index+=1
        return num

sul = Solution()
print(sul.romanToInt("IV"))
print(sul.romanToInt_1("IV"))
        