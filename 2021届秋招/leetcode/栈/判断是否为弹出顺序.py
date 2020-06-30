
"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&&tqId=11174&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


题解思路:模拟一下
空栈,依次push,判断是否需要pop(稍微注意越界问题),最终如果栈为空就可以.
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV==[]:
            return True
        stack=[]
        j=0
        for i in pushV:
           stack.append(i)
           while stack[-1]==popV[j]  :
                m=stack.pop()
                j += 1
                if j==len(pushV):
                    break
        if stack==[]:
            return True
        else:
            return False


pushV=[1,2,3,4,5]
popV=[4,5,3,2,1]


print(Solution().IsPopOrder(pushV,popV))