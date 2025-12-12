class Solution {
public:
    string convertToTitle(int columnNumber) {
        string columnTitle;
        int remainder;

        while (columnNumber > 0) {
            columnNumber = columnNumber - 1;
            remainder = columnNumber % 26;
            columnTitle = (char)('A' + remainder) + columnTitle;
            columnNumber = columnNumber / 26;
        }

        return columnTitle;
    }
};