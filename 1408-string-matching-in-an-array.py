class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i,w in enumerate(words):
            for j,s in enumerate(words):
                if i == j:
                    continue
                if w in s and w not in res:
                    res.append(w)
        return res
