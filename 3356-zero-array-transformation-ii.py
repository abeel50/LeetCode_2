from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        total = sum(nums)
        if total == 0:
            return 0

        def can_zero(k):
            # Difference array approach
            diff = [0] * (len(nums) + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < len(nums):
                    diff[r + 1] -= val

            coverage = 0
            for i in range(len(nums)):
                coverage += diff[i]
                # Check if coverage at i is less than nums[i] (not enough to reduce nums[i] to zero)
                if coverage < nums[i]:
                    return False
            return True

        left, right = 1, len(queries) + 1
        while left < right:
            mid = (left + right) // 2
            if can_zero(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left <= len(queries) else -1
