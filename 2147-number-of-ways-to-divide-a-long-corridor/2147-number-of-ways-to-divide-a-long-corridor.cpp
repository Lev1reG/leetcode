class Solution {
public:
    int numberOfWays(string corridor) {
        int total_s = count(corridor.begin(), corridor.end(), 'S');
        long long count = 1;
        int seatCount = 0;
        int plantGap = 0;
        const int MOD = 1000000007;

        if (total_s % 2 != 0 || total_s == 0) {
            return 0;
        } else {
            for (char c : corridor) {
                if (c == 'S') {
                    seatCount += 1;
                    if (seatCount > 2 && seatCount % 2 == 1) {
                        count = (count * (plantGap + 1)) % MOD;
                        plantGap = 0;
                    }
                } else if (c == 'P') {
                    if (seatCount >= 2 && seatCount % 2 == 0) {
                        plantGap += 1;
                    }
                }
            }
        }

        return count;
    }
};