class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        merged = []
        res = 0
        for start, end in meetings:
            if merged and merged[-1][1] >= start:
                merged[-1] = [min(start, merged[-1][0]), max(end, merged[-1][1])]
            else:
                if merged:
                    res += start - merged[-1][1] - 1
                merged.append([start, end])
        #edge cases for boundries
        res += (merged[0][0] - 1) + (days - merged[-1][1])
        return res    
