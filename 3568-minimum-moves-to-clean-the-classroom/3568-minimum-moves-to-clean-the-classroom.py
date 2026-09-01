class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        row = len(classroom)
        column = len(classroom[0])
        # Scan grid
        litter_id = {}
        litter_count = 0
        for r in range(row):
            for c in range(column):
                if classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1
                if classroom[r][c] == 'S':
                    Sx, Sy = r, c
        full_mask = (1 << litter_count) - 1

        if full_mask == 0:
            return 0
        
        queue = deque([(Sx, Sy, 0, energy, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        bestEnergy = [[[-1] * (1 << litter_count) for _ in range(column)] for _ in range(row)]
        bestEnergy[Sx][Sy][0] = energy

        while queue:
            r, c, mask, e, steps = queue.popleft()
            if mask == full_mask:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < column:
                    if classroom[nr][nc] == 'X':
                        continue
                    
                    rem_e = e - 1
                    if rem_e < 0:
                        continue
                    
                    if classroom[nr][nc] == 'L':
                        next_mask = mask | (1 << litter_id[(nr, nc)])
                    else:
                        next_mask = mask
                    
                    if next_mask == full_mask:
                        return steps + 1
                    
                    if rem_e == 0 and classroom[nr][nc] != 'R':
                        continue
                    
                    if classroom[nr][nc] == 'R':
                        next_e = energy
                    else:
                        next_e = rem_e
                    
                    if next_e > bestEnergy[nr][nc][next_mask]:
                        bestEnergy[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))

        if len(queue) == 0:
            return -1        