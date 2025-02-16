class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index):
            if index == len(sequence):
                return True
            
            if sequence[index] != 0:
                return backtrack(index + 1)
            
            for x in range(n, 0, -1):
                if used[x]:
                    continue
                
                if x == 1:
                    sequence[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    used[1] = False
                else:
                    if index + x < len(sequence) and sequence[index + x] == 0:
                        sequence[index] = x
                        sequence[index + x] = x
                        used[x] = True
                        if backtrack(index + 1):
                            return True
                        sequence[index] = 0
                        sequence[index + x] = 0
                        used[x] = False
            
            return False

        backtrack(0)
        return sequence
