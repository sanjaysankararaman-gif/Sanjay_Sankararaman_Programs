books = {"Python": 450, "Java": 500, "C": 300}
print(books)

books['C++'] = 400
print(books)

books['Python'] = 480
print(books)

books.pop('C')
print(books)

print("Number of books: ", len(books))

print(books.get('Java','Key not present in dictionary'))

books.update({'SQL':350})

books_copy = books.copy()
books_copy.clear()
print(books_copy)
