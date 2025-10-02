impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![vec![1]];

        for i in 1..num_rows {
            let mut row = vec![1];
            let prev_row = &result[i as usize - 1];
            for j in 0..prev_row.len() - 1 {
                row.push(prev_row[j] + prev_row[j + 1]);
            }
            row.push(1);
            result.push(row);
        }
        result
    }
}