students = ['Neville', 'Cho', 'Hannah', 'Draco']
print("Using only 'print(list_name(index))': ")
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print("\nUsing 'for' with 'print(variable_name)': ")
for student in students:
    print(student)
print("\nUsing 'len()' with 'print(variable_name)': ")
for student in range(len(students)):
    print(f'Index:{student}, Name:{students[student]}')
print('OR\nIf you wanna print just number and name:')
for student in range(len(students)):
    print(student+1, students[student])