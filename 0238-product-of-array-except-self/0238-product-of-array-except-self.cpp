class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int nums_size = nums.size();
        vector<int> left(nums_size, 1);
        vector<int> right(nums_size, 1);

        for (int i = 1; i < nums_size; i++) {
            left[i] = left[i - 1] * nums[i - 1];
        }

        for (int i = nums_size - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < nums_size; i++) {
            nums[i] = left[i] * right[i];
        }

        return nums;
    }
};