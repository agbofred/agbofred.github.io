row= ""
for i in range(32, 128):
    # print(i, chr(i))
    if len(row)== 32:
        print(row)
        row =""
    row = row + chr(i) + " "
print(row)