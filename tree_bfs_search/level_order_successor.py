from collections import deque

def find_successor(root,key):
    if root is None:
        return root
    queue = deque()
    queue.append(key)
    while queue:
        currentNode = queue.popleft()
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        if currentNode.val == key:
            break
    return queue[0] if queue else None