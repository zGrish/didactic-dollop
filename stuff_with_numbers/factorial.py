def factorial(numf):
    """To read parameter, calculate and return it's factorial"""
    fact = 1
    for i in range(1, numf + 1):
        fact = fact * i
    return fact

# USING RECURSION
    # def factorial(numf):
        # if numf == 0:
        #     return 1
        # else:
        #     return numf * factorial(numf - 1)

def main():
    num = int(input("\nEnter any number: "))
    print(f"The factorial of {num} is {factorial(num)}\n")
    
main()
