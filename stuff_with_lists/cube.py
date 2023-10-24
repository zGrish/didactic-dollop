cubes = []       
print('Printing the list:')         
for cube in range(1, 11):
    cubes.append(cube**3)                # joinning new iterations to the list using append()
print(cubes)                      
print('\nPrinting individual values:')
for cube in range(1, 11):
    print(cube)  

cubes = [cube**3 for cube in range(1, 11)]
print(f'\nPrinting cubes using list comprehension:\n{cubes}')    