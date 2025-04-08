class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def isDistinct(values):
            for v in values:
                if v > 1:
                    return False
            return True

        hash = Counter(nums)
        res = 0
        i = 0
        while i < len(nums) and not isDistinct(hash.values()):
            for j in range(i, i+3):
                if j < len(nums):
                    hash[nums[j]] -= 1
            i += 3
            res += 1
        return res       
