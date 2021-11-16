#sol1: hashTable
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans = []
        prefixMaps = defaultdict(set)
        for i in range(1, len(words[0])):
            for word in words:
                prefixMaps[word[:i]].add(word)
        
        def helper(step, square):
            if step == len(words[0]):
                ans.append(list(square))
                return
            prefix = []
            for prevword in square:
                prefix.append(prevword[step])
            prefix = ''.join(prefix)
            candidates = prefixMaps[prefix]
            for candidate in candidates:
                square.append(candidate)
                helper(step+1, square)
                square.pop()
        
        for word in words:
            square = [word]
            helper(1, square)
        return ans

# sol2: Trie
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans = []
        self.root = {}
        for i in range(len(words)):
            node = self.root
            for c in words[i]:
                if c not in node:
                    node[c] = {'getWords':[]}
                node = node[c]
                node['getWords'].append(i)
            
        def getWordsWithPrefix(prefix):
            node = self.root
            for c in prefix:
                if c not in node:
                    return []
                node = node[c]
            return [words[i] for i in node['getWords']]
        
        def helper(step, square):
            if step == len(words[0]):
                ans.append(list(square))
                return
            prefix = []
            for prevword in square:
                prefix.append(prevword[step])
            prefix = ''.join(prefix)
            candidates = getWordsWithPrefix(prefix)
            for candidate in candidates:
                square.append(candidate)
                helper(step+1, square)
                square.pop()
        
        for word in words:
            square = [word]
            helper(1, square)
        return ans
        
