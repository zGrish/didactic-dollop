alien_colour = [ 'green', 'yellow', 'red']
print(alien_colour)
colour = input('What is the colour of the alien shot down?\n')
if colour.lower() == 'green':
    print('You just earned 5 points!')
elif colour.lower() == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')
