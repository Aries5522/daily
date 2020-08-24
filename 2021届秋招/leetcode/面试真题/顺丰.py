string = input()
stack = []
res = 0
for s in string:
    if s in ["G", "o", "o", "d"]:
        stack.append(s)
        if s == "d":
            if len(stack) >= 4 and "".join(stack[-4:]) == "Good":
                stack = stack[:-4]
                res += 1
print(res)
"""
GGoodoooGoodd
"""
