MARKER ="-----"
class TMQuestion:
    def __init__(self, name, text, answers):
        """Create a nre TM object"""
        self._name = name
        self._text = text
        self._answers = answers
        
    def get_name(self):
        return self._name
    
    def get_text(self):
        return self._text
    
    def look_up_answer(self, response):
        next_question = self._answers.get(response, None)
        if next_question is None:
            next_question=self._answers.get("*", None)
        return next_question

#Defining function to read a question per time outside TMQuestion class 
def read_question(fh):
    name = fh.readline().rstrip()
    if name =="":
        return None
    text =[]
    finnished = False
    while not finnished:
        line = fh.readline().rstrip()
        if line == MARKER:
            finnished = True
        else:
            text.append(line)
    answers = {}
    finnished = False
    while not finnished:
        line = fh.readline().rstrip()
        if line =="":
            finnished =True
        else:
            colon = line.find(":")
            if colon == -1:
                raise ValueError("colon is missing from "+ line)
            response =line[:colon].strip().upper()
            next_question = line[colon+1:].strip()
            answers[response] = next_question
    return TMQuestion(name, text, answers)