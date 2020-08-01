
"""

使用两个栈，一个用来存数字和左括号nums，一个用来存操作符ops。
当nums的最后两个元素是数字并且ops非空，就把这三个元素弹出来求值一次，再把结果压入nums。
如果碰到右括号，则删除nums的倒数第二个元素（这个元素一定是左括号），再尝试求值一次。

可以自己先写一个cal函数用来计算nums后面两个数的相加或者相减.

"""

class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        data = [0]
        label = ["+"]
        n = len(s)
        i = 0
        while i < n:
            if s[i] in ["+", "-"]:
                label.append(s[i])
                i += 1
            elif s[i] in number:
                j = i + 1
                while j < n and s[j] in number:
                    j += 1
                data.append(int(s[i:j]))
                i=j
                if data[-1]!="(" and data[-2]!="(":
                    number2=data.pop()
                    number1=data.pop()
                    temp=number1+number2 if label.pop()=="+" else number1-number2
                    data.append(temp)
            elif s[i]=="(":
                data.append("(")
                i+=1
            elif s[i]==")":
                k1=data.pop()
                data.pop()
                k2=data.pop()
                temp=k1+k2 if label.pop()=="+" else k2-k1
                data.append(temp)
                i+=1
            else:
                i += 1
        res = data[0]
        return res
print(Solution().calculate("1-(5)"))



"""
参考代码:


class Solution:
    def calculate(self, s: str) -> int:
        nums, ops = [], []
        pos, N = 0, len(s)

        def cal() :
            if ops and len(nums) >= 2 and nums[-1] not in ['(',')'] and nums[-2] not in ['(',')'] :
                nums[-2] = nums[-1] + nums[-2] if ops[-1] == '+' else nums[-2] - nums[-1]
                del nums[-1]
                del ops[-1]

        while pos < N :
            tp = pos
            while tp < N and s[tp] in ['0','1','2','3','4','5','6','7','8','9']:
                tp += 1
            if tp != pos :
                n = int(s[pos:tp])
                nums.append(n)
                cal()
                pos = tp
                continue

            if s[pos] in ['+','-'] : ops.append(s[pos])
            if s[pos] == '(' : nums.append('(')
            if s[pos] == ')' :
                del nums[-2]
                cal()
            pos += 1
        
        return nums[-1]
"""