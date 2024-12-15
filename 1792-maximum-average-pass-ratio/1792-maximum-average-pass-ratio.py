class Solution:
  def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    heap = []
    heapify(heap)
    
    for p, t in classes:
      current_ratio = p / t
      gain = (p + 1) / (t + 1) - current_ratio
      heappush(heap, (-gain, p, t))
    
    while extraStudents > 0:
      gain, p, t = heappop(heap)
      p += 1
      t += 1
      new_gain = (p + 1) / (t + 1) - (p / t)
      heappush(heap, (-new_gain, p, t))
      extraStudents -= 1
    
    return sum(p / t for _, p, t in heap) / len(classes)
