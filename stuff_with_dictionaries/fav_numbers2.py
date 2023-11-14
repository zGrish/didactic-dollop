fav_numbers = {
    'inej':[7,11],
    'kaz':[5],
    'jesper':[69, 420],
    'nina':[25, 90],
    'wylan':[33, 18, 6]
}

print('\n')
for name, numbers in fav_numbers.items():
    print(name.title() + "'s favourite numbers are:")
    for number in numbers:
        print(number)
    print()
