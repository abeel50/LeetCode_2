class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_count = 0
        even_count = 1  # to handle the case when a subarray itself is odd
        prefix_sum = 0
        result = 0
        MOD = 10**9 + 7

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1
            result %= MOD
        
        return result
