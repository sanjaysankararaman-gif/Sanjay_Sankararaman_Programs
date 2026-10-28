def course_code_validation(s):
    s1 = s
    s1 = (s1.strip()).upper()

    if len(s) == 8:
        if s[0].isdigit() and s[1].isdigit():
            if s[2].isalpha() and s[3].isalpha():
                if s[-1].isdigit() and s[-2].isdigit() and s[-3].isdigit() and s[-4].isdigit():
                    print("Display Valid Course Code")
                    print("Year/Batch:",s1[:2])
                    print("Department:",s1[2:4])
                    print("Course Number:",s1[-1:-5:-1])
                else:
                    print("Invalid Course Code")
            else:
                print("Invalid Course Code")
        print("Invalid Course Code")
    else:
        print("Invalid Course Code")

course_number = input("Enter course code: ")
course_code_validation(course_number)
