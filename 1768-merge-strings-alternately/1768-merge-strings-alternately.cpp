class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string result = "";
        int iterator = 0;
        if (word1.length() >= word2.length())
        {
            iterator = word1.length();
        }
        else
        {
            iterator = word2.length();
        }

        for (int i = 0; i < iterator; i++)
        {
            if (i < word1.length())
            {
                result.push_back(word1[i]);

                if (i < word2.length())
                {
                    result.push_back(word2[i]);
                }
            }
            else if (i < word2.length())
            {
                result.push_back(word2[i]);
            }
        }

        return result;
    }
};