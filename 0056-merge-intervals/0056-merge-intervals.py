class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort list based on index [i]
        # start the pointer to first List [0]
        # iterate from index 1 [1]
        # compare if prev[1] >= curr[0] -> prev[1] = curr[1]
        # if we found that prev[1] < curr[0] it means its not overlapped
        # we add the prev to merged
        intervals.sort(key=lambda x: x[0])
        merged = []

        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(interval[1], prev[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)

        return merged