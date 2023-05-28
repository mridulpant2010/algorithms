#User function Template for python3
from collections import deque
"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Your code here
        queue = deque()
        queue.append(root)
        ans = []
        level_count = 1
        while queue:
            len_q = len(queue)
            currentLevel = deque()
            for _ in range(len_q):
                currentNode = queue.popleft()
                if level_count%2==0:
                    currentLevel.appendleft(currentNode.data)
                else:
                    currentLevel.append(currentNode.data)
                    
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            level_count+=1
            ans.extend(currentLevel)
        return ans