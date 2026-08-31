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
        crit_point = []
        minDistance = inf

        while curr.next:
            is_local_max = curr.val > prev.val and curr.val > curr.next.val
            is_local_min = curr.val < prev.val and curr.val < curr.next.val

            if is_local_max or is_local_min:
                crit_point.append(idx)
            
            prev = curr
            curr = curr.next
            idx += 1
        
        if len(crit_point) < 2:
            return [-1, -1]
        
        for i in range(len(crit_point) - 1):
            diff = crit_point[i + 1] - crit_point[i]
            minDistance = min(minDistance, diff)
        
        return [minDistance, (crit_point[-1] - crit_point[0])]

