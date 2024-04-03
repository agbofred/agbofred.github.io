def read_to_dict(filename):
    dictionary = {}
    with open(filename) as f:
        for line in f:
            ID, score = line.strip().split(',')
            dictionary[ID] = score
    return dictionary

def get_student_score():
    scores = read_to_dict('/Users/fjagbo/Documents/GitHub/agbofred.github.io/Spring_2024/Lecture/slides/SampleGrades.txt')
    done = False
    while not done:
        student_id = input('Enter a student id number: ')
        if student_id == "":
            done = True
        else:
            if student_id in scores:
                print(f"Student got a {scores[student_id]}.")
            else:
                print(f"Student id {student_id} was not found in classlist")

if __name__ =="__main__":
    get_student_score()