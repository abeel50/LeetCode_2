class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total = 0
        nums = []
        for row in grid:
            for n in row:
                nums.append(n)
                total += n
                if n % x != grid[0][0] % x:
                    return -1
        
        nums.sort()
        prefix = 0
        res = float('inf')
        for i in range(len(nums)):
            left = nums[i] * i - prefix
            right = total - prefix - (nums[i] * (len(nums) -i))
            res = min (res, (left+ right) // x)
            prefix += nums[i]
        return res
 
