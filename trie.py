# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
from typing import Tuple


class TrieNode:
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1


class Trie:
    def __init__(self, root):
        self.root = root

    def add(self, word):
        """
        Adding a word in the trie structure
        """
        node = self.root
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        leaf = TrieNode('*')
        node.children.append(leaf)
        leaf.word_finished = True

    def find_prefix(self, prefix):
        """
        Check and return 
        1. If the prefix exsists in any of the words we added so far
        2. If yes then how may words actually have the prefix
        """
        node = self.root
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not node.children:
            return False, 0
        for char in prefix:
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return False, 0
        # Well, we are here means we have found the prefix. Return true to indicate that
        # And also the counter of the last node. This indicates how many words have this
        # prefix
        return True, node.counter

    # Count total number of words in Trie
    def num_of_words(self):
        return self._num_of_words(self.root)

    def _num_of_words(self, node):
        count = 0
        if node.word_finished:
            count += 1
        for node in node.children:
            count += self._num_of_words(node)
        return count

    # get all the words in trie
    def list_words(self):
        return self._list_words(self.root)

    def _list_words(self, node):
        words = []
        for child in node.children:
            # if there are still chars to explore
            if not child.word_finished:
                # build the word
                for el in self._list_words(child):
                    words.append(child.char + el)
            else:
                words.append('')
        return words


if __name__ == '__main__':
    root = TrieNode('*')
    trie = Trie(root)
    trie.add('hackathon')
    trie.add('test')
    trie.add('hack')
    trie.add('hack')
    trie.add('testing')
    print trie.num_of_words()
