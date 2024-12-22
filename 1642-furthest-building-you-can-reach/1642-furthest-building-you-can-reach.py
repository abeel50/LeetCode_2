class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # min-heap to store the largest climbs we use bricks for
        
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb > 0:
                heapq.heappush(heap, climb)
                
                if len(heap) > ladders:  # use bricks when we've used all ladders
                    bricks -= heapq.heappop(heap)
                if bricks < 0:  # if we run out of bricks
                    return i
        
        return len(heights) - 1