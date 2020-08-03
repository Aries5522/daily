"""
贪心算法,在每次能选的项目中挑选价值最大的去做.

"""






from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        import heapq

        if W >= max(Capital):
            return W+sum(heapq.nlargest(k, Profits))
        n = len(Profits)
        projects = [(Profits[i], Capital[i]) for i in range(len(Profits))]
        projects = sorted(projects, key=lambda x: (x[1], x[0]))
        # print(projects)
        cur_money = W
        for i in range(min(n, k)):
            j = 0
            max_profit_index = -1
            while projects and j < len(projects):
                  # index,profit
                if projects[j][1] <= cur_money:
                    if max_profit_index == -1:
                        max_profit_index = j
                    if projects[j][0] > projects[max_profit_index][0]:
                        max_profit_index = j
                j += 1
            if max_profit_index == -1:
                break
            else:
                cur_money = cur_money + projects[max_profit_index][0]
                del projects[max_profit_index]
        return cur_money


print(Solution().findMaximizedCapital(k=1, W=2, Profits=[1, 2, 3], Capital=[1,1,2]))
