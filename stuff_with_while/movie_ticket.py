while True:
    age = input("\nHow old are you? ")
    if age == 'quit':
        break
    elif age.isnumeric():
        age = int(age)
        if age <= 3:
            print(f"\tNo ticket fee for persons under the age of 3")
        elif 3 < age < 12:
            print(f"\tYour ticket costs $10")
        else:
            print(f"\tYour ticket costs $15")   
    else:
        print('INVALID ENTRY!!!')
        continue  
