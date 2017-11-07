# Write a program that computes and prints the 1000th prime number.
x = 3

while x != 1000:
    for y in range(2, x):
        if  x % y == 0:
            break
        else:
            print x
    x = x + 1
