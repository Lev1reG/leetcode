impl Solution {
    pub fn kth_character(k: i32) -> char {
        let mut word = String::from("a");
        while word.len() < k as usize {
            let mut next_part = String::new();

            for c in word.chars() {
                next_part.push(Self::next_char(c));
            }

            word.push_str(&next_part);
        } 

        word.chars().nth(k as usize - 1).unwrap()
    }

    pub fn next_char(c: char) -> char {
        if c == 'z' {
            'a'        
        } else {
            ((c as u8) + 1) as char
        }
    }
}
