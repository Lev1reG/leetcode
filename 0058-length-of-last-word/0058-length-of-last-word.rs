impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut length: i32 = 0;
        for c in s.chars().rev() {
            if c == ' ' {
                if length > 0 {
                    break;
                }
            } else {
                length += 1;
            }
        }

        length
    }
}