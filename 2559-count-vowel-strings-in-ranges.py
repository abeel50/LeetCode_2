class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        prefixSum =defaultdict(int)
        curSum = 0
        for i, w in enumerate(words):
            if w[0] in VOWELS and w[-1] in VOWELS:
                curSum += 1
            prefixSum[i] = curSum

        res = []
        for s,e in queries:
            if s - 1 < 0 or s == 0:
                res.append(prefixSum[e])
            else:
                res.append(prefixSum[e]-prefixSum[s-1])
        return res
       
