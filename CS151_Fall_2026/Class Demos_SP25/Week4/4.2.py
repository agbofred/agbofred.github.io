row = ""
for i in range(32, 127):
    if len(row) == 32:
        print(row)
        row = ""
    row = row + chr(i) + " "
print(row)