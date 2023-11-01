file = "todaydemo.txt"
with open(file) as fh:
    data = fh.read()
with open(file, 'a') as fh:
    fh.write(data[::-1])