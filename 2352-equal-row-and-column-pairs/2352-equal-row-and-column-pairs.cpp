class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size();
        map<vector<int>, int> rowCount;
        map<vector<int>, int> colCount;

        for (int i = 0; i < n; i++) {
            rowCount[grid[i]]++;

            vector<int> col;

            for (int j = 0; j < n; j++) {
                col.push_back(grid[j][i]);
            }

            colCount[col]++;
        }

        int answer = 0;
        for (auto &pair : rowCount) {
            answer += rowCount[pair.first] * colCount[pair.first];
        }

        return answer;
    }
};