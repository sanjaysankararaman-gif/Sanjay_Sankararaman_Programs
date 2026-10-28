d = {'Name':'Arun','Age':20,"Department":'IT','Mark':85}

print(d)
print("Student Name:", d['Name'])
print("Student Mark:", d['Mark'])
print("Student Age:", d['Age'])

print(d.get('Grade', 'The given key does not exist in the dictionary'))
