class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for y in range(1, col):
            grid[0][y] += grid[0][y - 1]
        
        for x in range(1, row):
            grid[x][0] += grid[x - 1][0]

        for x in range(1, row):
            for y in range(1, col):
                grid[x][y] += min(grid[x][y - 1], grid[x - 1][y])
        
        return grid[-1][-1]
                