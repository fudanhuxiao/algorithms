class Solution:
    def originalDigits(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c,0)+1
        freq = {}
        freq['0'] = d['z'] if 'z' in d else 0
        freq['2'] = d['w'] if 'w' in d else 0
        freq['4'] = d['u'] if 'u' in d else 0
        freq['6'] = d['x'] if 'x' in d else 0
        freq['8'] = d['g'] if 'g' in d else 0
        freq['3'] = d['h'] - freq['8'] if 'h' in d else 0
        freq['5'] = d['f'] - freq['4'] if 'f' in d else 0
        freq['7'] = d['v'] - freq['5'] if 'v' in d else 0
        freq['6'] = d['s'] - freq['7'] if 's' in d else 0
        freq['1'] = d['o'] - freq['0'] - freq['2'] - freq['4'] if 'o' in d else 0
        freq['9'] = d['i'] - freq['5'] - freq['6'] - freq['8'] if 'i' in d else 0
        return ''.join([x*freq[x] for x in sorted(freq.keys())])
            
        
        
        
