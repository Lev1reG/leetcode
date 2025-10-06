impl Solution {
    pub fn count_hill_valley(nums: Vec<i32>) -> i32 {
        let mut count = 0;
        let n = nums.len();

        let mut i = 1;
        while i < (n - 1) {
            let mut left = i - 1;
            while left > 0 && nums[left] == nums[i] {
                left -= 1;
            }

            let mut right = i + 1;
            while right < n - 1 && nums[right] == nums[i] {
                right += 1;
            }

            if nums[left] != nums[i] && nums[right] != nums[i] {
                if (nums[left] < nums[i] && nums[right] < nums[i])
                    || (nums[left] > nums[i] && nums[right] > nums[i])
                {
                    count += 1;
                }
            }

            while i < n - 1 && nums[i] == nums[i + 1] {
                i += 1;
            }
            i += 1;
        }
        count
    }
}