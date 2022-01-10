class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        root = TrieNode()
        
        def dfs(word, idx):
            if idx == len(word):
                return True
            node = root
            for i in range(idx, len(word)):
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                if node.isWord and dfs(word, i+1):
                    return True
            return False
        
        ans = []
        for word in words:
            if word == '':
                continue
            if dfs(word, 0):
                ans.append(word)
            else:
                node = root
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                    node = node.children[c]
                node.isWord = True
        return ans
