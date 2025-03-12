class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        countNegatives, countPositives, countZeros = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] < 0 :
                countNegatives += 1
            if nums[i] == 0:
                countZeros += 1
        
        countPositives = len(nums) - countNegatives - countZeros
        return max(countNegatives , countPositives)
        
