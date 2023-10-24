numbers = list(range(1, 1000001))                              # list in range of 1 to 1 mil 
print('Numbers from 1 to 1 million:')                          
for number in numbers:                                         # for variable_name in list_name
    print(number)                                              # in-loop statement, prints numbers individually
print(f'List of numbers from 1 to 1 million: {numbers}')       # prints numbers as a list
print(f'Smallest number: {min(numbers)}')                      # smallest number using min() function
print(f'Largest number: {max(numbers)}')                       # smallest number using min() function
print(f'Sum of the numbers in the list: {sum(numbers)}')       # sum using min() function