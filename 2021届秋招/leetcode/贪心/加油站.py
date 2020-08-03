from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 0:
            return -1
        for i in range(n):
            j = i
            start = True
            gas_cur = gas[i]
            while j % n != i or start:
                start = False
                if gas_cur - cost[j] < 0:
                    gas_cur = gas_cur - cost[j]
                    break
                else:
                    gas_cur -= cost[j]
                    j += 1
                    j = j % n
                    gas_cur = gas_cur + gas[j]
            if gas_cur >= 0:
                return i
        return -1
print(Solution().canCompleteCircuit(gas=[1,2,3,4,5],cost=[3,4,5,1,2]))