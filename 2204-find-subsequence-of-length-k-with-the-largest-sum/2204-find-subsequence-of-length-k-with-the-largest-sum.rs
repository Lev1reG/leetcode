impl Solution {
    pub fn max_subsequence(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut indexed: Vec<(i32, usize)> = nums.iter().cloned().enumerate().map(|(i, v)| (v, i)).collect();
        indexed.sort_by(|a, b| b.0.cmp(&a.0));

        let mut top_k = indexed[..k as usize].to_vec();
        top_k.sort_by(|a, b| a.1.cmp(&b.1));
        
        let result: Vec<i32> = top_k.iter().map(|&(v, _)| v).collect();
        return result;
    }
}