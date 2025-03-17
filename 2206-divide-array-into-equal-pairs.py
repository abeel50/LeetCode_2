class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash = defaultdict(int)
        pairs = 0
        for n in nums:
            hash[n] += 1
            if hash[n] % 2 == 0:
                pairs += 1
        return pairs == len(nums) // 2   
