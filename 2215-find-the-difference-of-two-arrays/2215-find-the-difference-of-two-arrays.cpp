class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> nums1set(nums1.begin(), nums1.end());
        unordered_set<int> nums2set(nums2.begin(), nums2.end());
        vector<int> result1, result2;
        vector<vector<int>> result;

        for (int num : nums1set) {
            if (!(nums2set.contains(num))) {
                result1.push_back(num);
            }
        }

        for (int num : nums2set) {
            if (!(nums1set.contains(num))) {
                result2.push_back(num);
            }
        }

        result.push_back(result1);
        result.push_back(result2);

        return result;
    }
};