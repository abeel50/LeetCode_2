class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countBits(n):
            res = 0
            while n > 0:
                res += 1 & n
                n = n >> 1
            return res

        count1, count2 = countBits(num1), countBits(num2)
        x  = num1
        i = 0

        while count1 != count2:
            if count2 < count1 and x & (1 << i):
                count1 -= 1
                x = x ^ (1 << i)
            if count1 < count2 and x & (1 << i) == 0:
                count1 += 1
                x = x | (1 << i)
            i += 1
        return x
