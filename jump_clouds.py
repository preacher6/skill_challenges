c = [0, 0, 0, 0, 1, 0]
c = [0, 1, 0, 1, 0, 1, 0, 0]
#c = [0, 0, 0, 1, 0, 0]

jumps = 0
actual = 0
while actual != len(c)-1:
    jumps += 1
    if c[actual+2] == 0:
        actual = actual+2
    else:
        actual = actual+1

    if actual == len(c)-2:
        jumps += 1
        actual += 1

