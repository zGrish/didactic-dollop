print('\nThis Deli has run out of Pastrami Sandwiches.'
      '\nSorry for the inconvienence')

print('\nList of the items ordered by customers:')
sandwich_orders = ['pastrami', 'ham', 'pastrami', 'tuna', 
                   'grilled', 'veggie', 'pastrami', 'egg', 'chicken']
print(sandwich_orders)
opted_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('\nList after removing unavailable items:')
print(sandwich_orders)

print()

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich.title()} Sandwich is ready.")
    opted_sandwiches.append(sandwich)
   
print('\nHere is the list of sandwiches that have been chosen:')
for opted_sandwich in opted_sandwiches: 
    print(f'{opted_sandwich.title()}')
