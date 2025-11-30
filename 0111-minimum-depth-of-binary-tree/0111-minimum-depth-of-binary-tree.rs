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
use std::collections::VecDeque;
use std::rc::Rc;
impl Solution {
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(r) => {
                let mut queue = VecDeque::new();
                queue.push_back((r, 1));

                while let Some((node, depth)) = queue.pop_front() {
                    if node.borrow().left.is_none() && node.borrow().right.is_none() {
                        return depth
                    }
                    let new_depth = depth + 1;
                    if node.borrow().left.is_some() {
                        queue.push_back((node.borrow().left.clone().unwrap(), new_depth));
                    }
                    if node.borrow().right.is_some() {
                        queue.push_back((node.borrow().right.clone().unwrap(), new_depth));
                    }
                }
                return 0;
            }
        }
    }
}