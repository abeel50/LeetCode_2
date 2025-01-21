class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ROWS, COLS = 2, len(grid[0])
        
        # Calculate the prefix sums for both rows
        prefixSumR1, prefixSumR2 = [0] * (COLS + 1), [0] * (COLS + 1)
        
        for i in range(COLS):
            prefixSumR1[i + 1] = prefixSumR1[i] + grid[0][i]
            prefixSumR2[i + 1] = prefixSumR2[i] + grid[1][i]

        min_second_robot_score = float('inf')
        
        for i in range(COLS):
            # First robot can choose to go down after i-th column
            top_remaining = prefixSumR1[COLS] - prefixSumR1[i + 1]
            bottom_remaining = prefixSumR2[i]
            
            # Second robot will take the maximum of the remaining cells
            second_robot_score = max(top_remaining, bottom_remaining)
            
            # We want the minimum possible score for the second robot
            min_second_robot_score = min(min_second_robot_score, second_robot_score)
        
        return min_second_robot_score
