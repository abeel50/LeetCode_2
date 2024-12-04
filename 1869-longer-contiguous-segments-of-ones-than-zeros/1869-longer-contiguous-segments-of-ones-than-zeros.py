class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_one, max_zero = 0, 0
        current_one, current_zero = 0, 0
        
        for c in s:
            if c == '1':
                current_one += 1
                max_one = max(max_one, current_one)
                current_zero = 0
            else:
                current_zero += 1
                max_zero = max(max_zero, current_zero)
                current_one = 0
        
        return max_one > max_zero