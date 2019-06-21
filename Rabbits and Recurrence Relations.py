# Fn = Fn-1 + Fn-2
n = 34  # ending month
litter = 5  # litter of rabbits
Fn1 = 1
Fn2 = 1
for i in range(1, n-1):
    growth = Fn1 + Fn2 * litter
    Fn2 = Fn1
    Fn1 = growth
print(Fn1)
