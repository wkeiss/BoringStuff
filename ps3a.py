from string import *

def countSubStringMatch(target, key):
    a = find(target, key)
    b = len(key)
    count = 0
    while a == -1:
        index = a + b
        a = find(target, key, index)
        count += 1
    print "The key string presents %d time/times in target string." % count

t = raw_input("please input your target string, which must contain double-qoute.")
k = raw_input("please input your key string, which must contain double-qoute." )
countSubStringMatch(t, k)
