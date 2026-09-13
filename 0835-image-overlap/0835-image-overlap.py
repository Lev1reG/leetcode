class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        coordinate_img1, coordinate_img2 = [], []

        for x in range(n):
            for y in range(n):
                if img1[x][y] == 1:
                    coordinate_img1.append((x, y))
                
                if img2[x][y] == 1:
                    coordinate_img2.append((x, y))
        
        freq = {}
        maxOverlap = 0

        for x1, y1, in coordinate_img1:
            for x2, y2 in coordinate_img2:
                dx = x1 - x2
                dy = y1 - y2

                key = (dx, dy)
                freq[key] = freq.get(key, 0) + 1
                maxOverlap = max(maxOverlap, freq[key])

        return maxOverlap