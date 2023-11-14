polled = {
    'percy':'poseidon',
    'annabeth':'athena',
    'nico':'hades'
}

print('\nPoll results:')
for name, parent in polled.items():
    print(f'{name.title()} is the child of {parent.title()}.')
print()

charecters = ['percy', 'annabeth', 'grover', 'nico', 'thalia']
        
for charecter in charecters:
    if charecter in polled.keys():
        print("Thank you for taking the "
              "poll, " + charecter.title() + ".")   # you can cut print() like this
    else:
        print(charecter.title() + ", please take the poll.")
