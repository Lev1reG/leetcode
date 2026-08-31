class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        maxGap = 0
        lastOne = None

        for i in range(len(binary)):
            if binary[i] == '1':
                if lastOne is not None:
                    maxGap = max(maxGap, i - lastOne)
                lastOne = i
        
        return maxGap