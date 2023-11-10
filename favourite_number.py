fav_numbers = {
    'inej':7,
    'kaz':5,
    'jesper':69,
    'nina':25,
    'wylan':33,
}

inej = fav_numbers['inej']
kaz = fav_numbers['kaz']
jesper = fav_numbers['jesper']
nina = fav_numbers['nina']
wylan = fav_numbers['wylan']
matthias = fav_numbers.get('matthias', 'why bother?')   
# get() sets a default value if key doesn't exist (returns 'None' if default is not set)
print(f"Inej's favourite number is {inej}.")
print(f"Kaz's favourite number is {kaz}.")
print(f"Jesper's favourite number is {jesper}.")
print(f"Nina's favourite number is {nina}.")
print(f"Wylan's favourite number is {wylan}.")
print(f"Matthias's favourite number is {matthias.upper()}")
