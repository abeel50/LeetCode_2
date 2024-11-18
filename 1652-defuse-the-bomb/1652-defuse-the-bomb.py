class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N
        
        if k == 0:
            return res
        
        for i in range(N):
            if k > 0:
                res[i] = sum(code[(i + j) % N] for j in range(1, k + 1))
            else:
                res[i] = sum(code[(i + j) % N] for j in range(k, 0))
        
        return res