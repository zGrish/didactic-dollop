def main():
    n = int(input('Enter the size of the obstacle: '))
    print_square(n)
def print_square(size):
    for i in range(size):                     # for rows
        for j in range(size):                 # for columns
            print('#', end="")
        print()
main()
# Alternative and better code:
# def main():
#     n = int(input('Enter the size of the obstacle: '))
#     print_obstacle(n)
# def print_obstacle(size):
#     for i in range(size):
#         print_row(size)
# def print_row(width):
#     print('#'*width)
# main()
