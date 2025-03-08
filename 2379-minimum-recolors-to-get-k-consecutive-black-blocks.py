class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = w = blocks[:k].count('W')
        i = 1
        while i + k - 1 < len(blocks):
            if blocks[i-1] == 'W':
                w -= 1
            if blocks[i+k-1] == 'W':
                w += 1
            res = min(res, w)
            i += 1

        return res     
