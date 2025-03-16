
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root
    
    def search(self, data):
        return self._search(self.root, data)
    

    def _search(self, root, data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)
    

    def delete(self, data):
        self.root = self._delete(self.root, data)

    
    def _delete(self, root, data):
        if root is None:
            return root
        
        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.delete, data)
        else :
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = self._delete(root.right, root.data)
        return root
    
    # dfs (in order)
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)
        return

    # dfs (pre order) 
    def pre_order(self, root):
        if root:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)
        return 
    
    # dfs (post order)
    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)
        return 
    
    # bfs (leve order)
    def level_order(self, root):
        if not root:
            return 
        q = [root]

        while q:
            node = q.pop(0)
            print(node.data)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)




# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    print("Inorder traversal:")
    bst.in_order(bst.root)
    
    bst.delete(50)
    print("Inorder traversal after deletion:")
    bst.in_order(bst.root)
    search_key = 40
    if bst.search(search_key):
        print(f"{search_key} found in BST")
    else:
        print(f"{search_key} not found in BST")


        
       

