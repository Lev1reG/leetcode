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
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        match root {
            None => {
                return vec![];
            }
            Some(node) => {
                let mut result = vec![];
                let borrowed_node = node.borrow();

                let left_values = Self::inorder_traversal(borrowed_node.left.clone());
                let current_value = borrowed_node.val;
                let right_values = Self::inorder_traversal(borrowed_node.right.clone());

                result.extend(left_values);
                result.push(current_value);
                result.extend(right_values);
                return result;
            }
        }
    }
}