class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int start = 1;
        int max_sum, current_sum;
        double result;

        for (int i = 0; i < k; i++) {
            current_sum += nums[i];
        }
        max_sum = current_sum;

        while ((start + k - 1) < nums.size()) {
            current_sum = current_sum - nums[start - 1] + nums[start + k - 1];
            if (current_sum > max_sum) {
                max_sum = current_sum;
            }
            start++;
        }
        result = double(max_sum) / k;

        return result;
    }
};