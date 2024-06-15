


def deletion(node, val):
    if node is None:
        return None

    if node.root < val:
        node.right = deletion(node.right, val)
    elif node.root > val:
        node.left = deletion(node.left, val)
    else:
        if not node.right:
            return node.left
        if not node.left:
            return node.right

        # Find the smallest value in the right subtree
        temp = node.right
        while temp.left:
            temp = temp.left

        # Replace the node's value with the smallest value
        node.root = temp.root

        # Delete the smallest value in the right subtree
        node.right = deletion(node.right, temp.root)

    return node
