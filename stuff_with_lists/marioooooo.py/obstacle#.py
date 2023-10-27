def main():
    print('Height Obstacle:')
    n = int(input('What is the height of the obstacle? '))
    column(n)
def column(height):
    for _ in range(height):
        print('#')
main()
