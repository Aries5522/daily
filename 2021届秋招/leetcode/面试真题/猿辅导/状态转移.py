def encoder(nums):
    k = 8
    res = 0
    for i in range(3):
        for j in range(3):
            res += nums[i][j] * (2 ** k)
            k -= 1
    return res

def longest_step(mat1, mat2):
    visited = [0] * 512
    res = []
    def dfs(mat1, ans, visited):
        if encoder(mat1) == encoder(mat2):
            res.append(ans)
            return
        if visited[encoder(mat1)] == 1:
            return
        visited[encoder(mat1)] = 1
        for i in range(3):
            for j in range(3):
                if mat1[i][j] == 1:
                    if 0 <= i + 1 <= 2 and mat1[i + 1][j] == 0:
                        mat1[i][j], mat1[i + 1][j] = mat1[i + 1][j], mat1[i][j]
                        dfs(mat1, ans + 1, visited)
                        mat1[i][j], mat1[i + 1][j] = mat1[i + 1][j], mat1[i][j]
                    if 0 <= i - 1 <= 2 and mat1[i - 1][j] == 0:
                        mat1[i][j], mat1[i - 1][j] = mat1[i - 1][j], mat1[i][j]
                        dfs(mat1, ans + 1, visited)
                        mat1[i][j], mat1[i - 1][j] = mat1[i - 1][j], mat1[i][j]
                    if 0 <= j + 1 <= 2 and mat1[i][j + 1] == 0:
                        mat1[i][j], mat1[i][j + 1] = mat1[i][j + 1], mat1[i][j]
                        dfs(mat1, ans + 1, visited)
                        mat1[i][j], mat1[i][j + 1] = mat1[i][j + 1], mat1[i][j]
                    if 0 <= j - 1 <= 2 and mat1[i][j - 1] == 0:
                        mat1[i][j], mat1[i][j - 1] = mat1[i][j - 1], mat1[i][j]
                        dfs(mat1, ans + 1, visited)
                        mat1[i][j], mat1[i][j - 1] = mat1[i][j - 1], mat1[i][j]
        return res

    res = dfs(mat1, 0, visited)
    return res, min(res)


print(longest_step([[1, 0, 0], [1, 1, 0], [0, 0, 0]], [[0, 0, 1], [1, 0, 0], [0, 1, 0]]))
