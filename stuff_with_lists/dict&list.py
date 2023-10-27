students = [
    {'name':'Neville', 'house':'Gryffindor', 'status':'Pureblood'},
    {'name':'Cho', 'house':'Ravenclaw', 'status':'Halfblood'},
    {'name':'Hannah', 'house':'Hufflepuff', 'status':'Pureblood'},
    {'name':'Draco', 'house':'Slytherin', 'status':'Pureblood'},
]          # multiple dicts within a list
print('\nPrinting only variable_name:')
for student in students:
    print (student)
print('\nPrinting keys:')
for student in students:
    print(student['name'], student['house'], student['status'], sep=', ')
print('OR\nFormatting it:')
for student in students:
    print(f"This is {student['name']}, from house of {student['house']} and they're a {student['status']}")