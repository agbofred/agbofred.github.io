with open('PBride.txt') as f:
    c = f.read()
    i = c.find("f")
    print(i)
    print(c[i:i+6])