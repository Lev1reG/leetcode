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
// Recursive Solution
// impl Solution {
//     pub fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
//         let mut result: Vec<i32> = Vec::new();
//         Self::helper(root, &mut result);
//         result
//     }

//     fn helper(node: Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
//         if let Some(n) = node {
//             let n_borrowed = n.borrow();
//             result.push(n_borrowed.val);
//             Self::helper(n_borrowed.left.clone(), result);
//             Self::helper(n_borrowed.right.clone(), result);
//         }
//     }
// }

// Iterative Solution
impl Solution {
    pub fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        let mut stack = Vec::new();

        if let Some(r) = root {
            stack.push(r);
        }

        while !stack.is_empty() {
            if let Some(n) = stack.pop() {
                let n_borrowed = n.borrow();
                result.push(n_borrowed.val);
                if let Some(right) = &n_borrowed.right {
                    stack.push(right.clone());
                }
                if let Some(left) = &n_borrowed.left {
                    stack.push(left.clone());
                }
            }
        }

        result
    }
}