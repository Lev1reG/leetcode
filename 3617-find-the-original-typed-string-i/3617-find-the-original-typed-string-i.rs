impl Solution {
    pub fn possible_string_count(word: String) -> i32 {
        let mut groups: Vec<(char, usize)> = Vec::new();
        let mut chars = word.chars().peekable();

        while let Some(ch) = chars.next() {
            let mut count = 1;
            while let Some(&next) = chars.peek() {
                if next == ch {
                    count += 1;
                    chars.next();
                } else {
                    break;
                }
            }
            groups.push((ch, count));
        }

        let mut total = 1;
        for &(_, count) in &groups {
            if count >= 2 {
                total += count as i32 - 1;
            }
        }

        total
    }
}