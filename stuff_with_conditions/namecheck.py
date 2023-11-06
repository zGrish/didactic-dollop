current_users = ['shivagami', 'kattappa', 'bahubali', 'ballaladev']
new_users = ['bahubali', 'devasena', 'avantika', 'ballaladev']
for new_user in new_users:
    if new_user in current_users:
        print(f'\nUsername {new_user.title()} unavailable.\nEnter a unique username.')
    else:
        print(f'\nUsername available.\nHello {new_user.title()}!')
