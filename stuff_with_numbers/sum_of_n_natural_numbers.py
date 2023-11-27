def natural(numf):
    sum = 0
    for i in range(1, numf + 1):
        sum += i
    return sum

# USING RECURSION
    # def natural(numf):
        # if numf == 0:
            # return 0
        # else:
            # return numf + natural(numf - 1)

num = int(input("\nEnter any number: "))
print(f"Sum of {num} natural numbers: {natural(num)}\n")
