def get_existing_file(prompt="Input a filename: "):
    while True:
        filename = input(prompt)
        try:
            with open(filename):
                return filename
        except IOError:
            print("That filename is invalid!")
            
file = get_existing_file()

with open(file) as f:
    data =f.read()
print(data)
    