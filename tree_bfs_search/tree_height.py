from collections import deque
def height(self, root):
    # code here
    if root is None:
        return 0
    q=deque()
    q.append(root)
    counter=0
    while q:
        levelSize=len(q)
        
        for _ in range(levelSize):
            curr=q.popleft()
            
            if curr.left is not None:
                q.append(curr.left)
                
            if curr.right is not None:
                q.append(curr.right)
        counter+=1
    return counter