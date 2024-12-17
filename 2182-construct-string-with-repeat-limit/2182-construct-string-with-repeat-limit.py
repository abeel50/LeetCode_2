class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Create a frequency dictionary for all characters
        freq = {chr(ord('a') + i): 0 for i in range(26)}
        
        # Count frequency of each character in the string
        for c in s:
            freq[c] += 1
        
        # Create a max heap based on character ASCII values
        heap = []
        for c in freq:
            if freq[c] > 0:
                heapq.heappush(heap, (-ord(c), freq[c]))
        
        result = []
        
        while heap:
            c, count = heapq.heappop(heap)
            c = chr(-c)
            
            # Determine how many times we can use this character
            use_count = min(count, repeatLimit)
            
            # Add the character use_count times to the result
            result.extend([c] * use_count)
            count -= use_count
            
            if count > 0:
                if heap:
                    next_c, next_count = heapq.heappop(heap)
                    next_c = chr(-next_c)
                    
                    # Add the next character once to break the repeat limit
                    result.append(next_c)
                    next_count -= 1
                    
                    # Push the next character back if it still has remaining count
                    if next_count > 0:
                        heapq.heappush(heap, (-ord(next_c), next_count))
                    
                    # Push the current character back since it still has remaining count
                    heapq.heappush(heap, (-ord(c), count))
                else:
                    # No other character to insert, break loop to prevent invalid string
                    break
        
        return ''.join(result)
