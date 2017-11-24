from string import *

def countSubStringMatch(target, key):
    a = find(target, key)
    count = 0

    while a != -1:
        b = len(key)
        index = a + b
        a = find(target, key, index)
        count = count + 1

    print "The key string presents", count, "time/times in target string."

t = raw_input("please input your target string.")
k = raw_input("please input your key string." )
countSubStringMatch(t, k)
