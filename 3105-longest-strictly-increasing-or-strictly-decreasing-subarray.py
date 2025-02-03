class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prv = nums[0]
        inc, dec, res = 1, 1, 1 
        for i in range(1, len(nums)):
            if nums[i] > prv:
                inc += 1
                dec = 1
            elif nums[i] < prv:
                dec += 1
                inc = 1
            else:
                inc, dec = 1, 1
            res = max(res,inc, dec)
            prv = nums[i]
        return max(res, inc, dec)
