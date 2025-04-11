from TMcourse import TMCourse, read_course

def TM():
    course= choose_course()
    course.run()
    
def choose_course():
    while True:
        try:
            filename = input("Enter course name: ")
            with open(filename+".txt") as fh:
                return read_course(fh)
        except IOError:
            print("Please enter a valid file name")
if __name__ =="__main__":
    TM()