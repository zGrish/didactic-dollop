people = []

person = {'name':'percy jackson', 'gender':'male', 'age':18, 'species':'demigod'}
people.append(person)
person  = {'name':'annabeth chase', 'gender':'female', 'age':18, 'species':'demigod'}
people.append(person)
person = {'name':'grover underwood', 'gender':'male', 'age':'16(33)', 'species':'satyr'}
people.append(person)
person = {'name':'tyson ', 'gender':'male', 'age':'N/A', 'species':'cyclops'}
people.append(person)
person = {'name':'chiron ', 'gender':'male', 'age':'unknown', 'species':'centaur'}
people.append(person)
person = {'name':'sally jackson', 'gender':'female', 'age':41, 'species':'human'}
people.append(person)

for person in people:
    name = person['name'].title()
    age = str(person['age'])
    gender = person['gender'].title()
    species = person['species'].title()
    print('Name:  ' + name)
    print('Age: ' + age)
    print('Gender: ' + gender)
    print('Species: ' + species + '\n')
