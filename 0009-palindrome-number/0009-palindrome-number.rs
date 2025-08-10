impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x % 10 == 0 && x != 0) {
            return false;
        }

        let mut reversed = 0;
        let mut remaining = x;

        while remaining > reversed {
            reversed = reversed * 10 + remaining % 10;
            remaining /= 10;
        }

        if remaining == reversed || remaining == reversed / 10 {
            return true;
        } else {
            return false;
        }
    }
}