# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        idx = 1
        first_cp, prev_cp = -1, -1
        minDistance = float("inf")

        while curr.next:
            is_critical_point = (
                curr.val > prev.val and curr.val > curr.next.val
            ) or (
                curr.val < prev.val and curr.val < curr.next.val
            )

            if is_critical_point:
                if first_cp == -1:
                    first_cp = idx
                else:
                    minDistance = min(minDistance, idx - prev_cp)
                prev_cp = idx
            
            prev = curr
            curr = curr.next
            idx += 1
        
        if minDistance == float("inf"):
            return [-1, -1]
        
        return [minDistance, (prev_cp - first_cp)]

