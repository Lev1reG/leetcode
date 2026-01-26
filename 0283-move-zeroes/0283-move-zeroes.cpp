class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int writePos = 0, readPos = 0;

        if (nums.size() == 1) {
            return;
        }

        while (readPos < nums.size()) {
            if (nums[readPos] != 0) {
                swap(nums[writePos], nums[readPos]);
                writePos++;
            }
            readPos++;
        }
        
        return;
    }
};