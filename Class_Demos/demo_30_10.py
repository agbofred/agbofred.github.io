from filechooser import choose_input_file, choose_output_file
from pgl import GWindow, GImage

"""def foutput():
    filename= choose_output_file()
    if filename=="":
        print("no File name! Cancled")
    else:
        days =["Fredday", "Monday", "Teusdays", "Wednesday", "Thursday", "Friday", "Saturday", "Restday"]
        with open(filename, "w") as fh:
            for k in range(len(days)):
                fh.write(days[k]+"\n")
foutput()"""

def finput():
    filen = choose_input_file()
    gw = GWindow(800, 500)
    img = GImage(filen, 0,0)
    img.scale(gw.get_width()/(img.get_width()*2))
    gw.add(img)
finput()



"""days =["Sunday", "Monday", "Teusday", "Wednesday", "Thursday", "Friday", "Saturday"]
week = ["Week 1", "Week 2"]

with open ("weekdemo.txt", "a") as fh:
    for i in range(len(days)):
        fh.write(days[i])"""

