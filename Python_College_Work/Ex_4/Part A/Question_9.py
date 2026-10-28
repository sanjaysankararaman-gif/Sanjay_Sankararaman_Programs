def file_ext_check(s):
    s1 = s
    s1 = s1.strip()
    if s1.endswith('.txt') or s1.endswith('.pdf') or s1.endswith('.docx'):
        print("Valid File Type")
    else:
        print("Invalid File Type")


s = input('Enter file name with the file extension =')

file_ext_check(s)
