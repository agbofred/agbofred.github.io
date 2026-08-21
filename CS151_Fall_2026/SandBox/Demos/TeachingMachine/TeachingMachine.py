from TMCourse import read_course

def teaching_machine():
    course = choose_course()
    course.run()# Run is defined in TMCourse

def choose_course():
    while True:
        try:
            filename = input("Enter course name: ")
            with open(filename + ".txt") as fh:
                return read_course(fh)# Read_course is imported from TMCourse
        except IOError:
            print("Please enter a valid course name")

if __name__ == "__main__":
    teaching_machine() 
            
