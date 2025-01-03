class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp7 = deque()
        dp30 = deque()
        
        cost = 0
        
        for d in days:
            while dp7 and dp7[0][0] <= d - 7:
                dp7.popleft()
            while dp30 and dp30[0][0] <= d - 30:
                dp30.popleft()
                
            dp7.append((d, cost + costs[1]))
            dp30.append((d, cost + costs[2]))
            cost = min(cost + costs[0], dp7[0][1], dp30[0][1])
        return cost
          
