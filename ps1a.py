# Write a program that computes and prints the 1000th prime number.
# it means to find 1000 primes
count = 1
i = 3
primes = [2]

while count != 1000:
    for k in range(2,i):
        if i%k == 0:
            break
    else:# The else after for gets executed if the for loop was not broken out of prematurely.
        primes.append(i)
        count += 1
    i += 2

print primes

# thanks so much for Will Ness' answer:
#from https://stackoverflow.com/questions/15400108/how-to-generate-the-1000th-prime-in-python
