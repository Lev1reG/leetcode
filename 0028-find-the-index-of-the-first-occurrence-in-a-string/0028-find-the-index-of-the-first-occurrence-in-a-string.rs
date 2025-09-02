impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if haystack.len() < needle.len() {
            return -1;
        }

        for i in 0..=haystack.len() - needle.len() {
            let substring = &haystack[i..i + needle.len()];
            if substring == needle {
                return i as i32;
            }
        }

        -1
    }
}
