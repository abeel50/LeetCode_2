class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        counter = [0] * (len(A) + 1)
        res = []
        for i in range(len(A)):
            counter[A[i]] += 1
            counter[B[i]] += 1
            res.append(counter.count(2))
        return res
        
