from collections import deque
from collections import defaultdict
#Function to find the vertical width of a Binary Tree.
def verticalWidth(root):
    if root is None:
        return 0
    # code here
    queue = deque()
    queue.append(root)
    count_mapping = deque()
    count_mapping.append(0)
    d = defaultdict(list)
    while queue:
        currNode = queue.popleft()
        value = count_mapping.popleft()
        d[value].append(currNode.data)
        
        if currNode.left:
            queue.append(currNode.left)
            count_mapping.append(value-1)
        if currNode.right:
            queue.append(currNode.right)
            count_mapping.append(value+1)
    return len(d.keys())
