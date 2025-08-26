impl Solution {
    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut list1 = list1;
        let mut list2 = list2;

        let mut dummy = Box::new(ListNode::new(0));
        let mut tail = &mut dummy;

        while list1.is_some() && list2.is_some() {
            let l1_val = list1.as_ref().unwrap().val;
            let l2_val = list2.as_ref().unwrap().val;

            if l1_val < l2_val {
                let next = list1.as_mut().unwrap().next.take();
                tail.next = list1;
                list1 = next;
            } else {
                let next = list2.as_mut().unwrap().next.take();
                tail.next = list2;
                list2 = next;
            }

            tail = tail.next.as_mut().unwrap();
        }

        tail.next = if list1.is_some() { list1 } else { list2 };

        dummy.next
    }
}