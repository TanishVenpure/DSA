class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x :x[0])
        merged = [intervals[0]]
        for current in intervals[1:] :
            last_merged = merged[-1]
            if current[0] <= last_merged[1]:
                last_merged[1] = max(current[1],last_merged[1])
            else:
                merged.append(current)
        return merged