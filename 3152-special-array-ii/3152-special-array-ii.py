class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        special = [0] * n

        # Populate the special array
        for i in range(n - 1):
            if nums[i] % 2 != nums[i + 1] % 2:
                special[i] = 1

        # Create prefix sum array
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + special[i]

        res = []
        for s, e in queries:
            # Check the number of special pairs in the range
            if prefix_sum[e] - prefix_sum[s] == e - s:
                res.append(True)
            else:
                res.append(False)

        return res