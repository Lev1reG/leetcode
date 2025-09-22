impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 2 {
            return n;
        }

        // Fibonacci-like sequence
        let mut a = 1;
        let mut b = 2;
        let mut c = 0;
        for _ in 3..=n {
            c = a + b;
            a = b;
            b = c;
        }
        c
    }
}