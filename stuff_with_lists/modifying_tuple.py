# Create a tuple to represent the initial menu of a buffet-style restaurant.
food_items = ('roast beef fillet', 'prawn curry', 'roast duck', 'pork loin', 'glazed ham')

# Display the initial menu using a for loop.
print('\nInitial Menu:')
for food_item in food_items:
    print(food_item.title())

# Attempt to modify an item in the tuple (this will raise a TypeError).
# Commented out to show that Python rejects the change.
# food_items[2] = 'lamb chops'  # Raises TypeError: 'tuple' object does not support item assignment

# Update the menu by creating a new tuple with two items replaced.
food_items = ('lamb chops', 'sausage casserole', 'roast duck', 'pork loin', 'glazed ham')

# Display the modified menu using a for loop.
print('\nModified Menu:')
for food_item in food_items:
    print(food_item.title())
