students = {
    'Neville':'Gryffindor',
    'Cho':'Ravenclaw',
    'Hannah':'Hufflepuff',
    'Draco':'Slytherin'
}                                       # dict: connects value to key unlike value to index in lists
print('Only keys as output:')
for student in students:
    print(student, end="")        
print('Keys and values as output (with separator):')
for student in students:
    print(student, students[student], sep=', from ')