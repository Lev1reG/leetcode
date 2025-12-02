impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let mut row = vec![1];
        for _ in 0..row_index {
            row.push(1);
            for i in (1..=row.len() - 2).rev() {
                row[i] = row[i] + row[i - 1];
            }
        }

        return row;
    }
}