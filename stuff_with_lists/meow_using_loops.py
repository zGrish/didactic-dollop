while True:
    n = int(input("What's the value of n? "))
    if n<=0:                                 # until 'if' is satisfied, it'll continue printing the prev line
        continue                             # OR use: if n>=0:      }
    else:                                    #         break         } yields same result    
        break

for _ in range(n):
    print('meow')
    
print('Using functions:')
def main():
    print_output(check_number())
    
def check_number():
    while True:
        n = int(input("What's the value of n? "))
        if n>=0:
            break
    return n
    
def print_output(n):
    for m in range(n):
        print('meow')
        
main()