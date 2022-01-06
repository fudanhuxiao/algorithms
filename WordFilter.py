class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)+1):
                newword = word[j:]+'#'+word
                node = self.root
                for c in newword:
                    if c not in node.children:
                        node.children[c] =  TrieNode()
                    node = node.children[c]
                    node.index = i

    def f(self, prefix: str, suffix: str) -> int:
        node = self.root
        word = suffix + '#' + prefix
        for c in word:
            if c not in node.children:
                return -1
            node = node.children[c]
        return node.index


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
