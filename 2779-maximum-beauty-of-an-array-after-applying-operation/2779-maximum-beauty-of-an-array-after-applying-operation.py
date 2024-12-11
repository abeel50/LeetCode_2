class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        i, j = 0, 0
        while j < len(nums):
            if nums[j] - nums[i] <= 2 * k:
                res = max(res, j - i + 1)
                j += 1
            else:
                i += 1
        return res