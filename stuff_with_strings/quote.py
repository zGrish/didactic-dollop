famous_person = input('Enter the name of a famous person you admire: ').title()
famous_quote = input(f'Enter a famous quote by {famous_person}: ').rstrip('.').capitalize()
print (f'{famous_person} once said, "{famous_quote}."')