class TrieNode:
    def __init__(self):
        self.children = {}
        self.top3 = []

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.freq = {sentences[i]:times[i] for i in range(len(times))}
        self.curNode = self.root
        self.curInput = []
        for i in range(len(times)):
            self.addSentence(sentences[i], times[i])
        
    def addSentence(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if sentence in node.top3:
                node.top3.sort(key=lambda x: [-self.freq[x], x])
            else:
                if len(node.top3) < 3:
                    node.top3.append(sentence)
                    node.top3.sort(key=lambda x: [-self.freq[x], x])
                elif count >= self.freq[node.top3[-1]]:
                    node.top3.append(sentence)
                    node.top3.sort(key=lambda x: [-self.freq[x], x])
                    node.top3.pop()

    def input(self, c: str) -> List[str]:
        if c == '#':
            sentence = ''.join(self.curInput)
            self.freq[sentence] = self.freq.get(sentence, 0)+1
            self.addSentence(sentence, self.freq[sentence])
            self.curNode, self.curInput = self.root, []
            return []
        
        node = self.curNode
        if node is None or c not in node.children:
            self.curNode = None
            self.curInput.append(c)
            return []
        node = node.children[c]
        self.curNode = node
        self.curInput.append(c)
        return node.top3
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
