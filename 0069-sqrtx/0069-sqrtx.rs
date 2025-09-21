impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x < 2 {
            return x;
        }

        let initial_guess = x / 2;

        let mut guess = initial_guess;
        let mut next_guess = (guess + x / guess) / 2;
        for _ in 0..100 {
            guess = next_guess;
            next_guess = (guess + x / guess) / 2;
        }
        if next_guess * next_guess > x {
            next_guess - 1
        } else {
            next_guess
        }
    }
}