class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        if (k == 1) {
            return 0;
        }

        sort(nums.begin(), nums.end());
        int diff, min_diff = INT_MAX;

        for (int i = 0; i <= nums.size() - k; i++) {
            diff = nums[k - 1 + i] - nums[i];
            if (diff < min_diff) {
                min_diff = diff;
            }
        }

        return min_diff;
    }
};