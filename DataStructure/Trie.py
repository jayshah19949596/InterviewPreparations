from collections import defaultdict


class Trie(object):
    def __init__(self):
        self.trie = defaultdict(dict)

    # Time Complexity: O(n), where is length of the word
    def add_word(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

    # Time Complexity: O(n), where is length of the word
    def search_prefix(self, word):
        node = self.trie
        for char in word:
            if char not in word:
                return False
            node = node[char]
        return True
