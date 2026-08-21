from TMQuestion import TMQuestion, read_question
class TMCourse:
    def __init__(self, questions):
        self._questions = questions
    
    def get_question(self, name):
        return self._questions[name]
    
    def run(self):
        current ="START"
        while current!="EXIT":
            question = self.get_question(current)
            for line in question.get_text(): # get_text will be defined in TMQuestions
                print(line)
            answer= input("> ").strip().upper()
            next = question.lookup_answer(answer) # Look_up answer is defined in TMQuestions
            if next is None:
                print("I do not understand that response.")
            else:
                current = next
def read_course(fh):
    questions ={ }
    finished = False
    while not finished:
        question = read_question(fh) # read_question is defined in TMQuestion
        if question is None:
            finished = True
        else:
            name = question.get_name() # get_name is defined in TMQuestion
            if len(questions)==0:
                questions["START"] = question
            questions[name] = question
    return TMCourse(questions)


