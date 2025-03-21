'''
question -> remove word from tries data structures 

deletion of word from tries algorithm 
iterate through the tries child nodes if the char of the give word is present else return 
go to the last node check if it is the end character , change it false , if there is no children del it 
do the same for all 

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
    

    def delete_helper(self, node, word, depth):
        if depth == len(word):
            if node.is_end:
                node.is_end = False
                if not node.children:
                    del node
                    return True
            return False
        
        char = word[depth]
        if char not in node.children:
            return False 
        
        if self.delete_helper(node.children[char], word, depth + 1):
            del node.children[char]
            return not node.is_end and not node.children
        
        return False
    

    def delete(self, word):
        if not word:return 
        self.delete_helper(self.root,word,0)



t = Trie()
t.add('rahul')
t.add('rajeev')
t.add('name')
print(t.search('rahul'))
print(t.search('rah'))
t.delete('rahul')
print(t.search('rahul'))