# team members database
members = [ 'joe', 'admin', 'mama', 'cruella']

# making sure that list is not empty
if members:
    for member in members:
        if member == 'admin':
            print(f'Hello {member.title()}, would you like to see the status report?')
        else:
            print(f'Hello {member.title()}, thank you for logging in again.')
else:
    print('No members available.')
