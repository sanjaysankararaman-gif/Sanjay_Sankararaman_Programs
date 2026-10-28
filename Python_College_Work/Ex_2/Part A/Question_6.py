sent = input("Enter a sentence:")

vowels = 0 #initialising var vowel to zero to count the number of vowels

for i in sent: #Every i is a character in the string sent
    print(i)
    if i in "AEIOUaeiou":
        vowels +=1
        
    else:
        continue

    

print("Number of vowels =", vowels)
