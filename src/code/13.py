names = [(1, 'Sam'), (2, 'Calvin'), (3, 'Henry'),]
names_new = []
for name in names:
    names_new.append(name[1])

names_new.sort()
for name in names_new:
    print(name)
