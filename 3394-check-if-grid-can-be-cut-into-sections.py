class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def mergeRanges(ranges):
            merged = []
            for start, end in ranges:
                if merged and merged[-1][1] > start:
                    merged[-1] = [min(start, merged[-1][0]), max(end, merged[-1][1])]
                else:
                    merged.append([start, end])
                if len(merged) >= 3:
                    break
            return len(merged) >= 3

        x_ranges = [[x1, x2] for x1, y1, x2, y2 in rectangles]
        x_ranges.sort(key=lambda x: x[0])
        if mergeRanges(x_ranges):
            return True
        y_ranges = [[y1, y2] for x1, y1, x2, y2 in rectangles]
        y_ranges.sort(key=lambda x: x[0])
        return mergeRanges(y_ranges)
