print('Printing odd numbers within 1-20 by defining range:')
odd_numbers = range(1, 21, 2)              # list from range 1 to 20 with 2 as step size (to be added to initial value)
for odd_number in odd_numbers:             # for variable_name in list_name
    print(odd_number)                      # in-loop statement, prints numbers individually
print(f'\n')
print('Printing odd numbers within 1-20 by using emptyt list:')
odd_numbers = []                           # empty list
for odd_number in range(1, 21, 2):         # for variable_name in range 1 to 21 with 2 as step size
    print(odd_number)                      # in-loop statement, prints numbers individually