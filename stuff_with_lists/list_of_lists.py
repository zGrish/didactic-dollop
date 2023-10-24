fruits = ['mango', 'apple', 'banana']
animals = ['cat', 'dog', 'rat']
metals = ['gold', 'silver', 'copper']
listoflists = [fruits, animals, metals]
print(f'\n{listoflists}')

# 1st letter of each item in each list is considered to check alphabetical order not the names of lists

print(f'\n{sorted(listoflists)}') # temporary alphabetical ascending order
print(sorted(listoflists, reverse=True)) # temporary alphabetical descending order

listoflists.reverse() # permanenent reverse 
print(f'\n{listoflists}')
listoflists.reverse() # reverse again to get og list
print(listoflists)

listoflists.sort() # permanent alphabetical ascending order
print(f'\n{listoflists}') 
listoflists.sort(reverse=True) # permanent alphabetical descending order
print(f'{listoflists}')