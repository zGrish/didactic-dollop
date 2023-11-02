# Create a list of travel destinations.
places = ['cappadocia', 'yoshino', 'cinque terre', 'santorini',
          'aix-en-provence', 'jokulsarlon glacier lagoon', 'kauai']

# Display the first three items in the list.
print('\nThe first three items in the list are:')
for place in places[:3]:
    print(place.title())

# Display three items from the middle of the list.
print('\nThree items from the middle of the list are:')
for place in places[2:5]:
    print(place.title())

# Display the last three items in the list.
print('\nThe last three items in the list are:')
for place in places[-3:]:
    print(place.title())
