class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        marked = [False] * len(nums)
        markedCount = 0
        adj = defaultdict(list)
        heapify(heap)
        
        for i, n in enumerate(nums):
            heappush(heap, (n, i))
            left, right = -1, -1
            if i - 1 >= 0:
                left = i - 1
            if i + 1 < len(nums):
                right = i + 1
            adj[i] = (left, right)
        
        res = 0
        while markedCount != len(nums) and heap:
            x, i = heappop(heap)
            if marked[i]:
                continue
            res += x
            marked[i] = True
            markedCount += 1
            left, right = adj[i]
            if left != -1 and not marked[left]:
                marked[left] = True
                markedCount += 1
            if right != -1 and not marked[right]:
                marked[right] = True
                markedCount += 1
        
        return res