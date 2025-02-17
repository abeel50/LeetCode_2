class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backTrack():
            res = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1 + backTrack()
                    count[c] +=1
            return res
        return backTrack()
