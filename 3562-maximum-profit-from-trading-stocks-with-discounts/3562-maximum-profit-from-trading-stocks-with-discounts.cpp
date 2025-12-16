class Solution
{
public:
    int maxProfit(int n, vector<int> &present, vector<int> &future, vector<vector<int>> &hierarchy, int budget)
    {
        vector<vector<int>> hierarchyGraph(n);

        for (auto edge : hierarchy)
        {
            int boss = edge[0] - 1;
            int employee = edge[1] - 1;

            hierarchyGraph[boss].push_back(employee);
        }

        auto maxProfitSubtree = [&](auto &&self, int currentEmployee) -> tuple<vector<int>, vector<int>, int>
        {
            int fullPrice = present[currentEmployee];
            int discountPrice = present[currentEmployee] / 2;

            vector<int> parentNotBuy(budget + 1, 0);
            vector<int> parentBuy(budget + 1, 0);

            vector<int> childrenProfitNoDiscount(budget + 1, 0);
            vector<int> childrenProfitDiscount(budget + 1, 0);

            int subTreeSize = fullPrice;

            for (int child : hierarchyGraph[currentEmployee])
            {
                auto [childNotBuy, childBuy, childSize] = self(self, child);

                subTreeSize += childSize;

                for (int budgetAmount = budget; budgetAmount >= 0; budgetAmount--)
                {
                    for (int budgetForChild = 0; budgetForChild <= min(childSize, budgetAmount); budgetForChild++)
                    {
                        int budgetPreviousChildren = budgetAmount - budgetForChild;
                        childrenProfitNoDiscount[budgetAmount] = max(childrenProfitNoDiscount[budgetAmount], childrenProfitNoDiscount[budgetPreviousChildren] + childNotBuy[budgetForChild]);
                        childrenProfitDiscount[budgetAmount] = max(childrenProfitDiscount[budgetAmount], childrenProfitDiscount[budgetPreviousChildren] + childBuy[budgetForChild]);
                    }
                }
            }

            for (int budgetAmount = 0; budgetAmount <= budget; budgetAmount++)
            {
                parentNotBuy[budgetAmount] = childrenProfitNoDiscount[budgetAmount];
                parentBuy[budgetAmount] = childrenProfitNoDiscount[budgetAmount];

                if (budgetAmount >= discountPrice)
                {
                    int profitFromEmployee = future[currentEmployee] - discountPrice;
                    int totalProfit = profitFromEmployee + childrenProfitDiscount[budgetAmount - discountPrice];
                    parentBuy[budgetAmount] = max(parentBuy[budgetAmount], totalProfit);
                }

                if (budgetAmount >= fullPrice)
                {
                    int profitFromEmployee = future[currentEmployee] - fullPrice;
                    int totalProfit = profitFromEmployee + childrenProfitDiscount[budgetAmount - fullPrice];
                    parentNotBuy[budgetAmount] = max(parentNotBuy[budgetAmount], totalProfit);
                }
            }

            return {parentNotBuy, parentBuy, subTreeSize};
        };

        auto [parentNotBuy, parentBuy, size] = maxProfitSubtree(maxProfitSubtree, 0);
        return parentNotBuy[budget];
    }
};