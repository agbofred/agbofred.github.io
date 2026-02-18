class student:
    def __init__(self, name ="", NumofScores=4):
        self.name = name
        self.scores=[]
        for i in range(NumofScores):
            self.scores.append(0)
        
    def setscores(self, i, score):
        self.scores[i]= score
    
    def getIscore(self,i):
        return self.scores[i]
    
    def getallScores(self):
        return len(self.scores)
    
   