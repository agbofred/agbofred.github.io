from typing import Any


MARKER ="-----"

class TMQuestion:
    def __init__(self, name, text, answers):
        self._name = name
        self._text = text
        self._answers = answers

    def get_name(self): # rerturns the name of the question
        return self._name
    
    def get_text(self):
        return self._text # return the list containing text of the question
    
    def lookup_answer(self, response):
        next_question = self._answers.get(response, None)
        if next_question is None: 
            next_question = self._answers.get("*", None)
        return next_question

def read_question(fh):
    name = fh.readline().rstrip()
    if name =="":
        return None
    text =[ ]
    finished = False
    while not finished:
        line =fh.readline().rstrip()
        if line == MARKER:
            finished = True
        else: 
            text.append(line)
    answers = { }
    finished = False
    while not finished:
        line = fh.readline().rstrip()
        if line == "":
            finished = True
        else:
            colon =line.find(":")
            if colon == -1:
                raise ValueError("missing colon in "+line)
            response= line[:colon].strip().upper()
            next_question = line[colon + 1:].strip()
            answers[response] = next_question
    return TMQuestion(name, text, answers)
