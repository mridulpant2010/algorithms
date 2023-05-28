class Solution:
    def hasPathSum(self,root, S):
        # code here
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return root.data==S
        return self.hasPathSum(root.left,S-root.data) or self.hasPathSum(root.right,S-root.data)
