impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let input: Vec<char> = s.chars().collect();

        if input.len() == 0 || input.len() == 1 {
            return true;
        }

        let mut left: usize = 0;
        let mut right = input.len() - 1;

        while left < right {
            while left < right && !input[left].is_alphanumeric() {
                left += 1;
            }

            while left < right && !input[right].is_alphanumeric() {
                right -= 1;
            }

            if left < right && input[left].to_ascii_lowercase() != input[right].to_ascii_lowercase()
            {
                return false;
            }

            if left >= right {
                break;
            }

            left += 1;
            right -= 1;
        }

        return true;
    }
}