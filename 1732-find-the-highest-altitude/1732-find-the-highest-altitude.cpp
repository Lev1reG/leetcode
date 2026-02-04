class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int maxAlt = 0, current = 0;

        for (int gained : gain) {
            current += gained;

            maxAlt = max(maxAlt, current);
        }

        return maxAlt;
    }
};