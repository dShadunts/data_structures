import string


class SortedTrieNode:
    def __init__(self, char):
        self.char = char
        self.children = [None] * 26
        self.indices = []

    def get_child(self, char):
        if char < 'a' or char > 'z':
            return None
        return self.children[ord(char) - ord('a')]

    def add_child(self, char):
        if char < 'a' or char > 'z':
            return None
        node = SortedTrieNode(char)
        self.children[ord(char) - ord('a')] = node

    def add_index(self, i):
        self.indices.append(i)


class SortedTrie:
    def __init__(self):
        self.root = SortedTrieNode('*')

    def add(self, word, index):
        node = self.root
        for char in word:
            if node.get_child(char) is None:
                node.add_child(char)
            # go to next node
            node = node.get_child(char)
        node.add_index(index)

    # Sort array of strings using trie
    def print_sorted(self, arr):
        self.preorder(self.root, arr)

    def preorder(self, node, words):
        if node is None:
            return
        if len(node.indices) > 0:
            for i in node.indices:
                print words[i]
        for char in string.ascii_lowercase:
            self.preorder(node.get_child(char), words)


if __name__ == '__main__':
    array = ['test', 'bbb', 'test', 'aaa', 'bba']
    trie = SortedTrie()
    for i, s in enumerate(array):
        trie.add(s, i)
    trie.print_sorted(array)
