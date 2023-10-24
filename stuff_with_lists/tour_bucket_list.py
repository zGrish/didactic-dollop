# list is created
places = [ 'Cappadocia', 'Yoshino', 'Cinque Terre', 'Santorini', 'Aix-en-Provence', 'Jokulsarlon Glacier Lagoon']
print (f'List in the original order: {places}')

# temporarily arranged in alphabetical order using 'sorted()' 
print (f'\nList modified using sorted() method: {sorted(places)}')
# og list is not changed
print (f'List after modifying: {places}')

# temporarily arranged in reverse-alphabetical order using 'sorted(list_name, reverse=True)' 
print (f'\nList modified using sorted-reverse method: {sorted(places, reverse=True)}')
# og list is not changed
print (f'List after modifying: {places}')

# permanently arranged in reverse order using 'reverse()' 
print (f'\nList modified using reverse() method: {places.reverse()}')
# og list is changed to ulta
print (f'List after modifying: {places}')

# permanently rearranged in reverse order again using 'reverse()' 
print (f'\nReversing the list again using reverse(): {places.reverse()}')
# og list is changed to ulta again == og order
print (f'List after modifying: {places}')

# permanently arranged in alphabetical order using 'sort()' 
print (f'\nList modified using sort() method: {places.sort()}')
# og list is changed
print (f'List after modifying: {places}')

# permanently arranged in reverse-alphabetical order using 'sort()' 
print (f'\nList modified using sort-reverse method: {places.sort(reverse = True)}')
# og list is changed
print (f'List after modifying: {places}')