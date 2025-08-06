impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut min_so_far: i32 = nums[0];
        let mut max_diff: i32 = -1;

        for (i, num) in nums.iter().enumerate() {
            if num > &min_so_far {
                let diff: i32 = num - min_so_far;

                if diff > max_diff {
                    max_diff = diff;
                }
            } else {
                min_so_far = *num;
            }
        }

        return max_diff;
    }
}