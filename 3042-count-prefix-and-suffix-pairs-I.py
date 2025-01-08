class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False
     
            # Check if str1 is a prefix of str2
            is_prefix = str2.startswith(str1)
            
            # Check if str1 is a suffix of str2
            is_suffix = str2.endswith(str1)
            
            return is_prefix and is_suffix
        
        res = 0
        for i,w in enumerate(words):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(w, words[j]):
                    res += 1

        return res
