def passoword_check(s):
    if len(s) >= 8:
        u,l,d,s = 0,0,0,0
        for i in s:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1
            elif i.isdigit():
                d += 1
            elif i.isaplha():
                s += 1

        if u >= 1:
            if l >= 1:
                if d >= 1:
                    if s >= 1:
                        print("Strong Password")
                    else:
                        print("Weak Password. Include atleast one special character")
                else:
                    print("Weak Password. Include atleast one digit")
            else:
                print("Weak Password. Include atleast one lowercase character")
        else:
            print("Weak Password. Include atleast one uppercase character")
    else:
        print("Weak Password. The length of password must be greater than 8 characters")



s = input("Enter password =")

password_check(s)

            
