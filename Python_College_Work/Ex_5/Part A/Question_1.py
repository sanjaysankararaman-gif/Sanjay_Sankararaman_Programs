def gen_list():
    l=[i for i in range(1,21) if i%2==0 or i%3==0]
    return l
l = gen_list()
print(l)

#(a)
print("Display the complete list")
print(l)

print()

#(b)
print("Display the first and last elements")
print("The first element:", l[0])
print("The last element:",l[-1])
print()

#(c)
print("Display the first three elements")
print(l[0:3])
print()

#(d)
print("Ask the user to enter a number and check whether it is present in the list")
if int(input("Enter a number:")) in l:
    print(True)
else:
    print("False")
print()

#(e)
print("Ask the user to enter a number and display its position if it is present")
a = int(input("Enter a number:"))
if a in l:
    print(l.index(a))
else:
    print("Number not present in list")
print()

#(f)
print("Add the number 18 to the list")
l.append(18)
print(l)
print()

#(g)
print("Insert the number 12 at the second position")
l.insert(1,12)
print(l)
print()

#(h)
print("Find how many times 12 occurs in the list")
print(l.count(12))
print()

#(i)
print("Remove one occurrence of 12 from the list")
print(l.remove(12))
print()

#(j)
print("Remove the last element and display the removed element")
print(l.pop())
print()

#(k)
print("Reverse the list")
l.reverse()
print(l)
print()

#(l)
print("Arrange the elements in ascending order")
l.sort()
print(l)
print()

#(m)
print("Display the elements in descending order")
l.sort(reverse='True')
print(l)
print()

#(n)
print("Find and display the smallest value")
print(min(l))
print()

#(o)
print("Find and display the largest value")
print(max(l))
print()

#(p)
print("Calculate and display the total of all the elements")
print(sum(l))
print()

#(q)
print("Calculate and display the average of the elements")
print(sum(l)/len(l))
print()

#(r)
print("Display the total number of elements in the list")
print(len(l))
print()



