class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        numGroup = {} #keep track num is in which group

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1] > limit):
                groups.append(deque())
            groups[-1].append(n)
            numGroup[n] = len(groups) - 1

        res = []
        for n in nums:
            j = numGroup[n]
            res.append(groups[j].popleft())
        return res
