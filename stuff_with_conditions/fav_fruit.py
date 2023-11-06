fav_fruits = [ 'mango', 'apple', 'banana']
fruit = input("What's my favourite fruit?\n")
if fruit.lower() in fav_fruits:
    print(f'I do love {fruit.lower()}s!')
else:
    print(f"No, I'm not a fan of {fruit.lower()}")
    
# if 'apple' in fav_fruits: print('i do love apples')
    # repeating same for each fruit returns same o/p
