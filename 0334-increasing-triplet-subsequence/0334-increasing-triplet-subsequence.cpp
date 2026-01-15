class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int smallest = INT_MAX, middle = INT_MAX;

        for (int num : nums) {
            if (!(num > smallest)) {
                smallest = num;
            } else if (!(num > middle)) {
                middle = num;
            } else {
                return true;
            }
        }

        return false;
    }
};