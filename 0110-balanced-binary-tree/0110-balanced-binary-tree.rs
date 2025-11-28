use std::cmp::max;
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
       Self::helper(root) != -1
    }

    fn helper(node: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match node {
            None => 0,
            Some(n) => {
                let left_height = Self::helper(n.borrow().left.clone());
                let right_height = Self::helper(n.borrow().right.clone());

                if left_height == -1 || right_height == -1 {
                    return -1;
                }

                if (left_height - right_height).abs() > 1 {
                    return -1;
                }

                return 1 + max(left_height, right_height);
            }
        }
    }
}