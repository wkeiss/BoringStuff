from string import *

def countSubStringMatch(target, key):
    a = find(target, key)
    if a == -1:
        print"The keyword string appears 0 times in the target string"
    else:
        pass

def countSubStringMatchRecursive(target, key):
    b = countSubStringMatch(target, key, a)
    print"The keyword string appears %d times in the target string" % b

t = raw_input("Please input your target string.")
k = raw_input("Please input your key string.")

countSubStringMatch(t, k)
countSubStringMatchRecursive(t, k)
