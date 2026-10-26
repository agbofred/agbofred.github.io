from filechooser import choose_input_file, choose_output_file
# filename= choose_output_file()
# try:
#     with open(filename, "a") as fh:
#         fh.write("Here is a new text")
# except IOError:
#     print("The file location is not correct")
    
from filechooser import choose_input_file, choose_output_file
filename= choose_input_file()
try:
    with open(filename, "r") as fh:
        data= fh.read()
        print(data)
except IOError:
    print("The file location is not correct")