from TMquestions import TMQuestion, read_question
class TMCourse:
    def __init__(self, questions):
            """Creates a new TMCourse object with the specified questions."""
            self._questions = questions
    
    def get_question(self, name):
        """Returns the question with the specified name."""
        return self._questions[name]
    
    def run(self):
        """Steps through the questions in this course."""
        current = "START"
        while current != "EXIT":
            question = self.get_question(current)
            for line in question.get_text():
                print(line)
            answer = input(">>> ").strip().upper()
            next = question.lookup_answer(answer)
            if next is None:
                print("I don't understand that response.")
            else:
                current = next

def read_course(fh):
    """Reads the entire course from the data file handle fh."""
    questions = { }
    finished = False
    while not finished:
        question = read_question(fh)
        if question is None:
            finished = True
        else:
            name = question.get_name()
            if len(questions) == 0:
                questions["START"] = question
            questions[name] = question
    return TMCourse(questions)
