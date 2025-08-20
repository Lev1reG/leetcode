use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let dictionary = HashMap::from([
            ('(', ')'),
            ('{', '}'),
            ('[', ']'),
        ]);

        let mut stack = Vec::new();
        for ch in s.chars() {
            if dictionary.contains_key(&ch) {
                stack.push(ch);
            } else {
                if stack.is_empty() {
                    return false;
                }
                let last = stack.pop().unwrap();
                if dictionary.get(&last) != Some(&ch) {
                    return false;
                }
            }
        }
        stack.is_empty()
    }
}