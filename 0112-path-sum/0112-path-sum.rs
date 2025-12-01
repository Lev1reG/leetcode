// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
        match root {
            None => false,
            Some(r) => {
                let node = r.borrow();

                if node.left.is_none() && node.right.is_none() {
                    return node.val == target_sum;
                }
                return Self::has_path_sum(node.left.clone(), target_sum - node.val) || Self::has_path_sum(node.right.clone(), target_sum - node.val);
            }
        }
    }
}