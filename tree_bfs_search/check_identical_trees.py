from collections import deque
class Solution:
    #Function to check if two trees are identical.
    
    def levelOrderTraversal(self,root):
        queue = deque()
        queue.append(root)
        ans = deque()
        while queue:
            currNode = queue.popleft()
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
            ans.append(currNode.data)
        return ans
        
    def isIdentical(self,root1, root2):
        # Code here
        if root1 is None or root2 is None:
            return []
    
        ans1 = self.levelOrderTraversal(root1)
        ans2 = self.levelOrderTraversal(root2)
        if len(ans1)!=len(ans2):
            return False
        return ans1==ans2