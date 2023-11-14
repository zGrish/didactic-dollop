sources = {
    'nile':'egypt',
    'ganga':'india',
    'amazon':'brazil',
    'yangtze':'china',
    'volga':'russia'
}
print()
for river, country in sources.items():
    print(f'The {river.title()} runs through {country.title()}')
print()
print('The following rivers are mentioned in this data set:')
for river in sources.keys():
    print('- The ' + river.title())
print()
print('The following countries are mentioned in this data set:')
for country in sources.values():
    print('- ' + country.title())
