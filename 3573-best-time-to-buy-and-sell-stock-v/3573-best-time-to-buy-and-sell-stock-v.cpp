class Solution {
public:
    long long maximumProfit(vector<int>& prices, int k) {
        int n = prices.size();
        long long result;
        vector<vector<vector<long long>>> memo(n, vector<vector<long long>>(k+1, vector<long long>(3, -1)));
        
        function <long long(int, int, int)> solve = [&](int day, int transactionDone, int position) -> long long {
            if (day == n) {
                if (position == 0) {
                    return 0;
                } 
                if (position == 1) {
                    return -1000000000LL;
                }
                if (position == 2) {
                    return -1000000000LL;
                }
            }

            if (transactionDone == k) {
                if (position == 0) {
                    return solve(day+1, k, 0);
                }
                if (position == 1) {
                    return -1000000000LL;
                }
                if (position == 2) {
                    return -1000000000LL;
                }
            }

            if (memo[day][transactionDone][position] != -1) {
                return memo[day][transactionDone][position];
            }

            if (position == 0) {
                result = max({
                    solve(day+1, transactionDone, 0),
                    solve(day+1, transactionDone, 1) - prices[day],
                    solve(day+1, transactionDone, 2) + prices[day]
                });
            }

            if (position == 1) {
                result = max(
                    solve(day+1, transactionDone, 1),
                    solve(day+1, transactionDone+1, 0) + prices[day]
                );
            }

            if (position == 2) {
                result = max(
                    solve(day+1, transactionDone, 2),
                    solve(day+1, transactionDone+1, 0) - prices[day]
                );
            }

            memo[day][transactionDone][position] = result;

            return result;
        };

        return solve(0, 0, 0);
    }
};