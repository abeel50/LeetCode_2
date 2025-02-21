class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection = set()
        res = 0
        for n in reversed(nums):
            res += 1
            if n <= k:
                collection.add(n)
                if len(collection) ==  k:
                    return res
        return res
