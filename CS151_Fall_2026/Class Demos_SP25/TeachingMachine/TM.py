from TMcourse import read_course
 
def teaching_machine():
    course = choose_course()
    course.run()
 
def choose_course():
    """
    Returns a course chosen by the user.
    """
    while True:
        try:
            filename = input("Enter course name: ")
            with open(filename + ".txt") as f:
                return read_course(f)
        except IOError:
            print("Please enter a valid course name.")
 
 
# Startup code
 
if __name__ == "__main__":
    teaching_machine()