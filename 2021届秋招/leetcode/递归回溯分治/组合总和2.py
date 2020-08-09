"""
难点在于如何去重复
"""


from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        used = [False] * n
        path = []
        candidates.sort()

        def dfs(candidates, start, target, used, path):
            if target < 0:
                return
            if target == 0:
                res.append(path.copy())
                return
            for i in range(start, n):
                if i != 0 and candidates[i] == candidates[i - 1] and i > start:  ##在进入第二个dfs的时候i其实等于start,
                    # 所以不会跳过,但是,如果是在最顶层start=0但是i走到1的时候会跳过.
                    continue
                if not used[i]:
                    path.append(candidates[i])
                    used[i] = True
                    dfs(candidates, i + 1, target - candidates[i], used, path)
                    path.pop(-1)
                    used[i] = False

        dfs(candidates, 0, target, used, path)
        return res


print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
