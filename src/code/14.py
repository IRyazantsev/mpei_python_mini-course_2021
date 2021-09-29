names = [(1, 'Sam'), (2, 'Calvin'), (3, 'Henry'),]

def custom_key(people):
    return people[1]

names.sort(key=custom_key)
for name in names:
    print(name[1])
