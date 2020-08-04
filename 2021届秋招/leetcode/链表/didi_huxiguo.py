while True:
    try:
        s1 = input()
        s=s1.lower()
        max_cha = "a"
        if not s:print("")
        for i in s:
            max_cha = max(max_cha, i)
        res = ""
        n=len(s)
        for i in range(n):
            res = res + s1[i] if s[i] != max_cha else res + s1[i] + "(max)"
        print(res)
    except:
        break
