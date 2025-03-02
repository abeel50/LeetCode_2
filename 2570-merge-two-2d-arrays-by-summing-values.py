class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        h = defaultdict(int)
        for id, val in nums1 + nums2:
            h[id] += val
        
        return [[id, h[id]] for id in sorted(h.keys())]
