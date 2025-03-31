class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        splits = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        splits.sort()
        i = k - 1
        minScore = sum(splits[:i])
        maxScore = sum(splits[-i:])
        return maxScore- minScore
