# Write a program that computes and prints the 1000th prime number.
prime = []

for x in range(3, 7920):
    for y in range(2, x):
        if x % y == 0:
            x = x + 1
        else:
            prime.append(x)

print "The first 1,000 primes:"
print prime
