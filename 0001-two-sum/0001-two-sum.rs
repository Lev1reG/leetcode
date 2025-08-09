use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, usize> = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            let complement = target - num;
            if seen.contains_key(&complement) {
                return vec![seen[&complement] as i32, i as i32];
            }
            seen.insert(*num, i);
        }

        vec![]
    }
}