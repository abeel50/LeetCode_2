class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canAllocateCandies(n):
            child = 0
            for c in candies:
                if c >= n:
                    child += c // n
            return child >= k 

        left, right = 1, sum(candies) // k
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if canAllocateCandies(mid):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
        return res      
