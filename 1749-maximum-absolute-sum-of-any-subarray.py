class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxRes, minRes = nums[0], nums[0]
        maxEnding, minEnding = nums[0], nums[0]
  
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            minEnding = min(minEnding + nums[i], nums[i]) 

            maxRes = max(maxRes, maxEnding)
            minRes = min(minRes, minEnding)

        return max(abs(maxRes), abs(minRes))     
