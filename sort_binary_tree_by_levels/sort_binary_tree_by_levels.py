class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if not node.value:
        return []

    result = []
    q = [node]

    while q:
        curr = q.pop(0)
        result.append(curr.value)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

    return result
