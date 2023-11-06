# users database
users = [ 'joe', 'admin', 'mama', 'cruella']

option = input('LOGIN or SIGN UP?\n').lower()

if option == 'login':
    login = input('\nEnter Username: ').lower()
    
    # to check whether the account exists in the database
    if login in users:
        
        # to grant extra features to admin 
        if login == 'admin':
            print(f'\nHello {login.title()}, would you like to see the status report?')
        # regular features for other users
        else:
            print(f'\nHello {login.title()}, thank you for logging in again.')
            
    else:
        print("\n---Invalid Username---\nSign Up if you don't have an account.")

elif option == 'sign up':   # 'sign up' option
    sign_up = input('\nEnter Username: ').lower()
    if sign_up in users:
        print('\nUsername unavailable.\nTry another name.')
    else:
        print(f'\nSIGN UP successful.\nWelcome, {sign_up}.')