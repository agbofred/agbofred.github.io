
def parse_file_to_dict(filename):
    """Opens and reads from a file to parse the information into a dictionary

    Args:
        filename (string): The name of the file to open
    Returns:
        (dict): The dictionary with names as keys and grades as values
    """
    with open(filename) as fh:
        dic ={}
        for lines in fh:
            d = lines.strip().split(',')
            dic[d[0]] = d[1]
    return dic

def get_student_grade(grade_dict):
    """Prompts the user to enter in a student's name and then prints out the
    corresponding grade.

    Args:
        grade_dict (dict): The dictionary of names and corresponding grades
    Returns:
        None
    """
    stu_name = input("Enter the student name:> ")
    if stu_name in grade_dict:
        print(grade_dict[stu_name])
    else:
        print(f"No student called {stu_name} exists")


def get_students_with_grade(grade_dict):
    """Prompts the user to enter in a letter grade and then prints out all students who
    currently have that grade.

    Args:
        grade_dict (dict): The dictionary of names and corresponding grades
    Returns:
        None
    """
    stu_grade = input("Enter Grade:> ")
    for name, grade in grade_dict.items():
        if stu_grade == grade:
            print(name)

if __name__ == '__main__':
    grades = parse_file_to_dict('grades.txt')
    print(grades)

    # get_student_grA
    # ade(grades)
    get_students_with_grade(grades)
