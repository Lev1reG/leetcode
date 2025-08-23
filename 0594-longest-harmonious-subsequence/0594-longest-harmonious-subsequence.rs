use std::collections::HashMap;

impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        let mut count_map = HashMap::new();

        for num in nums.iter() {
            *count_map.entry(*num).or_insert(0) += 1;
        }

        let mut max_len = 0;

        for (&num, &count) in &count_map {
            if let Some(&next_count) = count_map.get(&(num + 1)) {
                let total = count + next_count;
                if total > max_len {
                    max_len = total;
                }
            }
        }

        max_len
    }
}