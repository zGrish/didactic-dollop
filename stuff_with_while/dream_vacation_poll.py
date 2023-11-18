poll = {}
print()
active = True
while active:
    name = input("What's your name? \n\t")
    dream = input("If you could visit any place in the world," 
                  "where would you go? \n\t")
    poll[name] = dream
    another_one = input("Would you like to send this poll for"
          "someone else to answer? (yes/no) ")
    if another_one == 'no':
        active = False
        
print('\n\n----------- Poll Results -----------\n')
for name, dream in poll.items():
    print(f"{name.title()} would like to visit {dream.title()}")
