class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        productHash = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                productHash[prod] += 1
        
        res = 0
        for v in productHash.values():
            if v >= 2:
                # Number of ways to pick 2 pairs out of v pairs is (v * (v - 1)) // 2
                # Each pair (a, b) can be combined with each pair (c, d) in 8 ways
                res += (v * (v - 1) // 2) * 8

        return res
