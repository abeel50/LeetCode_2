class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRobbed(target):
            i, count = 0, 0
            while i < len(nums):
                if nums[i] <= target:
                    count += 1
                    i += 1
                i += 1
                if count == k:
                    break
            return k == count        

        left, right = float('inf'), float('-inf')
        for num in nums:
            left, right = min(left, num), max(right, num)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if canRobbed(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res  
  
