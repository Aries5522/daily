while True:
    try:
        strings = input().split()
        stack = []
        help_stack = []
        for s in strings:
            if s not in ["undo", "redo"]:
                stack.append(s)
            elif stack and s == "undo":
                help_stack.append(stack.pop())
            elif help_stack and s == "redo":
                stack.append(help_stack.pop())
        res = " ".join(stack)
        print(res)
    except:
        break
"""
hello hello1 hello2 undo undo redo redo redo redo world. undo
"""
