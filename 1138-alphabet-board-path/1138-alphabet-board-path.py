class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pair_idx = defaultdict(list)

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        path = ""

        row = 0
        for i in range(26):
            pair_idx[alphabet[i]] = [row, i % 5]
            if i % 5 == 4:
                row += 1
        
        i = 0
        j = 0
        for c in target:
            posTarget = pair_idx[c]
            moveX = posTarget[0] - i
            moveY = posTarget[1] - j

            if moveX == 0 and moveY == 0:
                path += '!'
                continue
            
            if moveY < 0:
                path += 'L'*(-moveY)
            if moveX >= 0:
                path += 'D'*moveX
            else:
                path += 'U'*(-moveX)
            if moveY >= 0:
                path += 'R'*moveY

            path += '!'
            i = posTarget[0]
            j = posTarget[1]
        
        return path
        
        
                