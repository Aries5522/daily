class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence)<=2:
            return True
        n=len(sequence)
        r=n-1
        while r>0 and sequence[r-1]>sequence[n-1]:
            r-=1
        if r!=0 and max(sequence[0:r])>sequence[n-1]:
            return False
        else:return self.VerifySquenceOfBST(sequence[0:r]) and self.VerifySquenceOfBST(sequence[r:n-1])

print(Solution().VerifySquenceOfBST([4,8,6,12,16,14,10]))