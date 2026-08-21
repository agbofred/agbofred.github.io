from TMquestions import TMQuestion, read_question

class TMCourse:
    def __init__(self, questions):
        self._questions = questions
        
    def get_questions(self, name):
        return self._questions[name]
    
    def run(self):
        current = "START"
        while current !="EXIT":
            question = self.get_questions(current)
            for line in question.get_text():
                print(line)
            answer = input(">> ").strip().upper()
            next = question.look_up_answer(answer)
            if next is None:
                print("I don't understand your answer!")
            else:
                current = next
#Function to read entire courses from the data file 
def read_course(fh):
    questions = {}
    finnished = False
    while not finnished:
        question= read_question(fh)
        if question is None:
            finnished = True
        else:
            name = question.get_name()
            if len(questions)==0:
                questions["START"] = question
            questions[name]=question
    return TMCourse(questions)