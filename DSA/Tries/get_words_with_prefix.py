'''
write a function to retrieve all words in the Trie that start with a given prefix

algorithm
1 navigate to the prefix node, traverse until reach last char in prefix
2 Dfs traversal - to fatch all the words 
3 store the words in array and return 

'''

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    
    def __init__(self) -> None:
        self.root = Node()

    
    def add(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = Node()
            node = node.children[i]

        node.is_end=True
    

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    

    def get_words_with_prefix(self, word):
        def dfs(node, path, result):
            if node.is_end:
                result.append("".join(path))
            for char, child in node.children.items():
                dfs(child, path + [char], result)

                
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        
        result = []
        dfs(node, list(word), result)
        return result
    


        
