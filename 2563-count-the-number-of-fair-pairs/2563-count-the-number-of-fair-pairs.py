class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        
        for i in range(n):
            l ,r = i + 1 , n - 1
            
            # Find the first index where nums[i] + nums[l] >= lower
            while l <= r:
                mid = (l + r) // 2
                if nums[i] + nums[mid] < lower:
                    l = mid + 1
                else:
                    r = mid - 1
            left_bound = l
            
            l = i + 1
            r = n - 1
            
            # Find the last index where nums[i] + nums[r] <= upper
            while l <= r:
                mid = (l + r) // 2
                if nums[i] + nums[mid] > upper:
                    r = mid - 1
                else:
                    l = mid + 1
            right_bound = r
            
            if left_bound <= right_bound:
                res += right_bound - left_bound + 1
        
        return res