impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let mut carry = 1;

        for i in (0..digits.len()).rev() {
            let sum = digits[i] + carry;

            if sum == 10 {
                digits[i] = 0;
                carry = 1;
            } else {
                digits[i] = sum;
                break;
            }

            if i == 0 && carry == 1 {
                digits.insert(0, 1);
                return digits;
            }
        }

        digits
    }
}