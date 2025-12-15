class Solution {
public:
    long long getDescentPeriods(vector<int> &prices)
    {
        long long periodLength = 1;
        long long descentPeriodsCount = 0;

        for (int i = 1; i < prices.size(); i++)
        {
            if (prices[i] == prices[i - 1] - 1)
            {
                periodLength += 1;
            }
            else
            {
                descentPeriodsCount += (periodLength * (periodLength + 1) / 2);
                periodLength = 1;
            }
        }

        descentPeriodsCount += (periodLength * (periodLength + 1) / 2);

        return descentPeriodsCount;
    }
};