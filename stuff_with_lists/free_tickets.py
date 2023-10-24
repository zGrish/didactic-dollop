# 4 items in the initial list
friends = [ 'harry', 'hermione', 'ron', 'ginny']
print (friends)
print (f"\nDear {friends[0].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us?\n")
print (f"Dear {friends[1].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us?\n")
print (f"Dear {friends[2].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us?\n")
print (f"Dear {friends[-1].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us?\n")

print ('--------------------------------------------------------------------------------------------')
print (f"{friends[0].title()} and {friends[2].title()} can't make it cause of 'Auror Business'\nLet's have a girls night out!")

# replacing 2 items, 4 remaining
friends[0], friends[2] = 'luna', 'hannah'
print (friends)
print (f"\nDear {friends[0].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us on the girls night out?\n")
print (f"Dear {friends[2].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us on the girls night out?\n")

print ('--------------------------------------------------------------------------------------------')
print (f"Guys I've got more tickets! I'm going to invite more people")

# adding 3 items, 7 remaining
friends.insert( 0, 'angelina' )
friends.insert( 1, 'alicia' )
friends.append('katie')
print (friends)
print (f"\nDear {friends[0].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us on the girls night out?\n")
print (f"Dear {friends[1].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us on the girls night out?\n")
print (f"Dear {friends[-1].title()}, I've got extra tickets to the Quidditch World Cup!\nWanna join us on the girls night out?\n")

print ('--------------------------------------------------------------------------------------------')
print ("Guys there was a floo mishap and we were almost fried cause the fire was normal\nThank Merlin none of us are hurt but the World Cup tickets weren't lucky\nI'm sorry but 4 tickets are gone")

print (f"\nDear {friends[0].title()}, I'm so sorry you can't accompany!\nI promise that we're definitely hanging out soon.\n")
print (f"Dear {friends[1].title()}, I'm so sorry you can't accompany!\nI promise that we're definitely hanging out soon.\n")
print (f"Dear {friends[-1].title()}, I'm so sorry you can't accompany!\nI promise that we're definitely hanging out soon.\n")
print (f"Dear {friends[-3].title()}, I'm so sorry you can't accompany!\nI promise that we're definitely hanging out soon.\n")

# removing 4 items, 3 remaining
del friends[0]
friends.remove('alicia')
friends.pop()
friends.pop(-2)
print (friends)
print (f"\nDear {friends[0].title()}, It's just the three of us now\nLet's make the best out of it\n")
print (f"Dear {friends[1].title()}, It's just the three of us now\nLet's make the best out of it\n")
print (f"Dear {friends[2].title()}, It's just the three of us now\nLet's make the best out of it\n")

print ('--------------------------------------------------------------------------------------------')
print ("It was an amazing night! We'll make plans for a bigger party soon!")

# empty list
del friends[0]
friends.remove('hermione')
friends.pop()
print (friends)
print ('--------------------------------------------------------------------------------------------')