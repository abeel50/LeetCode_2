class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for i in range(1, len(nums)):
            if parity == nums[i] % 2:
                return False
            parity = nums[i] % 2
        return True       
