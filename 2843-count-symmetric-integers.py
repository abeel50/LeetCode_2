class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            n = str(i)
            if len(n) % 2:
                continue
            m = len(n) // 2
            if sum([int(k) for k in n[:m]]) == sum([int(k) for k in n[m:]]):
                res += 1
        return res      
