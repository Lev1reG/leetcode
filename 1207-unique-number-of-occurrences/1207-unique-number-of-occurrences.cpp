class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> occurences;
        unordered_set<int> setOccurences;

        for (int num : arr) {
            occurences[num]++;
        }

        for (const auto& pair : occurences) {
            setOccurences.insert(pair.second);
        }

        if (occurences.size() == setOccurences.size()) {
            return true;
        }

        return false;
    }
};