class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        l1, l2 = len(nums1), len(nums2)
        
        if l1 % 2 == 0 and l2 % 2 == 0:
            return res
        
        if l1 % 2:
            for n2 in nums2:
                res ^= n2
                
        if l2 % 2:
            for n1 in nums1:
                res ^= n1

        return res
