def valid_email(s):
    s1 = s
    s1 = (s1.strip()).lower()

    if s1.endswith('@snuchennai.edu.in') or s1.endswith('@ssn.edu.in'):
        print("Valid Email")
    else:
        print("Invalid Email")

s = input("Enter your email =")

valid_email(s)
