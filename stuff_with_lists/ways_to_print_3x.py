print('Ways to print "meow" 3 times\nUsing "print" function only:')
print('meow')
print('meow')
print('meow')

print('\nUsing "while" loop:')
n=3                      
while n!=0:
    print ('meow')
    n-=1
print('OR')
n=1                             # n=0
while n<=3:                     # while n<3 
    print('meow')               # above lines give the same o/p
    n+=1
    
print('\nUsing "for" loop:')
for n in [0, 1, 2]:             # using lists ( NOTE: 'n' csn be replaced with '_'
    print('meow')               #                     as it is not used again in the program ) 
print('OR')
for n in range(3):              # 'range()' function with one argument holds value from 0 upto that argument
    print('meow')               # 2 argument of this 'range(3)': range(0, 3) or range(1, 4)

print('\nUsing "Pythonic code":')
print('meow\n'*3)