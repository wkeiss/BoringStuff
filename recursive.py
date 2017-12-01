# code for learning recursive function.
# I try to write a function that call itself.
def showyourself(x):
    print x
    if x != 0:
        print showyourself(x - 1)

x =int(raw_input("what number you would like to count?     "))
showyourself(x)
