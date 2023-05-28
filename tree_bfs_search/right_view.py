from collections import deque

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        queue = deque()
        ans= []
        # code here
        queue.append(root)
        while queue:
            currentLevel = deque()
            len_q = len(queue)
            for _ in range(len_q):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.data)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            ans.append(currentLevel[-1])
        return ans