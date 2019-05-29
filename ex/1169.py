n = int(input())
while n:
    x = int(input())
    total = 1
    while x:
        total *= 2
        x -= 1
    print('{:d} kg'.format(total//12000))
    n -= 1