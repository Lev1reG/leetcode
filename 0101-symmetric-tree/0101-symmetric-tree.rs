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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match root {
            None => true,
            Some(node) => {
                Self::is_mirror(node.borrow().left.clone(), node.borrow().right.clone())
            }
        }
    }

    pub fn is_mirror(
        left: Option<Rc<RefCell<TreeNode>>>,
        right: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (left, right) {
            (None, None) => true,
            (None, Some(_)) | (Some(_), None) => false,
            (Some(l), Some(r)) => {
                if l.borrow().val == r.borrow().val
                    && Self::is_mirror(l.borrow().left.clone(), r.borrow().right.clone())
                    && Self::is_mirror(l.borrow().right.clone(), r.borrow().left.clone())
                {
                    true
                } else {
                    false
                }
            }
        }
    }
}