class Solution {
public:
    int compress(vector<char>& chars) {
        int read = 0, write = 0, count;
        char currentChar;
        string countStr;
        int length = chars.size();

        while (read < length) {
            count = 1;
            currentChar = chars[read];

            while (read + 1 < length && chars[read] == chars[read + 1]) {
                count++;
                read++;
            }

            chars[write++] = currentChar;
            if (count > 1) {
                countStr = to_string(count);
                for (char digit : countStr) {
                    chars[write++] = digit;
                }
            }
            read++;
        }

        return write;
    }
};