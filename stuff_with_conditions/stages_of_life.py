name = input('Enter name: ')
age = int(input('Enter age: '))
if age < 2:
    print(f'{name} is a baby')
elif age < 4:
    print(f'{name} is a toddler')
elif age < 13:
    print(f'{name} is a kid')
elif age < 20:
    print(f'{name} is a teenager')
elif age < 65:
    print(f'{name} is an adult')
else:
    print(f'{name} is an elder')
