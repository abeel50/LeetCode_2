class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        
        # Calculate the moves needed from the left side
        count = 0
        moves = 0
        for i in range(n):
            res[i] += moves
            count += int(boxes[i])
            moves += count
        
        # Calculate the moves needed from the right side
        count = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            res[i] += moves
            count += int(boxes[i])
            moves += count

        return res
