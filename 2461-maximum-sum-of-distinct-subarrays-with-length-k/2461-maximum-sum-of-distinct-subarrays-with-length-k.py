class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        
        h = defaultdict(int)
        subSum = 0
        for i in range(k):
            h[nums[i]] += 1
            subSum += nums[i]
        
        res = subSum if len(h) == k else 0
        
        for i in range(k, len(nums)):
            subSum += nums[i] - nums[i - k]
            h[nums[i]] += 1
            h[nums[i - k]] -= 1
            if h[nums[i - k]] == 0:
                del h[nums[i - k]]
            
            if len(h) == k:
                res = max(res, subSum)
        
        return res