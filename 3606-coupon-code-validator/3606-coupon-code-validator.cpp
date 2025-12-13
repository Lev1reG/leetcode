class Solution
{
public:
    vector<string> validateCoupons(vector<string> &code, vector<string> &businessLine, vector<bool> &isActive)
    {
        unordered_map<string, int> categories = {
            {"electronics", 0},
            {"grocery", 1},
            {"pharmacy", 2},
            {"restaurant", 3}};

        vector<pair<string, string>> validCoupons;

        for (int i = 0; i < code.size(); i++)
        {
            if (isActive[i] == true)
            {
                if (categories.count(businessLine[i]))
                {
                    if (validateCode(code[i]))
                    {
                        validCoupons.push_back({code[i], businessLine[i]});
                    }
                }
            }
        }

        sort(validCoupons.begin(), validCoupons.end(), [&](pair<string, string> a, pair<string, string> b) {
            if (categories[a.second] != categories[b.second]) {
                return categories[a.second] < categories[b.second];
            }

            return a.first < b.first;
        });

        vector<string> result;
        for (auto& p : validCoupons) {
            result.push_back(p.first);
        }

        return result;
    }

    bool validateCode(string code)
    {
        if (!code.empty())
        {
            return all_of(code.begin(), code.end(), [](char c)
                   { return isalnum(c) || c == '_'; });
        }
        return false;
    }
};