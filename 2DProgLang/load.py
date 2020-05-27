import re

def load(text):    
    m = re.findall('{(\d+),(\d+):([+-])([xy]),(\-?\d+),([MAS])}', text)
    if m:
        for g in m:
            i, j = g[0], g[1]
            
            d = 1 if g[2]=='+' else -1, 0
            
            if g[3] == 'y':
                d = d[::-1]
                
            x, y = d
            
            s = g[4]
            f = g[5]
            
            yield i, j, x, y, s, f