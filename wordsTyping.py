class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = ' '.join(sentence)+' '
        i, n = 0, len(sentence)
        for r in range(rows):
            i += cols
            if sentence[i%n] == ' ':
                i += 1
            else:
                while i > 0 and sentence[(i-1)%n] != ' ':
                    i -= 1
        return i//n
