with open('PBride.txt') as f:
    for line in f:
        w = line.split()
        if w[0] == "You":
            print(w[-1])

with open('PBride.txt') as f:
    c = f.read().splitlines()
    print(c[1][4])
    # print(c)
    
with open('PBride.txt') as f:
    c = f.read()
    i = c.find("f")
    print(c[i:i+6])
