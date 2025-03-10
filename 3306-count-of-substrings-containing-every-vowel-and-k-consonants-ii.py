class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def helperK(k):
            vowels = defaultdict(int)
            const, res = 0, 0
            l = 0

            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowels[word[r]] += 1
                else:
                    const += 1
                while len(vowels) == 5 and const >= k:
                    res += (len(word) - r)
                    if word[l] in 'aeiou':
                        vowels[word[l]] -= 1
                    else:
                        const -= 1
                    if vowels[word[l]] == 0:
                        vowels.pop(word[l])
                    l += 1
            return res
        return helperK(k) - helperK(k + 1)

        
