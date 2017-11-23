from string import *
def countSubStringMatch(target, key):
    a = find(target, key)
    b = len(key)
    count = 0
    while a != -1:
        a = find(target, key, (a + b))
        count += 1
    print count
countSubStringMatch("snbdcmpfmfdlndom", "njskemak")
