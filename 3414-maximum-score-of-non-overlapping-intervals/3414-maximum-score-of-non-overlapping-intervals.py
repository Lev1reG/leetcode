class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        idx_original = {}
        for i, (l, r, w) in enumerate(intervals):
            key = (l, r, w)
            if key not in idx_original:
                idx_original[key] = i
        
        intervals = sorted(idx_original.keys())
        n = len(intervals)

        next_idx = [0] * n
        for i in range(n):
            l, r, w = intervals[i]
            next_idx[i] = bisect.bisect_right(
                intervals, (r, float('inf'), float('inf'))
            )
        
        dp = {}

        def solve(i, k):
            if i == n or k == 0:
                return (0, [])
            if (i, k) in dp:
                return dp[(i, k)]
            
            skip = solve(i + 1, k)

            l, r, w = intervals[i]
            take_score, take_idx = solve(next_idx[i], k - 1)
            take_score -= w
            take_idx = sorted(take_idx + [idx_original[(l, r, w)]])
            take = (take_score, take_idx)

            result = min(skip, take)
            dp[(i, k)] = result
            return result
        
        return solve(0, 4)[1]