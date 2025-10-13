impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut result = String::new();
        let mut current_char = s.chars().next();
        let mut count = 0;

        for c in s.chars() {
            if Some(c) == current_char {
                count += 1;
            } else {
                current_char = Some(c);
                count = 1;
            }

            if count < 3 {
                result.push(c);
            }
        }

        result
    }
}