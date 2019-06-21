from itertools import permutations
nmb_perm = []
perm = permutations([1, 2, 3, 4, 5])
for i in list(perm):
    nmb_perm.append(str(i)[1:-1])
    n = ''.join(str(i))[1:-1]
    print(n.replace(", ", " "))
print(len(nmb_perm))
