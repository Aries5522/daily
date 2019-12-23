class Solution:
    def isPalindrome(self, x):
        print(self.reverse(x))
        return x==self.reverse(x)
    def reverse(self,x):
        if x>0:
            str_x=list(str(x))
            l=len(str_x)
            y=0
            for i in range(0,l):
                y+=int(str_x[i])*(10**i)
        if x==0:
            y=0
        if x<0:
            y=0
        return y

solution=Solution()
print(solution.isPalindrome(x=121))