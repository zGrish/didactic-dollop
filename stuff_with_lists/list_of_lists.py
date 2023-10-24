fruits = ['mango', 'apple', 'banana']
animals = ['cat', 'dog', 'rat']
metals = ['gold', 'silver', 'copper']
listoflists = [fruits, animals, metals]
print(f'\n{listoflists}')

print(f'\n{sorted(listoflists)}') # 1st letter of each item in each list is considered to check alphabetical order not the names of lists
print(sorted(listoflists, reverse=True)) # ,,

listoflists.reverse() # reverse
print(f'\n{listoflists}')
listoflists.reverse() # reverse again to get og list
print(listoflists)

listoflists.sort()
print(f'\n{listoflists}')
listoflists.sort(reverse=True)
print(f'{listoflists}')


