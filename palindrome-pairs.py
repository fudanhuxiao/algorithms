class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = -1
        self.suffixes = []

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root, n = TrieNode(), len(words)
        for i in range(n):
            word = words[i][::-1]
            cur = root
            for j in range(len(word)):
                if word[j:] == word[j:][::-1]:
                    cur.suffixes.append(i)
                if word[j] not in cur.children:
                    cur.children[word[j]] = TrieNode()
                cur = cur.children[word[j]]
            cur.isWord = i
                
        ans = []
        for i in range(n):
            cur = root
            findTrie = True
            for j in range(len(words[i])):
                if cur.isWord != -1 and words[i][j:] == words[i][j:][::-1]:
                    ans.append([i, cur.isWord])
                if words[i][j] not in cur.children:
                    findTrie = False
                    break
                cur = cur.children[words[i][j]]
            if findTrie:
                if cur.isWord != -1 and cur.isWord != i:
                    ans.append([i, cur.isWord])
                for k in cur.suffixes:
                    ans.append([i, k])
        return ans
            
                    
