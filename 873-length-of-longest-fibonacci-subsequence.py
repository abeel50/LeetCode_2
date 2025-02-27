class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                prv, nxt = arr[i], arr[j]
                seq = 2 
                while prv + nxt in nums:
                    prv, nxt = nxt, prv + nxt
                    seq += 1
                res = max(res, seq)
        
        return res if res > 2 else 0
