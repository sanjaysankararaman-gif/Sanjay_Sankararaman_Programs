import math
students = {"101": {"Name": "Arun", "Python": {"CAT1": 80, "CAT2": 85}, "Java": {"CAT1": 75, "CAT2": 90} },
"102": {"Name": "Priya","Python": {"CAT1": 92, "CAT2": 95}, "Java": {"CAT1": 88, "CAT2": 91} }}

def student_details():
    for i in students:
        print("Registered Number: ", i)
        print("Name: ", students[i]["Name"])
        print("Python Marks")
        print("CAT 1: ", students[i]['Python']['CAT1'])
        print("CAT 2: ", students[i]['Python']['CAT2'])
        print("Java Marks")
        print("CAT 1: ", students[i]['Java']['CAT1'])
        print("CAT 2: ", students[i]['Java']['CAT2'])
        print()


print("Student 101 Python CAT 1: ",students['101']['Python']['CAT1'])
print()

for k,v in students.items():
    if v['Name'] == 'Priya':
        v['Java']['CAT2'] = 96

students['103'] = {'Name': 'Sanjay','Python':{'CAT1': 90, 'CAT2': 100}, 'Java':{'CAT1': 89, 'CAT2': 88}}

a = -math.inf
b = ''
for k,v in students.items():
    print('Registration Number: ',k)
    print(v['Python']['CAT1'] + v['Python']['CAT2'] + v['Java']["CAT1"] + v['Java']['CAT2'])

    if a < v['Python']['CAT1'] + v['Python']['CAT2'] + v['Java']["CAT1"] + v['Java']['CAT2']:
        a = v['Python']['CAT1'] + v['Python']['CAT2'] + v['Java']["CAT1"] + v['Java']['CAT2']
        b = v['Name']

print('Student who obtained the highest total: ',b)

