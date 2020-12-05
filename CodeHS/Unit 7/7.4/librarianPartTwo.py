authors = []
for auth in range(5):
    author = input('Name: ')
    splitList = author.split()
    authors.append(splitList[1])

authors.sort()
print(authors)
