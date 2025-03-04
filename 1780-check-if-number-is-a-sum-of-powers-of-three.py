class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def helper(sm, p):
            if sm == n:
                return True
            if sm > n or 3**p > n:
                return False
            
            if helper(sm + 3**p, p + 1):
                return True
            return helper(sm, p + 1)

        return helper(0, 0)
