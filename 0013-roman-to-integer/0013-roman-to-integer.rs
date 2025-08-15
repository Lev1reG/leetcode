use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let rules = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]);

        let mut total = 0;
        let roman: Vec<char> = s.chars().collect();

        for i in 0..roman.len() {
            let curr = rules[&roman[i]];

            if i + 1 < roman.len() && rules[&roman[i + 1]] > curr {
                total -= curr;
            } else {
                total += curr;
            }
        }

        return total;
    }
}