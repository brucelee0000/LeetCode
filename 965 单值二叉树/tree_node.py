# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        执行用时：12 ms, 在所有 Python 提交中击败了99.37%的用户
        内存消耗：12.6 MB, 在所有 Python 提交中击败了100.00%的用户
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
