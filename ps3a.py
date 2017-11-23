from string import *
count = 0
def countSubStringMatch(target, key):
    while count != -1:
        a = find(target, key)
        b = len(key)
        count += 1
        a += b
    print count
