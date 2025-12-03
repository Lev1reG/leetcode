impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price = prices[0];
        let mut max_profit: i32= 0;

        for i in 0..prices.len() {
            if min_price > prices[i] {
                min_price = prices[i];
            }

            if max_profit < (prices[i] - min_price) {
                max_profit = prices[i] - min_price;
            }
        }

        return max_profit
    }
}