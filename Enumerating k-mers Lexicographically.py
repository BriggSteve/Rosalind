from itertools import product
for i in product('ABCD', repeat=4):
    sorted_answer = sorted(i)
    print(*i, sep='')
