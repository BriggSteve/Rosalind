from itertools import product
for i in product('ABCD', repeat=4):
    print(*i, sep='')
