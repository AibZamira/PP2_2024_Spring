def P(n):
    perm_set = itertools.permutations(st) 

    for i in perm_set: 
        print(i)

import itertools

string = tuple(map(str, input().split())) 
P(string)
