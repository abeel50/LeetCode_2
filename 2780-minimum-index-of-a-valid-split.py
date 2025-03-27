class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        h = defaultdict(int)
        maxFreq, dom, = 0, 0
        for n in nums:
            h[n] += 1
            if maxFreq < h[n]:
                maxFreq, dom = h[n], n
        
        f2 = h[dom] - (1 if nums[0] == dom else 0)
        l1, l2 = 1 , len(nums) - 1
        for i in range(len(nums)-1):
            f1 = h[dom] - f2
            if f1 > 0 and f2 > 0 and f1 * 2 > l1 and f2 * 2 > l2:
                return i
            f2 = f2 - (1 if nums[i+1] == dom else 0)
            l1 += 1
            l2 -= 1
        return -1        
