impl Solution {
    pub fn k_mirror(k: i32, n: i32) -> i64 {
        let mut count = 0;
        let mut total = 0;
        let mut length = 1;
        
        while count < n {
            // Generate palindromes of current length in order
            if length == 1 {
                // Single digit palindromes: 1-9
                for digit in 1..=9 {
                    if count >= n { break; }
                    let base_k = to_base_k(digit, k as u32);
                    if is_palindrome(&base_k) {
                        total += digit as i64;
                        count += 1;
                    }
                }
            } else {
                // Multi-digit palindromes
                let half_len = (length + 1) / 2;
                let start = 10_u64.pow(half_len as u32 - 1);
                let end = 10_u64.pow(half_len as u32);
                
                for root in start..end {
                    if count >= n { break; }
                    let palindrome = create_palindrome(root, length % 2 == 1);
                    let base_k = to_base_k(palindrome, k as u32);
                    if is_palindrome(&base_k) {
                        total += palindrome as i64;
                        count += 1;
                    }
                }
            }
            length += 1;
            if length > 18 { break; } // Safety break for large numbers
        }
        
        total
    }
}

fn is_palindrome(s: &str) -> bool {
    s.chars().eq(s.chars().rev())
}

fn create_palindrome(root: u64, is_odd: bool) -> u64 {
    let root_str = root.to_string();
    let mut palindrome = root_str.clone();
    
    if is_odd {
        // For odd length, exclude the middle digit when mirroring
        palindrome.push_str(&root_str[..root_str.len()-1].chars().rev().collect::<String>());
    } else {
        // For even length, mirror the entire root
        palindrome.push_str(&root_str.chars().rev().collect::<String>());
    }
    
    palindrome.parse().unwrap()
}

fn to_base_k(mut num: u64, k: u32) -> String {
    if num == 0 {
        return "0".to_string();
    }

    let mut digits = Vec::new();
    while num > 0 {
        let digit = (num % k as u64) as u32;
        digits.push(char::from_digit(digit, k).unwrap());
        num /= k as u64;
    }

    digits.iter().rev().collect()
}