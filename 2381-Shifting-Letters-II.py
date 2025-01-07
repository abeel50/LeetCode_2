class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_array = [0] * (n + 1)
        
        # Apply the shifts to the shift_array
        for start, end, d in shifts:
            if d == 1:
                shift_array[start] += 1
                if end + 1 < n:
                    shift_array[end + 1] -= 1
            else:
                shift_array[start] -= 1
                if end + 1 < n:
                    shift_array[end + 1] += 1
        
        # Calculate the prefix sum of shift_array
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        
        # Apply the shifts to the string
        alphabates = dict(zip(string.ascii_lowercase, range(26)))
        res = []
        for i, c in enumerate(s):
            new_pos = (alphabates[c] + shift_array[i]) % 26
            res.append(string.ascii_lowercase[new_pos])
        
        return ''.join(res)
