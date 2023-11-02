# Define a list of favorite pizzas.
my_fav_pizzas = ['pepperoni', 'BBQ', 'cheese']

# Display the original list of favorite pizzas.
print(f'\nBefore copying:\n{my_fav_pizzas}')

# Create a copy of the original list using slicing.
friend_fav_pizzas = my_fav_pizzas[:]

# Display the original and copied lists before appending new pizzas.
print(f'\nAfter copying, before appending:')
print(f"My favourites: {my_fav_pizzas}\nMy friend's favourites:{friend_fav_pizzas}\n")

# Append different pizzas to both lists.
my_fav_pizzas.append('hawaiian')
friend_fav_pizzas.append('margherita')

# Display the updated lists after appending new pizzas.
print('After appending:')
print('My favourite pizzas are:')
for pizza in my_fav_pizzas:
    print(pizza.title())
print("\nMy friend's favourite pizzas are:")
for pizza in friend_fav_pizzas:
    print(pizza.title())
