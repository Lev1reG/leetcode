class Solution {
public:
    bool isSubsequence(string s, string t) {
        int pointerS = 0, pointerT = 0;

        if (s.size() == 0) {
            return true;
        }

        while (pointerT < t.size()) {
            if (s[pointerS] == t[pointerT]) {
                pointerS++;
                if (pointerS == s.size()) {
                    return true;
                }
            }
            pointerT++;
        }

        return false;
    }
};