class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Create a dictionary to store the highest beauty for each price
        h = defaultdict(int)
        for p, b in items:
            h[p] = max(h[p], b)
        
        # Sort the dictionary by price
        sorted_items = sorted(h.items())
        
        # Prepare a list to store the maximum beauty till each price point
        max_beauty = []
        current_max = 0
        for price, beauty in sorted_items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))
        
        # Prepare the result list
        res = []
        for q in queries:
            # Binary search to find the maximum beauty for the given query price
            left, right = 0, len(max_beauty) - 1
            while left <= right:
                mid = (left + right) // 2
                if max_beauty[mid][0] <= q:
                    left = mid + 1
                else:
                    right = mid - 1
            res.append(max_beauty[right][1] if right >= 0 else 0)
        
        return res