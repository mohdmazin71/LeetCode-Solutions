class Solution:
    def hasPathSum(self, root, targetSum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)