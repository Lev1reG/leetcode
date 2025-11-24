impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut results: Vec<bool> = vec![];
        let mut old_remainder = 0;
        let mut new_remainder;

        for num in &nums {
            new_remainder = (old_remainder*2 + num) % 5;
            if new_remainder == 0 {
                results.push(true);
            } else {
                results.push(false);
            }
            old_remainder=new_remainder
        }

        results
    }
}