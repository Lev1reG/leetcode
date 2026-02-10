class Solution {
public:
    bool closeStrings(string word1, string word2) {
        vector<int> list1;
        vector<int> list2;

        if (word1.size() != word2.size()) {
            return false;
        }

        int freq1[26] = {0};
        int freq2[26] = {0};

        for (char c : word1) {
            freq1[c - 'a']++;
        }

        for (char c : word2) {
            freq2[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (!(freq1[i] == 0) && (freq2[i] == 0)) {
                return false;
            } else {
                list1.push_back(freq1[i]);
                list2.push_back(freq2[i]);
            }
        }

        sort(list1.begin(), list1.end());
        sort(list2.begin(), list2.end());

        if (list1 == list2) {
            return true;
        }

        return false;
    }
};