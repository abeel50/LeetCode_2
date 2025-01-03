class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum = []
        cur = 0
        for i,n in enumerate(nums):
            cur += n
            prefixSum.append(cur)

        res = 0
        for i in range(len(nums)-1):
            if prefixSum[i] >= prefixSum[-1] - prefixSum[i]:
                res += 1
        return res      
