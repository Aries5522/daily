def generate(n):
    res = []

    def dfs(left, right, path):
        if left == 0 and right == 0:
            res.append(path)
        if left:
            dfs(left - 1, right, path + "(")
        if left < right:
            dfs(left, right - 1, path + ")")

    dfs(n, n, "")
    return res


print(generate(3))
