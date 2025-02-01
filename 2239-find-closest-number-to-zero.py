class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res, dis = float('inf'), float('inf')
        for n in nums:
            diff = abs(n - 0)
            if diff < dis or (diff == dis and n > res):
                dis = diff
                res = n
        
        return res
