class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = set(banned)
        res = 0
        for i in range(1, n + 1):
            if i not in banned and i <= maxSum:
                res += 1
                maxSum -= i
        return res