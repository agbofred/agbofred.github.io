from filechooser import choose_input_file, choose_output_file

filename = choose_input_file()
with open(filename) as f:
    
    data = f.read()
    
filename = choose_output_file()
with open(filename, "a") as f:
    f.write("Here are the new stuff")
    