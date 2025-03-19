class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] = int(nums[i+1] != 1)
                nums[i+2] = int(nums[i+2] != 1)
                res += 1
    
        if nums[len(nums) - 2] == 0 or nums[len(nums) - 1] == 0:
            return -1

        return res
        
