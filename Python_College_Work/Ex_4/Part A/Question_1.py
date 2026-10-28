MyString= "Data Science 2026"

#(a)
print(MyString[0:4]) #"Data"

#(b)
print(MyString[len(MyString)-1])#"6"

#(c)
print(MyString[-6:-1])#e 202

#(d)
print(2 * MyString)#Data Science 2026Data Science 2026

#(e)
print(MyString[::-2])#60 cec tD

#(f)
print(MyString[:4] + MyString[4:])#Data Science 2026

#(g)
print(MyString.swapcase())#dATA sCIENCE 2026

#(h)
print(MyString.startswith("Data"))#True

#(i)
print(MyString.endswith("2026"))#True

#(j)
print(MyString.upper())#DATA SCIENCE 2026

#(k)
print(MyString.lower())#data science 2026

#(l)
print(MyString.count('a'))#2

#(m)
print(MyString.find("Science"))#5

#(n)
print(MyString.index("Data"))#0

#(o)
print(MyString.replace("Science","Analytics"))#Data Analytics 2026

#(p)
print(MyString.split(" "))#["Data","Science","2026"]

#(q)
print(MyString.isalpha())#False

#(r)
print("2026".isdigit())#True

#(s)
print("Data2026".isalnum())#True
