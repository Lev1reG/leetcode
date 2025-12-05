impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let total_sum: i32 = nums.iter().sum();

        if total_sum % 2 == 0 {
            return (nums.len() - 1) as i32;
        }

        return 0
    }
}