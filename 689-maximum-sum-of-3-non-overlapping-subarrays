class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # pre sums for sub arrays of size k
        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1]+ nums[i] - nums[i-k])

        # Caching 
        cache = {}
        def getMaxSum (i, cnt):
            #base case
            if cnt == 3 or i > len(nums) - k:
                return 0
    
            # Already computed
            if (i, cnt) in cache:
                return cache[(i, cnt)]
            
            # included the current index
            inc = k_sums[i] + getMaxSum(i + k, cnt + 1)
            #skip the current index
            skp = getMaxSum(i+1, cnt)

            cache[(i, cnt)] = max(inc, skp)
            return cache[(i, cnt)]
        
        i = 0
        res = []
        while i <= len(nums) - k and len(res) < 3:
            inc = k_sums[i] + getMaxSum(i+k, len(res) + 1)
            skp = getMaxSum(i+1, len(res))
            if inc >=skp:
                res.append(i)
                i += k
            else:
                i += 1
        return res        
