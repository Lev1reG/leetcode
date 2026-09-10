# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def sumOfSubtree(node: TreeNode):
            nonlocal match_count
            if not node:
                return 0, 0
            
            leftSum, leftCount = sumOfSubtree(node.left)
            rightSum, rightCount = sumOfSubtree(node.right)

            totalSum = leftSum + rightSum + node.val
            totalCount = leftCount + rightCount + 1

            if (totalSum // totalCount) == node.val:
                match_count += 1
            
            return totalSum, totalCount
        
        match_count = 0
        sumOfSubtree(root)

        return match_count