prompt = "\nWhat are the toppings you'd like on your pizza? "
prompt += "\n[Type 'quit' when you're finished.]\n"
#  toppings = ''
## while toppings != 'quit' [or the code below]
active = True        # here 'active' is a flag
while active: 
    toppings = input(prompt)
    if toppings == 'quit':
        active = False
    elif toppings == 'pineapple':
        print(f"You're a retarded a-hole if you want pineapple on pizza.")
    elif toppings.isalpha():
        print(f'{toppings.title()} added to your pizza.')
    else:
        print('INVALID ENTRY!!!')
        continue
