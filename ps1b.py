"""Write a program that computes the sum of the logarithms
of all the primes from 2 to some number n
and print out the sum of the logs of the primes, the number n,
and the ratio of these two quantities."""
from math import *

count = 1
n = int(raw_input("n = ? >"))
i = 3
logs = log(2)

while count != n:
    for k in range(2, 1 + int(sqrt(i + 1))):
        if i % k == 0:
            break
    else:
        logs = logs + log(i) # compute the sum of the logarithms
        count += 1

i += 2


print "The sum of the logs of the primes is %d." % logs
print "The number n is %d." % n
print "The ratio of these two quantities is %d." % (logs / n)
