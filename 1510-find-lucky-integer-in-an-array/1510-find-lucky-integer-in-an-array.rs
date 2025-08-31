use std::collections::HashMap;

impl Solution {
    pub fn find_lucky(arr: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();

        for &num in &arr {
            *freq.entry(num).or_insert(0) += 1;
        }

        let mut lucky = -1;
        for (&num, &count) in &freq {
            if num == count && num > lucky {
                lucky = num;
            }
        }

        lucky
    }
}