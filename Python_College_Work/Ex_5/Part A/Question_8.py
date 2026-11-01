def get_product():
    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = int(input("Enter price: "))
    rating = float(input("Enter rating: "))
    return (name, category, price, rating)


product = get_product()
print()

# a) Name and price using indexing
print("a) Product name:", product[0])
print("Price:", product[2])

# b) Category and rating using slicing
print("b) Category and rating:", product[1::2])

# c) Check if a value is present
value = input("c) Enter a value to search for: ")
found = False
for item in product:
    if str(item) == value:
        found = True
if found:
    print("Yes,", value, "is present in the tuple.")
else:
    print("No,", value, "is not present in the tuple.")

# d) Number of elements
print("d) Number of elements:", len(product))

# e) Unpacking
name, category, price, rating = product
print("e) The " + name + " is in the " + category + " category, costs Rs." + str(price) + " and has a rating of " + str(rating) + ".")

# f) Another tuple and concatenation
extra = (10, "In Stock")
new_product = product + extra
print("f) New tuple:", new_product)