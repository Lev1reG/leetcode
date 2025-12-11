class Solution
{
public:
    int countCoveredBuildings(int n, std::vector<std::vector<int>> &buildings)
    {
        std::map<int, std::vector<int>> byX;
        std::map<int, std::vector<int>> byY;

        for (int i = 0; i < buildings.size(); i++)
        {
            int x = buildings[i][0];
            int y = buildings[i][1];

            byX[x].push_back(y);
            byY[y].push_back(x);
        }

        int count = 0;

        std::map<int, int> minByX, maxByX;
        std::map<int, int> minByY, maxByY;

        for (auto &pair : byX)
        {
            int x = pair.first;
            std::vector<int> &y_values = pair.second;

            minByX[x] = *std::min_element(y_values.begin(), y_values.end());
            maxByX[x] = *std::max_element(y_values.begin(), y_values.end());
        }

        for (auto &pair : byY)
        {
            int y = pair.first;
            std::vector<int> &x_values = pair.second;

            minByY[y] = *std::min_element(x_values.begin(), x_values.end());
            maxByY[y] = *std::max_element(x_values.begin(), x_values.end());
        }

        for (int i = 0; i < buildings.size(); i++)
        {
            int x = buildings[i][0];
            int y = buildings[i][1];

            if (minByX[x] < y && maxByX[x] > y && minByY[y] < x && maxByY[y] > x)
            {
                count += 1;
            }
        }

        return count;
    }
};