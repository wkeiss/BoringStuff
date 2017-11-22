McNuqqets = [50, 51, 52, 53, 54, 55]

for n in McNuqqets:
    for a in range(0, 10):
        for b in range(0, 7):
            for c in range(0, 3):
                if 6 * a + 9 * b + 20 * c == n:
                    print "a = %d" % a, "b = %d" % b,"c = %d" % c,"n = %d" % n
                else:
                    break
