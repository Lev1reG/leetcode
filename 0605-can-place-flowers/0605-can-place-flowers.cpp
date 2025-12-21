class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int counter = 0;

        if (flowerbed.size() == 1) {
            if (flowerbed[0] != 1) {
                counter += 1;
            }
            return counter >= n;
        }

        for (int i = 0; i < flowerbed.size(); i++) {
            if (i == 0 && flowerbed[i] != 1) {
                if(flowerbed[i + 1] != 1) {
                    counter += 1;
                    flowerbed[i] = 1;
                }
            } else if (i == flowerbed.size() - 1 && flowerbed[i] != 1) {
                if (flowerbed[i - 1] != 1) {
                    counter += 1;
                    flowerbed[i] = 1;
                }
            } else if (flowerbed[i] != 1) {
                if (flowerbed[i - 1] != 1 && flowerbed[i + 1] != 1) {
                    counter += 1;
                    flowerbed[i] = 1;
                }
            }
        }

        return counter >= n;
    }
};