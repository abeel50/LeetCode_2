class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, value in enumerate(nums):
            if target - value in d:
                return [d[target - value], i]
            else:
                d[value] = i
        