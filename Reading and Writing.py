array = []
f = open("Sample.txt", "r")
for line in f:
    array.append(line.splitlines())
g = array[::2]
f = open("Sample.txt", "w")
f.write(str(g))
print(g)
