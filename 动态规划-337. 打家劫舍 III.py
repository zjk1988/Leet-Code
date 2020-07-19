# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.rob1(root)
        return max(res[0],res[1])
    def rob1(self,root):
        if root==None:
            return (0,0)
        left = self.rob1(root.left)
        right = self.rob1(root.right)
        not_do = max(left[0],left[1]) + max(right[0],right[1])
        do = root.val + left[0] + right[0]
        return not_do,do