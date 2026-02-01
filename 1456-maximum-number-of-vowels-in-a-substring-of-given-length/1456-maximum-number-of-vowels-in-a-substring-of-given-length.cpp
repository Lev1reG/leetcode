class Solution {
public:
    int maxVowels(string s, int k) {
        int start = 1;
        int currentCount = 0;
        int maxCount = 0;

        for (int i = 0; i < k; i++) {
            if (isVowels(s[i])) {
                currentCount += 1;
            }
        }
        maxCount = currentCount;

        while (start + k <= s.size()) {
            if (isVowels(s[start - 1])) {
                currentCount -= 1;
            }
            if (isVowels(s[start + k - 1])) {
                currentCount += 1;
            }
            if (currentCount > maxCount) {
                maxCount = currentCount;
            }
            start++;
        }

        return maxCount;
    }

    bool isVowels(char c) {
        return c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o';
    }
};