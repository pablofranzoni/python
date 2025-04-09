from itertools import *
h = [(k, len(list(g))) for k, g in groupby('aaaabbbcca')]
 
print(tuple(h))
    
      
