class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        int complement, operations = 0;

        for (int num : nums) {
            complement = k - num;

            if (map[complement]) {
                map[complement]--;
                operations++;
            } else {
                map[num] += 1;
            }
        }

        return operations;
    }
};