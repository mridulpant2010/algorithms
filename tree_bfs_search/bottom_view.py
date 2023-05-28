from collections import defaultdict
from collections import deque


def bottomView(root):

    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    count_mapping =deque()
    count_mapping.append(0)
    d = defaultdict(int)

    while queue:
        currNode = queue.popleft()
        value = count_mapping.popleft()
        d[value] = currNode.data

        if currNode.left:
            queue.append(currNode.left)
            count_mapping.append(value-1)
        
        if currNode.right:
            queue.append(currNode.right)
            count_mapping.append(value+1)
    
    for i in sorted(d):
        print(d[i],end=",")