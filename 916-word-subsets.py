class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_max_freq(words):
            max_count = Counter()
            for word in words:
                count = Counter(word)
                for char in count:
                    max_count[char] = max(max_count[char], count[char])
            return max_count

        b_max_count = count_max_freq(words2)
        
        def is_universal(word):
            word_count = Counter(word)
            for char in b_max_count:
                if word_count[char] < b_max_count[char]:
                    return False
            return True
        
        return [word for word in words1 if is_universal(word)]      
