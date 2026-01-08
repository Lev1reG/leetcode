class Solution {
public:
    string reverseVowels(string s)
    {
        std::stack<char> vowels;

        for (char c : s)
        {
            if (isVowels(c))
            {
                vowels.push(c);
            }
        }

        for (int i = 0; i < s.length(); i++) {
            if (isVowels(s[i])) {
                s[i] = vowels.top();
                vowels.pop();
            }
        }

        return s;
    }

    bool isVowels(char c)
    {
        switch (c)
        {
        case 'a':
        case 'i':
        case 'u':
        case 'e':
        case 'o':
        case 'A':
        case 'I':
        case 'U':
        case 'E':
        case 'O':
            return true;
            break;
        default:
            return false;
            break;
        }
    }
};