# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def sumOfSubtree(node: TreeNode):
            if not node:
                return 0, 0
            
            leftSum, leftCount = sumOfSubtree(node.left)
            rightSum, rightCount = sumOfSubtree(node.right)

            totalSum = leftSum + rightSum + node.val
            totalCount = leftCount + rightCount + 1

            if (totalSum // totalCount) == node.val:
                self.match_count += 1
            
            return totalSum, totalCount
        
        self.match_count = 0
        sumOfSubtree(root)

        return self.match_count