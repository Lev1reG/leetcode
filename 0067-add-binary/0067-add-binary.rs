impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut result = String::new();
        let mut carry = 0;
        let mut i = a.len() as i32 - 1;
        let mut j = b.len() as i32 - 1;

        while i >= 0 || j >= 0 || carry > 0 {
            let mut sum = carry;

            let digit_a = if i >= 0 {
                a.chars().nth(i as usize).unwrap().to_digit(2).unwrap() as i32
            } else {
                0
            };

            let digit_b = if j >= 0 {
                b.chars().nth(j as usize).unwrap().to_digit(2).unwrap() as i32
            } else {
                0
            };

            sum += digit_a + digit_b;
            result.push(char::from_digit((sum % 2) as u32, 10).unwrap());
            carry = sum / 2;

            i -= 1;
            j -= 1;
        }

        result.chars().rev().collect()
    }
}