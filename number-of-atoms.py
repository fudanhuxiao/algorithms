class Solution:
    def countOfAtoms(self, formula: str) -> str:
        d, stack, coeff, elem, cnt, i = {}, [], 1, '', 0, 0
        for j in range(len(formula)-1, -1, -1):
            c = formula[j]
            if c.isdigit():
                cnt += int(c)*(10**i)
                i += 1
            elif c == ')':
                count = cnt if cnt > 0 else 1
                stack.append(count)
                coeff *= count
                cnt, i = 0, 0
            elif c.isupper():
                elem = c+elem
                count = cnt if cnt > 0 else 1
                d[elem] = d.get(elem, 0)+count*coeff
                elem, cnt, i = '', 0, 0
            elif c == '(':
                coeff //= stack.pop()
            elif c.islower():
                elem = c+elem
        return ''.join([k+str(v) if v>1 else k for k, v in sorted(d.items())])
            
                
