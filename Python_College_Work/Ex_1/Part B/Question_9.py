string = str(input("Enter a string in lowercase:"))

upper_string = ""

for i in string:
    new_char = chr(ord(i) - 32)
    upper_string += new_char

print(string, "in uppercase is", upper_string)