class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        total_pairs = len(nums) * (len(nums) - 1) // 2
        good_pairs = 0
        
        for i, num in enumerate(nums):
            diff = num - i
            good_pairs += hash[diff]
            hash[diff] += 1
        
        return total_pairs - good_pairs
