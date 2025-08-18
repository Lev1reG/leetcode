impl Solution {
    pub fn divide_string(s: String, k: i32, fill: char) -> Vec<String> {
    let k = k as usize;
    let chars: Vec<char> = s.chars().collect();
    let mut result = Vec::new();
    let mut i = 0;

    while i < chars.len() {
            let mut group: Vec<char> = chars[i..chars.len().min(i + k)].to_vec();

            while group.len() < k {
                group.push(fill);
            }

            result.push(group.into_iter().collect());
            i += k;
        }

        return result;
    }
}